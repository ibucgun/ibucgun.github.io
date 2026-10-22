---
name: metin-denetimi
description: ismailbucgun.com (psikiyatri muayenehanesi) sitesindeki Türkçe metni denetler ve onaylı düzeltir — önce Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Faaliyetleri Hakkında Yönetmelik ve sitenin CLAUDE.md kuralları, sonra yapay zekâ yazım izleri (noktalı virgül, "X değil Y", -mektedir yığını, boş kapanış, kanca açılış). Bu sitede bir hastalık sayfası, /klinik, SSS, /tms, randevu/iletişim metni ya da blog yazısı yazıldığında veya düzenlendiğinde son adım olarak MUTLAKA kullan; kullanıcı "yapay zeka yazmış gibi görünmesin", "AI kokusunu at", "humanize et", "metni doğallaştır", "denetle", "mevzuata uygun mu", "gözden geçir" dediğinde de kullan. Yalnız rapor veren denetim modu ve dokunulmazları betikle doğrulanan düzeltme modu vardır.
---

# Metin denetimi — ismailbucgun.com

Bu sitedeki metin, bir psikiyatri muayenehanesinin hastaya dönük metnidir. İki şeye
karşı denetlenir ve **sıra önemlidir**:

1. **Mevzuat ve site kuralları** — yanlış bir cümle yasal risk ve hasta güveni demektir
2. **Yapay zekâ yazım izleri** — metnin şablondan çıkmış gibi okunması

Bu ikisi çatışabilir. Yapay zekâ izini temizlemenin en kolay yolu çoğu zaman çekinceyi
atmaktır: "Çalışmalarda etkili olduğu bildirilmiştir" yerine "Etkilidir" daha akıcıdır,
ama yönetmeliğin yasakladığı kesinlik iddiasına dönüşür. **Böyle bir durumda iz kalır,
çekince kalır.** Akıcılık için yasal güvenceden asla vazgeçilmez.

## Öncelik sırası (çatışmada üstteki kazanır)

1. **Yönetmelik** → `references/mevzuat.md`
2. **Sitenin gerçekleri ve dil rehberi** → repodaki `CLAUDE.md`. Her çalıştırmada şu
   bölümleri oku: *Mevzuat*, *Dil rehberi*, *Sunulan hizmetler* (konumlandırma, ayrışma
   noktası), *Sunulmayan*, *Hastalık sayfası düzeni*. Bu skill onların kopyasını tutmaz,
   çünkü değişiyorlar: esketamin, psikoterapi kapasitesi, hizmet listesi zamanla değişir.
   Eski bir kopyaya göre denetlemek, doğru metni "düzeltip" bozmak demektir.
3. **Yapay zekâ izleri** → `references/sinyaller.md`

## Modlar

**Denetim (varsayılan).** Dosyayı değiştirme. Rapor ver. Kullanıcı yalnızca "denetle",
"kontrol et", "mevzuata uygun mu" dediğinde ve emin olmadığında bu moddasın.

**Düzeltme.** Kullanıcı "düzelt", "AI kokusunu at", "humanize et" dediğinde ya da
denetim raporundan sonra onay verdiğinde. Mevzuat bulgularını **kendin düzeltme**,
yalnızca raporla: bunlar hukuki karar gerektirir ve karar hekimindir. Yazım izlerini
düzelt, sonra karşılaştırma betiğiyle dokunulmazların yerinde olduğunu kanıtla.

## Metin türleri

Dosya yoluna göre belirle, kullanıcıya sorma:

| Tür | Dosyalar | Davranış |
|---|---|---|
| **Hasta bilgilendirme** | kökteki hastalık sayfaları, `klinik`, `tms`, `tdcs`, `parlakisik`, `sikca-sorulan-sorular`, `randevu`, `iletisim`, `404`, `_layouts/`, `_includes/` içindeki metin | Tam denetim. Tıbbi bilgi nesnel ve edilgen kalır, süreç birinci tekil, "siz" yalnız talimatta. Retorik soru, öz-düzeltme ("daha doğrusu"), birinci çoğul, devrik cümle **eklenmez** |
| **Blog** | `_posts/*.md` | Yazar sesi; daha serbest ritim. Mevzuat aynı sıkılıkta. Ses için yazarın kendi 2022 yazılarındaki cümle yapısına bak, kendi zevkine değil |
| **Yasal** | `aydinlatma-metni`, `acik-riza`, `cerez-politikasi` | Yalnız denetim. Düzeltme yalnız açık istekle ve yalnız noktalama düzeyinde; hukuki anlam değişmez |

Front matter'daki görünür metinler de metindir: `description`, `lead` denetlenir ve
düzeltilebilir. `title`, `seo_title`, `acil`, `acil_baslik`, `refs` denetlenir ama
**düzeltmede değiştirilmez**: başlıklar SEO kararıdır, acil metni kalıptır, kaynaklar bibliyografyadır.

## Dokunulmazlar (düzeltmede değişmez)

Bunların her biri bir sebepten orada; betik hepsini kontrol eder:

- **Atıflar** (`<sup>[n]</sup>`), **sayılar, yıllar, yüzdeler, dozlar, seans sayıları** — tıbbi olgu.
  Atıf **silinmez**. Atıf **eklemek** serbest ama yalnızca gerçek bir kaynakla, kullanıcı onayıyla;
  asla uydurulmaz (`references/mevzuat.md` → A10)
- **Linkler** (`href`), **HTML etiketleri**, **Liquid** (`{% %}`, `{{ }}`) — sayfa yapısı
- **H2 ve H3 başlıkları** — hastalık sayfası iskeleti sabittir; değişiklik gerekiyorsa öner
- **Çekinceli kalıplar** (`references/mevzuat.md` → B) — yasal güvence
- **Muayenehane notları ve acil kalıbı** (`references/mevzuat.md` → C) — onaylanmış kalıplar
- **`<b>` ile vurgulanmış uyarı cümleleri** — bilinçli vurgu; örneğin "Ancak psikoterapi
  için şu anda yeni hasta kabul edemiyorum." Bağlaçla başlasa da birleştirilmez

## Akış

### 1. Hazırlık
`CLAUDE.md`'nin yukarıdaki bölümlerini oku. Düzeltme yapılacaksa **önce yedek al**:

```bash
python3 .claude/skills/metin-denetimi/scripts/denetle.py --yedekle <dosya>
```

### 2. Betik taraması
```bash
python3 .claude/skills/metin-denetimi/scripts/denetle.py <dosya> [<dosya> ...]
```

Betik iki listeyi satır numarasıyla verir: **mevzuat bayrakları** ve **yazım izleri**,
ayrıca 100 kelimede iz yoğunluğu. Birden fazla dosya verilirse sayfalar arası tekrar eden
cümleleri de bulur ("Bu sayfada … özetledim" sekiz sayfada aynıydı).

Betik bayrakları **aday**dır, hüküm değildir. "nadir" kelimesi "literatürde nadir
bildirilen bir yan etki" cümlesinde tıbbi sıklıktır, üstünlük iddiası değil. Her bayrağı
bağlamında oku ve karar ver.

### 3. Okuyarak denetim
Betiğin göremediklerine bak; bunlar anlam düzeyinde:

- **Atıfsız otorite (A10)** — betik bulur; her biri için kaynak listesinde destekleyen kaynak
  var mı bak, varsa numarasını öner, yoksa "kaynak gerekiyor" de. Kaynak listesi hiç olmayan
  sayfalarda (betik belirtir) bunu ayrıca raporla
- **Sunulmayan hizmet ima ediliyor mu?** `CLAUDE.md` → *Sunulmayan* tablosuyla karşılaştır:
  EKT, tDCS, psikoterapi (yeni hasta), çocuk-ergen, online, acil
- **Konumlandırma doğru mu?** Alt alan için "uzmanı" yok; eğitimler olgularla; karşılaştırma yok
- **Psikoterapi çerçevesi** "yapmıyorum" değil "şu anda yeni hasta kabul edemiyorum" mu?
  Yönlendirme "uygun yöntemi belirleyip" diye mi anlatılıyor?
- **Ölçüsüz kesinlik** — sonuç vaadi, "her hastada", "mutlaka iyileşir"
- **Ses doğru mu?** Tıbbi bilgi birinci şahısla mı yazılmış?
- **Her bölümün ilk cümlesi** soruyu tek başına cevaplıyor mu? (hastalık sayfaları)
- **Somut olmayan genelleme**, boş kapanış, kalıp tekrarı

### 4. Düzeltme (yalnız düzeltme modunda)
`references/sinyaller.md`'deki onarımları uygula. Her değişiklikte kendine sor: bu cümle
bir olgu, bir çekince, bir atıf ya da bir uyarı kaybetti mi? Kaybettiyse geri al.

Yarım cümle üretme. Bilgi ekleme: bir cümle somut bir örnek istiyor ama metinde yoksa,
uydurma, kullanıcıya sor. Yapıyı koru: liste liste, başlık başlık kalır.

### 5. Karşılaştırma (düzeltmeden sonra zorunlu)
```bash
python3 .claude/skills/metin-denetimi/scripts/denetle.py --karsilastir <dosya>
```

Yedekle şimdiki hali karşılaştırır: atıflar (eksilme hata, ekleme uyarı), sayılar, linkler, HTML etiketleri, Liquid,
başlıklar, front matter, çekince sayıları, acil kalıbı ve mevzuat bayrakları. **BAŞARISIZ**
dönerse düzeltmeyi bitmiş sayma: gösterdiği farkları geri al ya da kullanıcıya gerekçesiyle
sun. Çekince sayısındaki bir düşüş gerçekten gerekliyse (örneğin aynı cümlenin tekrarı
silindiyse) bunu açıkça söyle ve onay iste.

## Rapor biçimi

Her çalıştırmada bu yapıyı kullan:

```
# Metin denetimi: <dosya>
Tür: <hasta bilgilendirme | blog | yasal> · Mod: <denetim | düzeltme>

## 1. Mevzuat ve site kuralları
İHLAL  — satır N: "<alıntı>" → neden, öneri (karar hekimin)
RİSK   — satır N: "<alıntı>" → bağlama göre neden riskli
TEMİZ  — bulgu yoksa bunu açıkça yaz

## 2. Yapay zekâ izleri
Yoğunluk: X iz / 100 kelime   (düzeltmede: önce X → sonra Y)
| İz | Adet | Örnek (satır) |

## 3. Değişiklikler            (yalnız düzeltme modunda)
Önce → sonra, en önemlileri; hepsini listeleme

## 4. Bilerek dokunmadıklarım
Çekinceler, onaylı kalıplar, bilinçli vurgular, kullanıcı kararı bekleyenler

## 5. Karşılaştırma betiği       (yalnız düzeltme modunda)
BAŞARILI / BAŞARISIZ + farklar
```

Bulgu yoksa uzatma: "Mevzuat: temiz. Yazım izi: 0,3/100 kelime, düzeltme gerekmiyor."
Temiz bir metni temiz diye tanımak da raporun işidir.

## Sınırlar

- Amaç yapay zekâ dedektörlerini atlatmak değil; hastanın doğal, somut ve güvenilir bir
  metin okumasıdır. Google da içeriği yapay zekâ yazdı diye değil, genel ve özgül olmadığı
  için cezalandırır.
- Tıbbi doğruluğu bu skill denetlemez; kaynak-cümle uyumu ve yeni tıbbi iddia onayı
  `CLAUDE.md` kurallarıyla yürür. Ama düzeltme sırasında anlamı değişen bir tıbbi cümle
  fark edersen raporla.
- Commit ve push kullanıcıya aittir.
