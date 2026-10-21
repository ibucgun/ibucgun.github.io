#!/usr/bin/env python3
"""ismailbucgun.com metin denetimi.

Kullanım:
  denetle.py <dosya> [<dosya> ...]      Tara: mevzuat bayrakları + yazım izleri (+ sayfalar arası tekrar)
  denetle.py --yedekle <dosya>          Düzeltmeden önce yedek al
  denetle.py --karsilastir <dosya>      Yedekle karşılaştır; dokunulmaz değişmişse çıkış kodu 1
  denetle.py --json ...                 Makine okunur çıktı

Bayraklar adaydır, hüküm değildir: her birini bağlamında değerlendir (bkz. SKILL.md).
"""
import html
import json
import os
import re
import statistics
import sys
import tempfile
from collections import Counter

# ---------------------------------------------------------------- yardımcılar

def tr_lower(s):
    return s.replace("I", "ı").replace("İ", "i").lower()


def metin_turu(yol):
    ad = os.path.basename(yol)
    if "/_posts/" in yol.replace(os.sep, "/") or yol.startswith("_posts"):
        return "blog"
    if ad.split(".")[0] in ("aydinlatma-metni", "acik-riza", "cerez-politikasi"):
        return "yasal"
    return "hasta"


def ayir(icerik):
    """Front matter ve gövdeyi ayır. (fm_satirlari, govde, govde_ilk_satir_no)"""
    m = re.match(r"\A---\n(.*?)\n---[ \t]*(?:\n|\Z)", icerik, re.S)
    if not m:
        return [], icerik, 1
    fm = m.group(1).split("\n")
    return fm, icerik[m.end():], len(fm) + 3


GORUNUR_FM = ("title", "seo_title", "description", "lead", "acil", "acil_baslik")
DUZELTILEBILIR_FM = ("description", "lead")


def fm_anahtarlari(fm_satirlari):
    """Üst düzey anahtar -> ham değer metni (devam satırlarıyla)."""
    d, anahtar = {}, None
    for s in fm_satirlari:
        m = re.match(r"^([A-Za-z_][\w-]*):\s?(.*)$", s)
        if m:
            anahtar = m.group(1)
            d[anahtar] = m.group(2)
        elif anahtar is not None:
            d[anahtar] += "\n" + s
    return d


def fm_degeri(ham):
    v = ham.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1].replace('\\"', '"')
    return v


ATLA = [
    r"<script\b.*?</script>", r"<style\b.*?</style>", r"<svg\b.*?</svg>", r"<!--.*?-->",
    r"\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}",
    r'<nav class="tms-toc".*?</nav>', r"```.*?```",
]


def satir_metinleri(icerik):
    """[(satir_no, duz_metin, tur)] — HTML/Liquid/Markdown temizlenmiş görünür metin.
    tur: 'govde' | 'baslik' (H1–H6, title, seo_title, acil_baslik) | 'meta' (description)."""
    fm, govde, ilk = ayir(icerik)
    sonuc = []
    anahtarlar = fm_anahtarlari(fm)
    for i, s in enumerate(fm):
        m = re.match(r"^([A-Za-z_][\w-]*):\s?(.*)$", s)
        if m and m.group(1) in GORUNUR_FM:
            alan = m.group(1)
            tur = "baslik" if alan in ("title", "seo_title", "acil_baslik") else ("meta" if alan == "description" else "govde")
            sonuc.append((i + 2, fm_degeri(m.group(2)), tur))
    temiz = govde
    for desen in ATLA:
        temiz = re.sub(desen, lambda m: "\n" * m.group(0).count("\n"), temiz, flags=re.S)
    for j, s in enumerate(temiz.split("\n")):
        baslik = bool(re.search(r"<h[1-6]\b", s)) or bool(re.match(r"\s*#{1,6}\s", s))
        t = re.sub(r"\{%.*?%\}|\{\{.*?\}\}", " ", s)
        t = re.sub(r"<[^>]*>", " ", t)
        t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
        t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
        t = re.sub(r"\*\*|__", "", t)
        t = re.sub(r"^\s*#{1,6}\s*", "", t)
        t = re.sub(r"\s+", " ", html.unescape(t)).strip()
        if t:
            sonuc.append((ilk + j, t, "baslik" if baslik else "govde"))
    return sonuc, anahtarlar


# ---------------------------------------------------------------- desenler

# (kod, kategori, düzey, açıklama, regex)
MEVZUAT = [
    ("A1", "üstünlük", "İHLAL", "üstünlük iddiası", r"\ben (iyi|deneyimli|başarılı|güvenilir|kaliteli|etkili|donanımlı|yetkin)\b"),
    ("A1", "üstünlük", "İHLAL", "benzersizlik", r"\btek (merkez|hekim|uzman|adres|muayenehane)\b"),
    ("A1", "üstünlük", "İHLAL", "yer/ilk iddiası", r"(adana|türkiye|bölge|çukurova)['’]?(nın|nin|da|de|daki|deki)? (ilk|tek|en)\b"),
    ("A1", "üstünlük", "İHLAL", "karşılaştırmalı konumlandırma", r"klasik uzmanlığın ötesinde|diğer (uzman|hekim|psikiyatrist|doktor)\w*[^.]{0,40}(farklı|aksine)"),
    ("A1", "üstünlük", "RİSK", "üstünlük çağrışımı", r"\b(lider|öncü|ayrıcalıklı)\b"),
    ("A1", "üstünlük", "RİSK", "'nadir' (tıbbi sıklık mı, üstünlük mü?)", r"\bnadir\b"),
    ("A2", "sayı/başarı", "İHLAL", "hasta sayısı", r"\b(yüzlerce|binlerce|onlarca|çok sayıda)\s+(hasta|kişi|danışan)"),
    ("A2", "sayı/başarı", "RİSK", "oran (literatür çerçevesi var mı?)", r"(başarı|iyileşme|yanıt) oran|%\s?\d+"),
    ("A3", "kesinlik", "İHLAL", "garanti/kesin sonuç", r"\bgaranti|\bkesin (sonuç|iyileş|geçer|tedavi)|\bmucize|\brisksiz\b|\bzararsız\b"),
    ("A3", "kesinlik", "İHLAL", "yan etki inkârı", r"yan etki(si|leri)? (yok|yoktur|görülmez|olmaz)"),
    ("A3", "kesinlik", "İHLAL", "mutlak sonuç", r"tamamen (iyileş|geçer|ortadan kalkar)|\bmutlaka (iyileş|düzel|geçer)"),
    ("A3", "kesinlik", "RİSK", "genelleme/kesinlik", r"\bher hastada\b|kalıcı (çözüm|iyileşme)|\bkesinlikle\b"),
    ("A4", "tesis", "İHLAL", "tesis/konfor övgüsü", r"\b(konforlu|lüks|ferah|son teknoloji)\b|modern (muayenehane|cihaz|ortam)"),
    ("A4", "tesis", "RİSK", "konum/otopark üstünlüğü", r"otopark|merkezi konum"),
    ("A5", "sunulmayan", "İHLAL", "psikoterapi hizmet beyanı", r"(psikoterapi|bdt|kipt)(?:(?!tms|esketamin|ilaç|parlak)[^.]){0,80}(uyguluyorum|uygulanmaktadır|yapıyorum|veriyorum|vermekteyim|uygulamaktayım)\b"),
    ("A5", "sunulmayan", "İHLAL", "esketamin deneyim ima", r"esketamin[^.]{0,150}uyguluyorum"),
    ("A5", "sunulmayan", "İHLAL", "EKT/tDCS uygulanıyor ima", r"\b(ekt|elektrokonvülsif|tdcs)\b[^.]{0,80}(uyguluyorum|uygulanmaktadır|yapıyorum)\b"),
    ("A5", "sunulmayan", "İHLAL", "'ilk muayene yüz yüze' (kontroller online sanılır)", r"ilk (muayene|görüşme)(?:(?!kontrol|takip)[^.]){0,60}yüz ?yüze"),
    ("A5", "sunulmayan", "RİSK", "online/uzaktan (yalnız olumsuz biçimde yazılır)", r"\b(online|çevrim ?içi|uzaktan|görüntülü)\b[^.]{0,40}(muayene|görüşme|takip|randevu|terapi)(?![^.]{0,60}(yapılmaz|yapılmamaktadır|yapmıyorum|yoktur|değil|mümkün değil))"),
    ("A6", "karşılaştırma", "RİSK", "yöntem/sonuç karşılaştırması", r"\bdaha (etkili|hızlı sonuç|güvenli|başarılı|iyi sonuç)\b"),
    ("A6", "karşılaştırma", "RİSK", "fiyat/maliyet", r"\b(fiyat\w*|ücret\w*|ucuz\w*|pahalı\w*|maliyet\w*|indirim\w*|kampanya\w*|uygun fiyat\w*)\b"),
    ("A7", "talep", "İHLAL", "doluluk/kapasite gerekçesi", r"\b(doluyuz|yoğunluk nedeniyle|kontenjan|bekleme listesi|yoğun talep)"),
    ("A7", "talep", "RİSK", "aciliyet pazarlaması", r"(geç kalmadan|vakit kaybetmeden|hemen)[^.]{0,30}(arayın|randevu alın|başvurun)(?![^.]{0,80}112)"),
    ("A7", "talep", "RİSK", "kanca/senaryo açılışı", r"\w+(sanız|seniz|yorsanız|yorseniz|ettiyseniz|diyseniz|tıysanız|tiyseniz)\b[^.]{0,200}\bolabilir"),
    ("A8", "kuruluş", "İHLAL", "klinik (tesis adı)", r"\bklini(ğim|ğimiz|ğimde|ğimizde|ğimize|ğimizin|ğe)\b|\bpoliklinik|\btıp merkez"),
    ("A8", "kuruluş", "RİSK", "'klinik' (sıfat mı, tesis mi?)", r"\bklinik\b(?!\s+(durum|deneyim|görüşme|uygulama|çalışma|tablo|değerlendirme|psikoloji|özellik|bulgu|karar|takip|pratik|belirti|seyir|araştırma))"),
    ("A8", "unvan", "İHLAL", "alt alan 'uzmanı' (yasal yan dal yok)", r"\b(duygudurum|bipolar|depresyon|yaşlılık|geriatri\w*|tms|okb|anksiyete|psikofarmakoloji|psikoterapi)\w*\s+(bozuklukları\s+)?uzmanı"),
    ("A9", "çoğul", "İHLAL", "çoğul şahıs", r"\b(biz|bize|bizim|bizi|bizden|ekibimiz\w*)\b"),
    ("A9", "çoğul", "RİSK", "-imiz (kurum ima?)", r"\b\w{3,}(ımız|imiz|umuz|ümüz)(da|de|a|e|ı|i|dan|den|ın|in)?\b"),
]

BUROKRATIK = ["bu bağlamda", "söz konusu", "bu doğrultuda", "bu çerçevede", "öte yandan", "bunun yanı sıra"]
BOS_KAPANIS = ["kritik bir rol", "önemli bir rol", "büyük önem taşı", "hayati öne", "vazgeçilmez", "göz ardı edilmemeli", "unutulmamalıdır"]
BOS_SIFAT = ["eşsiz", "benzersiz", "paha biçilmez", "kapsamlı", "bütüncül", "yenilikçi", "son teknoloji"]
VURGU = ["tam da", "gerçekten de", "aslında", "esasen", "nihayetinde", "kesinlikle", "bir bakıma", "gerçek anlamda"]
KALIP = ["bu sayfada", "özetledim", "özetliyorum", "ele alacağız", "değineceğiz", "inceleyeceğiz"]

IZLER = [  # (kod, açıklama, regex) — regex tr_lower metne uygulanır
    ("noktali_virgul", "noktalı virgül", r";"),
    ("karsitlik_virgul", "karşıtlık bağlacından önce virgül", r",\s*(ancak|ama|fakat|lakin)\b"),
    ("x_degil_y", "'X değil, Y' kalıbı", r"\b(sadece|yalnızca|salt)\b[^.;]{0,80}\bdeğil|\bdeğil(dir)?\s*[,;]\s|anlamına gelmez\s*[;,]|\w+(ın|in|un|ün) ötesinde"),
    ("burokratik", "bürokratik bağlaç", r"\b(" + "|".join(BUROKRATIK) + r")\b"),
    ("bos_kapanis", "boş önem/kapanış", "(" + "|".join(BOS_KAPANIS) + ")"),
    ("bos_sifat", "boş değerlendirici sıfat", r"\b(" + "|".join(BOS_SIFAT) + r")\b"),
    ("vurgu", "vurgu doldurucu", r"\b(" + "|".join(VURGU) + r")\b|^işte\b"),
    ("sudur", "'şudur:' kalıbı", r"\bşudur\s*:"),
    ("slash", "slash ayırıcı", r"[a-zçğıöşü]{2,}/[a-zçğıöşü]{2,}"),
    ("uzun_cizgi", "uzun çizgi", r"—| – "),
    ("kalip", "kalıp cümle ('bu sayfada… özetledim')", r"\b(" + "|".join(KALIP) + r")\b"),
]
MEKTEDIR = r"\w+(mektedir|maktadır|mektedirler|maktadırlar|mekteyim|maktayım|mekteyiz|maktayız)\b"

CEKINCELER = [  # mevzuat.md -> B
    ("çalışmalarda", r"çalışmalarda"),
    ("bildirilmiş", r"bildirilm[iı]ş"),
    ("incelenmiş", r"incelenm[iı]ş"),
    ("gösterilmiş", r"gösterilm[iı]ş"),
    ("kılavuz", r"kılavuz"),
    ("-ebilir/-abilir", r"\w+(ebil|abil)(ir|en|ecek|mekte|di|me|eceği|diği)\w*"),
    ("hastadan hastaya", r"hastadan hastaya"),
    ("uygun görülen", r"uygun görülen"),
    ("uygun hastalarda", r"uygun hastalar"),
    ("gerektiğinde", r"gerektiğinde"),
    ("genellikle", r"genellikle"),
    ("112 acil kalıbı", r"112 acil çağrı merkezi"),
]

TEKRAR_IZINLI = [  # bilinçli tekrarlar: mevzuat.md -> C
    "112 acil çağrı merkezi", "şu anda psikoterapi için yeni hasta kabul edemediğimden",
    "bu sayfa yalnızca genel bilgilendirme", "muayenehanede uygulanmamaktadır",
    "yalnızca yüz yüze hizmet", "psikoterapi için şu anda yeni hasta",
]

# ---------------------------------------------------------------- tarama

def tara(yol):
    icerik = open(yol, encoding="utf-8").read()
    satirlar, _ = satir_metinleri(icerik)
    tur = metin_turu(yol)
    mevzuat, izler = [], {k: [] for k, _, _ in IZLER}
    izler["mektedir_yigini"], izler["iki_nokta"], izler["retorik_soru"], izler["unlem"] = [], [], [], []
    kelime, cumleler, mektedir_toplam = 0, [], 0
    for no, t, st in satirlar:
        baslik = st == "baslik"
        lt = tr_lower(t)
        kelime += len(re.findall(r"\w+", t))
        for kod, kat, duzey, acik, desen in MEVZUAT:
            if kod == "A7" and "kanca" in acik and tur != "hasta":
                continue
            for m in re.finditer(desen, lt):
                mevzuat.append({"satir": no, "kod": kod, "kategori": kat, "duzey": duzey, "aciklama": acik,
                                "alinti": t[max(0, m.start() - 40): m.end() + 40]})
        for kod, acik, desen in IZLER:
            for m in re.finditer(desen, lt):
                if kod == "slash":  # "Çukurova/Adana" gibi özel ad çiftleri (adres biçimi) iz değildir
                    sol, sag = t[m.start():m.end()].split("/", 1)
                    if sol[:1].isupper() and sag[:1].isupper():
                        continue
                izler[kod].append({"satir": no, "alinti": t[max(0, m.start() - 45): m.end() + 45]})
        n = len(re.findall(MEKTEDIR, lt)); mektedir_toplam += n
        if n >= 3:
            izler["mektedir_yigini"].append({"satir": no, "alinti": f"{n} adet: " + t[:90]})
        govde = re.sub(r"(\s*\[\d+\])+\s*$", "", t).rstrip(":")
        iki = [m.start() for m in re.finditer(r":\s", govde) if m.start() > 45]
        if len(iki) >= 1:
            izler["iki_nokta"].append({"satir": no, "alinti": t[:100]})
        if st == "govde" and "?" in t:
            izler["retorik_soru"].append({"satir": no, "alinti": t[:100]})
        if "!" in t:
            izler["unlem"].append({"satir": no, "alinti": t[:100]})
        if st == "govde":
            for c in re.split(r"(?<=[.!?])\s+", t):
                w = len(re.findall(r"\w+", c))
                if w >= 3:
                    cumleler.append(w)
    say = {k: len(v) for k, v in izler.items()}
    yogunluk_haric = {"retorik_soru", "kalip"} if tur == "blog" else set()
    toplam_iz = sum(v for k, v in say.items() if k not in yogunluk_haric)
    return {
        "dosya": yol, "tur": tur, "kelime": kelime,
        "cumle_ort": round(statistics.mean(cumleler), 1) if cumleler else 0,
        "cumle_ss": round(statistics.pstdev(cumleler), 1) if len(cumleler) > 1 else 0,
        "mektedir_toplam": mektedir_toplam,
        "mevzuat": mevzuat, "izler": izler, "iz_sayilari": say,
        "yogunluk": round(toplam_iz * 100 / kelime, 2) if kelime else 0,
    }


def tekrarlar(yollar):
    esik = 2 if len(yollar) == 2 else 3
    cumle_dosya, acilis_dosya = {}, {}
    for yol in yollar:
        satirlar, _ = satir_metinleri(open(yol, encoding="utf-8").read())
        goruldu_c, goruldu_a = set(), set()
        for _, t, st in satirlar:
            if st != "govde":
                continue
            for c in re.split(r"(?<=[.!?])\s+", t):
                lc = tr_lower(c).strip()
                kelimeler = re.findall(r"\w+", lc)
                if len(kelimeler) < 6 or any(iz in lc for iz in TEKRAR_IZINLI):
                    continue
                if lc not in goruldu_c:
                    cumle_dosya.setdefault(lc, set()).add(os.path.basename(yol)); goruldu_c.add(lc)
                ac = " ".join(kelimeler[:4])
                if ac not in goruldu_a:
                    acilis_dosya.setdefault(ac, set()).add(os.path.basename(yol)); goruldu_a.add(ac)
    return {
        "esik": esik,
        "ayni_cumle": sorted([(c, sorted(d)) for c, d in cumle_dosya.items() if len(d) >= esik], key=lambda x: -len(x[1])),
        "ayni_acilis": sorted([(a, sorted(d)) for a, d in acilis_dosya.items() if len(d) >= esik], key=lambda x: -len(x[1])),
    }


# ---------------------------------------------------------------- yedek / karşılaştırma

def yedek_yolu(yol):
    goreli = os.path.relpath(os.path.abspath(yol)).replace(os.sep, "__")
    klasor = os.path.join(tempfile.gettempdir(), "metin-denetimi-yedek")
    os.makedirs(klasor, exist_ok=True)
    return os.path.join(klasor, goreli)


def degismezler(icerik):
    fm, govde, _ = ayir(icerik)
    satirlar, anahtarlar = satir_metinleri(icerik)
    duz = "\n".join(t for _, t, _ in satirlar)
    lduz = tr_lower(duz)
    return {
        "atif": Counter(re.findall(r"\[(\d+)\]", govde)),
        "sayi": Counter(re.findall(r"\d+(?:[.,]\d+)?", duz)),
        "link": Counter(re.findall(r'href="([^"]*)"', govde) + re.findall(r"\]\(([^)]+)\)", govde)),
        "etiket": Counter((a, b.lower()) for a, b in re.findall(r"<\s*(/?)([a-zA-Z0-9]+)", govde)),
        "liquid": Counter(re.findall(r"\{%.*?%\}|\{\{.*?\}\}", govde, re.S)),
        "baslik": [t for _, t, st in satirlar if st == "baslik"],
        "fm": {k: v for k, v in anahtarlar.items() if k not in DUZELTILEBILIR_FM},
        "kalin": [re.sub(r"\s+", " ", x).strip() for x in re.findall(r"<b>(.*?)</b>", govde, re.S)],
        "cekince": {ad: len(re.findall(d, lduz)) for ad, d in CEKINCELER},
    }


def karsilastir(yol):
    yp = yedek_yolu(yol)
    if not os.path.exists(yp):
        return {"durum": "YEDEK_YOK", "hatalar": [f"Yedek yok. Önce: denetle.py --yedekle {yol}"], "uyarilar": []}
    once_ic, simdi_ic = open(yp, encoding="utf-8").read(), open(yol, encoding="utf-8").read()
    a, b = degismezler(once_ic), degismezler(simdi_ic)
    hatalar, uyarilar = [], []
    for k, ad in (("atif", "atıf"), ("sayi", "sayı"), ("link", "link"), ("etiket", "HTML etiketi"), ("liquid", "Liquid")):
        if a[k] != b[k]:
            eksik, fazla = a[k] - b[k], b[k] - a[k]
            hatalar.append(f"{ad} değişti — eksilen: {dict(eksik) or '-'} · eklenen: {dict(fazla) or '-'}")
    if a["baslik"] != b["baslik"]:
        hatalar.append("başlık (H1–H6 / title / seo_title / acil_baslik) değişti: "
                       + "; ".join(f"'{x}'" for x in a["baslik"] if x not in b["baslik"]))
    for k in sorted(set(a["fm"]) | set(b["fm"])):
        if a["fm"].get(k) != b["fm"].get(k):
            hatalar.append(f"front matter '{k}' değişti (yalnız description ve lead düzeltilebilir)")
    for ad, n in a["cekince"].items():
        m = b["cekince"][ad]
        if m < n:
            hatalar.append(f"çekince azaldı: '{ad}' {n} → {m}")
    ta, tb = tara_icerik(once_ic, yol), tara_icerik(simdi_ic, yol)
    ka = Counter((x["kod"], x["duzey"]) for x in ta["mevzuat"])
    kb = Counter((x["kod"], x["duzey"]) for x in tb["mevzuat"])
    for (kod, duzey), n in kb.items():
        if n > ka.get((kod, duzey), 0):
            hatalar.append(f"yeni mevzuat bayrağı: {kod} {duzey} ({ka.get((kod, duzey), 0)} → {n})")
    for x in a["kalin"]:
        if x not in b["kalin"]:
            uyarilar.append(f"kalın vurgu değişti/kalktı: '{x[:80]}'")
    return {"durum": "BAŞARISIZ" if hatalar else "BAŞARILI", "hatalar": hatalar, "uyarilar": uyarilar,
            "yogunluk_once": ta["yogunluk"], "yogunluk_sonra": tb["yogunluk"]}


def tara_icerik(icerik, yol):
    gecici = yedek_yolu(yol) + ".tara"
    with open(gecici, "w", encoding="utf-8") as f:
        f.write(icerik)
    try:
        r = tara(gecici); r["dosya"] = yol; r["tur"] = metin_turu(yol)
        return r
    finally:
        os.remove(gecici)


# ---------------------------------------------------------------- çıktı

IZ_ADLARI = dict((k, a) for k, a, _ in IZLER)
IZ_ADLARI.update({"mektedir_yigini": "-mektedir yığını (satırda ≥3)", "iki_nokta": "cümle içi iki nokta",
                  "retorik_soru": "gövdede soru işareti", "unlem": "ünlem"})
TUR_ADI = {"hasta": "hasta bilgilendirme", "blog": "blog", "yasal": "yasal"}


def yaz_rapor(r):
    print(f"\n=== {r['dosya']}  ({TUR_ADI[r['tur']]}) ===")
    print(f"Kelime: {r['kelime']} · Cümle ort.: {r['cumle_ort']} kelime (ss {r['cumle_ss']}) · -mektedir toplam: {r['mektedir_toplam']}")
    print("\nMEVZUAT BAYRAKLARI (aday; bağlamında değerlendir, kendin düzeltme)")
    if not r["mevzuat"]:
        print("  yok")
    for x in sorted(r["mevzuat"], key=lambda x: (x["duzey"] != "İHLAL", x["satir"])):
        print(f"  [{x['duzey']}] {x['kod']} {x['aciklama']}  s.{x['satir']}: …{x['alinti']}…")
    print(f"\nYAZIM İZLERİ — {r['yogunluk']} / 100 kelime")
    bos = True
    for k, liste in r["izler"].items():
        if not liste:
            continue
        bos = False
        print(f"  {IZ_ADLARI[k]:<38} {len(liste):>3}   satır: {', '.join(str(x['satir']) for x in liste[:12])}")
        for x in liste[:2]:
            print(f"      s.{x['satir']}: …{x['alinti']}…")
    if bos:
        print("  yok")


def main(argv):
    js = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    if not argv:
        print(__doc__); return 2
    if argv[0] == "--yedekle":
        for yol in argv[1:]:
            with open(yedek_yolu(yol), "w", encoding="utf-8") as f:
                f.write(open(yol, encoding="utf-8").read())
            print(f"yedek alındı: {yol} → {yedek_yolu(yol)}")
        return 0
    if argv[0] == "--karsilastir":
        kod = 0
        for yol in argv[1:]:
            r = karsilastir(yol)
            if js:
                print(json.dumps(r, ensure_ascii=False, indent=1))
            else:
                print(f"\n=== karşılaştırma: {yol} → {r['durum']} ===")
                if "yogunluk_once" in r:
                    print(f"  yazım izi yoğunluğu: {r['yogunluk_once']} → {r['yogunluk_sonra']} / 100 kelime")
                for h in r["hatalar"]:
                    print(f"  HATA   {h}")
                for u in r["uyarilar"]:
                    print(f"  UYARI  {u}")
            if r["durum"] != "BAŞARILI":
                kod = 1
        return kod
    sonuclar = [tara(y) for y in argv]
    tekrar = tekrarlar(argv) if len(argv) > 1 else None
    if js:
        print(json.dumps({"dosyalar": sonuclar, "tekrar": tekrar}, ensure_ascii=False, indent=1, default=list))
        return 0
    for r in sonuclar:
        yaz_rapor(r)
    if tekrar:
        print(f"\n=== SAYFALAR ARASI TEKRAR (≥{tekrar['esik']} dosyada; bilinçli kalıplar hariç) ===")
        if not tekrar["ayni_cumle"] and not tekrar["ayni_acilis"]:
            print("  yok")
        for c, d in tekrar["ayni_cumle"][:15]:
            print(f"  aynı cümle ({len(d)}): \"{c[:90]}\"  → {', '.join(d)}")
        for a, d in tekrar["ayni_acilis"][:15]:
            print(f"  aynı açılış ({len(d)}): \"{a} …\"  → {', '.join(d)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
