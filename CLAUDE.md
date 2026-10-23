# ismailbucgun.com

Uzm. Dr. İsmail Buçgün'ün (Adana, psikiyatri uzmanı) muayenehane web sitesi.
Jekyll + GitHub Pages. Site dili Türkçe; kullanıcıyla Türkçe konuş.

---

## Teknik kısıtlar

**Bunlara uy, istisna yok:**

- **Build adımı yok.** GitHub Pages Jekyll'i kendi çalıştırır. `npm`, `yarn`, bundler,
  webpack, herhangi bir derleme aracı **eklenmez**.
- **Harici kütüphane yok.** JavaScript **vanilla** olacak. jQuery, React, GSAP, Tailwind yok.
- **Stil:** `_sass/` altında SCSS partials, `css/main.scss` içinden `@import` edilir.
  Sıralama önemlidir.
- **Şablon:** Liquid. Mantık layout ve include'larda; sayfalar mümkün olduğunca sade.
- Bu makinede **Node.js kurulu değil** ve yerel Jekyll build **çalışmıyor**
  (`Gemfile.lock` bundler 2.1.4 ister, sistem Ruby 2.6). Doğrulama push sonrası
  canlı site üzerinden `curl` ile yapılır.

## Mevzuat — en kritik kural

Site, Türkiye'deki **Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Faaliyetleri
Hakkında Yönetmelik** (12 Kasım 2025) kapsamındadır. İçerik yazarken veya
düzenlerken şunlar **yasaktır**:

- Üstünlük / benzersizlik iddiası ("ilk", "tek", "en iyi", "nadir", "lider")
- Hasta sayısı, başarı oranı, tedavi garantisi ("yüzlerce hasta", "%90 iyileşme")
- Kesinlik bildiren sonuç ifadeleri ("kesin geçer", "yan etkisi yoktur")
- Tesis övgüsü, konfor/otopark vb. üzerinden rekabet
- Sunulmayan bir hizmetin sunuluyormuş gibi anlatılması
- Karşılaştırmalı fiyat veya yöntem üstünlüğü

**Yerine:** "Çalışmalarda ... bildirilmiştir", "güncel kılavuzlarda tanımlı
protokoller", "hastadan hastaya değişir" gibi ölçülü, kaynağa dayalı dil.

Yeni tıbbi iddia eklemeden önce kullanıcıya sor. Mevcut metinleri "güçlendirmek"
için iddia ekleme.

### Kuruluş türü

Burası hukuken bir **muayenehane**. "Klinik", "poliklinik", "tıp merkezi"
kelimeleri **tesis adı olarak** kullanılamaz. "Poliklinik hizmeti" de yazılmaz — poliklinik
ayrı bir ruhsat türüdür; yerine "ayaktan muayene ve tedavi". Google Business Profile adı
"Uzm. Dr. İsmail Buçgün - Adana Psikiyatri - TMS" ve en önemli hasta kaynağı.

> **Türkçe arama tuzağı:** `grep -i "klinik"` yetmez — ünsüz yumuşaması nedeniyle
> "kliniğimde" eşleşmez. `klini[kğ]` kalıbını kullan.

---

## Dil rehberi

Ses sayfaya göre değil, **cümlenin işine göre** seçilir:

| Ne anlatılıyor | Ses |
|---|---|
| Muayenehanede ne yapıldığı (`/klinik`, `/randevu`, SSS cevapları, hastalık sayfalarında süreç) | Birinci tekil: "değerlendiriyorum", "yönlendiriyorum" |
| Tıbbi bilgi (tanım, belirti, tedavi seçenekleri) | Nesnel, edilgen, kaynaklı: "…ile seyreder", "kılavuzlarda … önerilir [2]" |
| Talimat (acil durum) | Hastaya "siz" ile doğrudan: "112'yi arayın" |
| Blog | Yazar sesi, serbest |

Tıbbi bilgi birinci şahısla yazılmaz — kanıt kişisel görüşe dönüşür, kaynak numarası
anlamını yitirir. Hiçbir yerde **"biz", "-imiz", "ekibimiz"** yok: tek hekimli muayenehane.

FDA kararları **"FDA onayı"** diye yazılır; "clearance / 510(k)" ayrımına girilmez (hasta için
kafa karıştırıcı, karar). Kaynak eklerken bu ifade değiştirilmez.

**Yazılmaz:**
- **Kanca / senaryo açılışı** ("…yapıyorsanız, … olabilir", "fark ettiyseniz…"): okuru
  kendine tanı koymaya iter, endişe üzerinden ilgi çeker. Hastalık sayfası ya doğrudan
  içindekiler kutusuyla ya da kısa, nesnel bir çerçeve cümlesiyle başlar.
- Dramatik cümle ("bu durumun bir adı var"); gövdede retorik soru ve ünlem.
- **Sayfalar arası kalıp tekrarı.** "Bu sayfada … özetledim" 8 sayfanın 8'indeydi —
  şablon metin izi. Lead tek, ciddi bir cümledir; kapsamı içindekiler kutusu gösterir.
- Gereksiz kalın yazı: yalnızca en önemli bir iki olgu.

---

## Muayenehane bilgileri (NAP — her yerde birebir aynı olmalı)

```
Uzm. Dr. İsmail Buçgün
Güzelyalı Mah. 81161. Sok. No:4/107
01170 Çukurova / Adana
+90 551 033 48 96
bilgi@ismailbucgun.com
Pazartesi–Cuma 09:00–18:00
```

Adres 2026'da Hurmalı/Seyhan'dan buraya taşındı. Eski adresi ("Central Plaza
Kat:2 D:23" veya "Kat:6 D:62") taşıyan bir yer görürsen bildir — eski kayıtlar
sıralama düşmesine yol açmıştı.

## Sunulan hizmetler

TMS ve derin TMS · psikiyatrik değerlendirme · farmakolojik tedavi ·
parlak ışık tedavisi · psikometrik ve nöropsikolojik testler ·
ilaç kan düzeyi takibi

**Konumlandırma:** İlk başvuruda herkese **genel psikiyatrik değerlendirme** yapılır
(tanısını bilmeyen hasta da gelebilir). Ağırlık **tedavi ve takipte** üç alandadır:
duygudurum bozuklukları, yaşlılık psikiyatrisi, beyin uyarım tedavileri. "Genel
psikiyatri ikinci planda" ya da "sadece bu alanlara bakıyorum" gibi yazılmaz. Alt alan
için "uzmanı" denmez (yasal yan dal unvanı yok); "ağırlıklı olarak ilgilendiğim
alanlar" + dayandığı eğitim.

**Ayrışma noktası: uzmanlık sonrası eğitimler** — FEBP + DUSEP (duygudurum, 2 yıl,
süpervizyonlu), RCPsych International Diploma (yaşlılık psikiyatrisi), NEI Master
Psychopharmacology. Fark **olgularla** gösterilir ("uzmanlık sonrası", "yapılandırılmış",
"süpervizyonlu"); "diğer uzmanlardan farklı olarak", "klasik uzmanlığın ötesinde" gibi
**karşılaştırma yazılmaz** — üstünlük iddiası sayılır. TMS için yapılandırılmış program
yok (yalnızca 2021 kongre kursu); "üç alanda da eğitim aldım" denmez.

## Sunulmayan — bu ayrım önemli

| Yöntem | Durum |
|---|---|
| EKT | Anestezi gerektirir, hastanede uygulanır; hasta yönlendirilir |
| tDCS | Uygulanmıyor. `/tdcs` yalnızca bilgilendirme sayfası |
| Esketamin | Uygun hastalarda **muayenehanede uygulanabilir**, henüz uygulanmadı. "Uygun görülen hastalarda muayenehanede uygulanabilen seçenekler arasındadır" yazılır; **"uyguluyorum"** ya da deneyim ima eden ifade **yazılmaz**. Türkiye'de ruhsatlı, reçeteyle temin ediliyor, **SGK geri ödemesi yok** (kullanıcı beyanı, 2026-10; değişirse sayfayı güncelle). Fiyat/maliyet yorumu yazılmaz. FDA onayı (2019) kaynakla yazılır |
| **Psikoterapi** (BDT, KİPT, destekleyici, psikanalitik) | Eğitimleri var ve yapıyor, ama **şu anda yeni hasta kabul edilemiyor.** İhtiyacı olan yeni hasta ilk muayenede veya takipte belirlenip o yöntemle çalışan uzmana **yönlendirilir**; psikiyatrik takip ve ilaç muayenehanede sürebilir |
| **Acil durumlar** (intihar riski, kendine/başkasına zarar, akut kriz, deliryum) | Muayenehane acil hizmet vermez. "Randevu alabileceğiniz durumlar" listelerine **yazılmaz**; her zaman "randevu beklemeden 112 Acil Çağrı Merkezi'ni arayın veya en yakın hastanenin acil servisine başvurun" kalıbıyla yönlendirilir |
| Çocuk ve ergen psikiyatrisi | Hizmet verilmiyor (18+) |
| **Online muayene ve takip** | **Hiç yapılmıyor** — ilk muayene, kontrol ve takip dahil yalnızca yüz yüze. "İlk muayene yüz yüze" diye **yazılmaz**: kronik hastalar kontrollerin online olabileceğini sanıp geliyordu |

Eğitim ve sertifika kayıtları (`_data/aldigiegitimler.yml`, schema `hasCredential`,
`knowsAbout`) **kalır** — eğitim beyanı serbesttir, hizmet beyanı değildir.

**Psikoterapi nasıl yazılır:** Çerçeve "yapmıyorum" değil, **"şu anda yeni hasta
kabul edemiyorum"**. Hastalık sayfalarında kılavuz bilgisi kalır ("OKB'de kılavuzlarda
önerilen yöntem BDT'dir"), ardından: "Şu anda psikoterapi için yeni hasta kabul
edemediğimden, … hastaları bu yöntemle çalışan bir uzmana yönlendiriyorum." Yalnız
"yönlendiriyorum" yazmak "bu hizmeti vermiyorum" diye okunur, yetmez. Sebebi
("doluyuz", "yoğunluk nedeniyle") **yazılmaz** — dolaylı hasta yoğunluğu beyanıdır.
Yönlendirme **düz bir sevk değildir**: hekim psikoterapi ihtiyacını ve hangi yöntemin
(BDT, KİPT, destekleyici) uygun olduğunu belirler, sonra o yöntemle çalışan uzmana
yönlendirir. Metin bunu yansıtır ("…uygun yöntemi belirleyip o yöntemle çalışan bir
uzmana yönlendiriyorum"). Psikoterapi eğitimleri bu eşleştirmenin dayanağıdır.
**Eğitimler eşit sıralanmaz:** destekleyici psikoterapi = süpervizyonlu, ~3,5 yıllık
yapılandırılmış eğitim + TPD Uygulayıcı sertifikası (uzmanlık **sırasında** alındı,
"uzmanlık sonrası" denmez); BDT ve KİPT = temel eğitim. Psikanalitik psikoterapi için
belgelenmiş eğitim yok, eğitim olarak yazılmaz.
Schema `availableService`'te psikoterapi yok: yeni hastaya açık olmayan hizmet
listelenmez.

---

## Dosya haritası

| Yol | İşlev |
|---|---|
| `_layouts/resume.html` | Ana sayfa |
| `_layouts/page.html` | İç sayfalar (`wide_layout: true` ile geniş yerleşim) |
| `_layouts/post.html` | Blog yazısı |
| `_includes/head.html` | Meta, OG, canonical, schema çağrıları, GA4; `seo_title` varsa `<title>` onu kullanır |
| `_includes/schema/hekim-klinik.html` | Ana sayfa JSON-LD (Physician + MedicalClinic) |
| `_includes/schema/tms.html` | `/tms` JSON-LD (FAQPage + MedicalProcedure) |
| Kökteki hastalık sayfaları | `depresyon.html` vb.; `layout: hastalik` |
| `_layouts/hastalik.html` | Hastalık sayfası şablonu: kaynaklar, uyarı (otomatik tarih), acil kutusu, CTA |
| `_includes/schema/hastalik.html` | `MedicalWebPage` + `MedicalCondition`; yazar ve gözden geçiren `/#hekim` |
| `_includes/iletisim-cta.html` | Ara / WhatsApp butonu; `baslik`, `metin`, `buton` parametreleri |
| `_data/categories.yml` | Blog kategori renkleri |
| `llms.txt` | Dil modelleri için site özeti — **hizmet değişince güncelle** |
| `.claude/skills/metin-denetimi/` | Metin denetimi skill'i: mevzuat + yapay zekâ yazım izleri; `scripts/denetle.py` tarama, yedek ve karşılaştırma |

### Hastalık sayfası düzeni

Hepsi **`layout: hastalik`** kullanır. Sayfa dosyasında yalnızca içindekiler ve 5 bölüm
bulunur. **Kaynaklar → yasal uyarı → acil durum kutusu → CTA** şablondan gelir, sırası
sabittir. Acil kutusu her sayfada var ve **CTA'nın hemen üstünde**: sayfa tek bir "ne
yapmalıyım" bloğuyla kapanır (acilse 112, değilse randevu).

**Front matter:** `title` (H1, kısa) · `seo_title` (`<title>`; kalıp **"[X] Tedavisi"**, sonek
dahil ≤55 karakter — uzarsa Google sondan keser ve "Adana" kaybolur; şemsiye sayfada yazılmaz, H1 kullanılır) · `description` (≤155, tırnaklı) · `lead` (tek cümle) ·
`kosul` / `kosul_diger` (schema `MedicalCondition`) · `refs` (kaynak listesi) · `acil` /
`acil_baslik` (yoksa genel metin) · `last_modified_at` (uyarıdaki tarih ve schema
`lastReviewed` buradan gelir; elle tarih yazılmaz).

**Bölümler — her sayfada aynı sıra ve aynı kalıp:**
1. **[X] nedir?** — nesnel, kaynaklı. Blog yazısı varsa kısa tutulur, yazıya link verilir.
2. **[X]'in belirtileri nelerdir?** — liste.
3. **[X]'te değerlendirme nasıl yapılır?** — ilk cümle soruyu genel olarak, nesnel dille
   cevaplar; **hemen ardından, aynı paragrafta** yerel hizmet cümlesi gelir ("Adana Çukurova'daki
   muayenehanemde…"), devamı birinci tekil (pilotta kullanıcı kararı).
4. **[X] nasıl tedavi edilir?** — alt başlıklar sabit sırada (pilotta kullanıcı kararı):
   ilaç → TMS / derin TMS (varsa, `/tms` linki) → diğer ilaç seçenekleri (esketamin gibi,
   varsa) → psikoterapi (kılavuz + yönlendirme) → muayenehanede uygulanmayanlar (EKT, notuyla)
   → diğer (parlak ışık vb.).
5. **[X] tedavisi ne kadar sürer, takip nasıl yapılır?**

Neden böyle (arama ve yapay zekâ): yapay zekâ sistemleri sayfayı pasaj pasaj alıntılar.
Başlıklarda hastalık adı geçer ki pasaj başlığıyla alıntılandığında bağlam kalsın. Her
bölümün **ilk cümlesi soruyu tek başına cevaplar** ("Bu yöntem…" diye başlamaz). Yerel
cümle olmadan "Adana'da X için kime gidilir?" sorusunda sayfa kaynak gösterilemez. Metin
içinde en az 2 ilgili sayfaya link. "Sık sorulanlar" bölümü **eklenmez** (karar).

**Kapsam:** Sayfa yalnız muayenehanede yapılanı değil, **kılavuzdaki seçenekleri** anlatır.
Muayenehanede uygulanmayan bir seçenek (EKT gibi) genel bilimsel bilgi olarak, kaynağıyla
yazılır; hemen yanında "muayenehanede uygulanmamaktadır, … yönlendirilir" notu bulunur.
Seçeneği hiç anmamak sayfayı eksik bırakır; notsuz anmak sunuluyormuş gibi okunur.

**Uzunluk: 650–950 kelime** (bağlayıcı) — bölüm aralıkları yol göstericidir: nedir 80–120 ·
belirtiler 80–150 · değerlendirme 120–180 · tedavi 200–300 · takip 80–150. Tedavinin asıl konu
olduğu sayfada (dirençli depresyon) tedavi bölümü uzayabilir. Büyüme eksik konudan gelir,
dolgudan değil.

Punto kademesi: gövde 1.18rem → TOC 0.88rem → kaynaklar 0.8rem → uyarı 0.75rem. TOC ve
kaynak kutusu blogdaki `.post-toc` / `.post-refs` ile aynı dili konuşur; uyarıya kutu verilmez.

### Ölçüm (GA4)

`head.html` telefon ve WhatsApp tıklamalarını `phone_click` / `whatsapp_click` olayı ve
`link_location` parametresiyle gönderir (`hero`, `cta`, `iletisim_karti`, `menu`, `footer`,
`icerik`). GA4'te ikisi **anahtar etkinlik**, `link_location` özel boyut ("Buton konumu").
Uçtan uca 2026-10-20'de doğrulandı. `gtag` kuyruğu sayfa başında tanımlı (erken tıklama
kaybolmasın), ağ yüklemesi gecikmeli. Yeni bir buton kapsayıcısı eklenirse `konum`
eşlemesine ekle.

**Referans dönemi: 2026-10-20 → 2026-11-10.** Bu tarihe kadar dönüşümü etkileyecek büyük
değişiklik (`/tms` başlığı, ana sayfanın sadeleşmesi) yapılmaz; önce mevcut durum ölçülür.
Veri çok azsa dönem uzatılır.

### Senkron tutulması gerekenler

- **Sayfa metni ↔ schema.** `/tms` SSS metinleri `_includes/schema/tms.html`
  içinde birebir tekrarlanır. Birini değiştirince diğerini de değiştir.
- **Hizmet listesi ↔ üç yer:** `klinik.html`, schema `availableService`, `llms.txt`.
  **Bilinçli istisna — esketamin:** hizmet listesinde (`/klinik`, schema) **yer almaz**;
  yalnızca dirençli depresyon sayfasında ve `llms.txt`'de "uygulanabilir" olarak geçer.
  Tutarsızlık sanıp listeye ekleme.
- Blog yazılarının URL'leri `permalink: /:title` ile **kilitli**. Global ayar
  `/blog/:title` ama mevcut 6 yazının adresi değişmemeli (trafik var).
- **`last_modified_at`** — bir sayfanın veya yazının içeriğini değiştirdiğinde
  front matter'daki bu tarihi de güncelle (`YYYY-AA-GG`). `sitemap.xml` ve
  `_layouts/post.html` (schema `dateModified`) bu alanı okur. Güncellemezsen
  Google değişikliği fark etmez. Sadece dizgi/stil düzeltmesiyse dokunma —
  içerik değişmediyse tarih de değişmemeli.

---

## Bilinen tuzaklar

- **YAML front matter'da tırnaksız değer içinde `: ` olamaz.** Olursa Jekyll
  sessizce pes eder: `---` bloğunu siler ama layout ve permalink uygulanmaz,
  sayfa çıplak HTML olarak servis edilir. İki KVKK sayfası aylarca böyle bozuktu.
  Açıklamalarda iki nokta varsa değeri tırnağa al.
- **zsh** tırnaksız değişkenleri kelimelere bölmez (bash'ten farklı). Dosya
  listeleri için `find … -print0 | xargs -0` kullan.
- macOS'ta `timeout` yok; BSD `grep` seçenekleri yoldan **önce** ister; `grep -Z`
  güvenilmez.
- **`.content-section` içindeki `h2`, `h3` ve `p` global olarak `!important` ile
  stilleniyor** (`_resume.scss`, "MODERN İÇERİK" bloğu: `h3` 1.4rem indigo + 2.5rem üst
  boşluk, `p` 1.18rem + 1.95 satır aralığı). Sayfa içinde küçük bir bileşen (kutu başlığı,
  ince yazı) yaparken `font-size`, `color`, `margin`, `line-height`'a **`!important`
  vermezsen kuralın sessizce ezilir.** Kaynak kutusu ve yasal uyarı bu yüzden ilk
  yayında büyük göründü. Alternatif: başlık için `h3` yerine `strong` kullan (TOC böyle).
  Global `!important`'ı kaldırma — 13 sayfadaki tüm başlık ve paragrafları yönetiyor.
- `noindex` için front matter'a `noindex: true` yaz (`head.html` bunu okur).
  `robots.txt`'ye `Disallow` **ekleme** — engellenen sayfa taranamaz, dolayısıyla
  `noindex` görülmez.

---

## Kalan işler

**Site içi**
1. **Hastalık sayfaları — pilot açıldı, kalan 7 yeniden yazılacak (`noindex`).** Sıradaki iş:
   içeriği 5 bölümlük iskelete göre birer birer yeniden yazmak; örnek olarak açılmış pilot
   `tedaviye-direncli-depresyon` esas alınır. Her biri kullanıcı onayıyla açılır: `noindex` + `sitemap:` satırlarını
   sil, `last_modified_at`'ı güncelle. Ana sayfa kutuları, blog geri linkleri ve `llms.txt`
   kayıtları kalır. Yaşlılık sayfasındaki deliryum kutusu konuya özgü, içerikte kalır.
   Her sayfada `metin-denetimi`'nin A10 (atıfsız otorite) bulgularına atıf eklenir; şu an
   3 cümle var (OKB 1, bipolar 1, şizofreni 1).

   | Sayfa | İskelete göre yazıldı | Açıldı |
   |---|---|---|
   | `tedaviye-direncli-depresyon` (pilot) | evet | evet (2026-10-23) |
   | `depresyon` | taslak, kullanıcı okuması bekliyor | hayır |
   | `okb` · `bipolar-bozukluk` · `anksiyete-bozukluklari` | hayır | hayır |
   | `eriskin-dehb` · `yaslilik-psikiyatrisi` · `sizofreni` | hayır | hayır |

2. İç linkleme — şu sayfalardan hiç iç link çıkmıyor: `tms`, `randevu`,
   `iletisim`, `tdcs`, `blog`, `eriskin-dehb`, `yaslilik-psikiyatrisi`, `sizofreni`.
   `/tms` en çok gösterim alan sayfa (62.437) ve oradan hiçbir yere gidilemiyor;
   öncelik orada.
3. **`/tms` kaynak listesi.** Sayfada 10 atıfsız iddia var (FDA onay yılları, endikasyonlar,
   "literatürde çalışmalar bulunmaktadır") ve **hiç kaynak listesi yok**; sitenin en çok
   gösterim alan sayfası. FDA yılları için Cohen SL ve ark. *Brain Stimul.* 2022;15(1):73-75
   (TMS FDA kronolojisi, "approved" diyor; pilotta kullanıldı); ilaç onaylarında prospektüs.
   Gerçek kaynaklar (FDA kararları, temel çalışmalar) eklenecek:
   atıf numaraları metne, `.page-refs` kutusu sayfa sonuna (`/tms` `tms-content` kullandığı
   için stil hazır; hastalık şablonunda olmadığından kutu elle eklenir). SSS metni değişirse
   `_includes/schema/tms.html` ile senkron. Başlık ve metin değişmediği için referans
   dönemini beklemesi gerekmez. Aynı sorun `/tdcs`'te (6, kaynak listesi yok; yalnız tek bir
   satır içi "Kaynak:" notu) ve `/klinik`'te (1, FDA ifadesi) de var.

> Hastalık sayfaları muayenehanedeki **değerlendirme ve tedavi sürecini** anlatır,
> hastalığın "nedir"ini **blog yazıları** anlatır. Aynı metni iki yere yazma;
> birbirine link ver. Ana sayfa kutuları, `llms.txt` ve blog geri linkleri bağlandı.

**Ölçüm**
4. `/tms` başlık ve açıklama CTR yazımı — 62.437 gösterim, %0,73 tıklama.
   Ölçüm kuruldu; referans dönemi bittikten sonra (2026-11-10) yapılır.

**Bekleyen**
5. `/parlakisik` içeriği yazılacak. Şu an `noindex` + sitemap dışı, içeriği
   boşaltıldı. Tedavi **uygulanıyor**, eksik olan sadece sayfa.
6. **`/hakkimda` — taslak, yayında değil.** Amaç: ana sayfayı özgeçmiş görünümünden çıkarmak.
   - Taslakta: `noindex` + sitemap dışı, **hiçbir yerden link yok** (menü, footer, `llms.txt`,
     404, blog). Adresi bilen açabilir ve repo herkese açık; taslağa gizli bilgi konmaz.
   - Taşınacak 4 bölüm: Yeterlilik ve Üyelikler, Akademik Eğitim, Çalıştığım Kurumlar,
     Aldığım Eğitimler. Veri zaten `_data/*.yml`'de; sayfa aynı dosyaları okur, içerik
     kopyalanmaz. Bölüm şablonları `_includes/ozgecmis/`'e alınır. Canlı ana sayfaya
     yayına kadar **dokunulmaz**.
   - Yalnız CV dökümü olmaz: başta birinci şahısla kısa anlatım (neden bu alanlar, nasıl
     çalışıyorum). Ham malzeme: git geçmişindeki `_data/meslekiilgialanlari.yml`.
   - **Sıra:** ölçüm kuruldu; yayın referans döneminden sonra (2026-11-10) — ana sayfa
     "adana psikiyatri"de üst sırada, değişikliğin etkisi ölçülebilmeli.
   - Yayın listesi: noindex/sitemap satırlarını sil, `last_modified_at` ekle · ana sayfadan
     4 bölümü kaldır, yerine kısa yeterlilik özeti (FEBP + uzmanlık sonrası eğitimler) ve
     `/hakkimda` linki · menü ve footer linki · blog yazar kutusundan link · `llms.txt` ·
     schema: `/hakkimda`'ya `ProfilePage` (`mainEntity` → mevcut `/#hekim`; ikinci kişi düğümü
     açılmaz, Physician ana sayfada kalır), `hasCredential`'a DUSEP, RCPsych, NEI · Search
     Console'dan dizine ekleme isteği · 2–3 hafta sıralama takibi.

**Site dışı**
7. İyi Psikolog ve Türkiye Psikiyatristleri'ne adres güncelleme maili gönderildi,
   takip edilecek. Doktorum360 için KVKK 11. madde talebi opsiyonel.
   (DoktorTakvimi ve Doktorsitesi düzeltildi.)

**En son — içerik bittikten sonra**
8. Yeniden tasarım ("yapay zeka yapımı" görünümden çıkarmak). Yöntem kararlaştırıldı:
   ayrı public repo `tasarim`, önizleme `ismailbucgun.com/tasarim/` adresinde
   (ana site özel domain kullandığı için GitHub proje repolarını onun altına koyar).
   - Başlarken `master`'a `tasarim-oncesi` tag'i at — geri dönüş noktası.
   - Önizleme reposunda `CNAME`'i sil (iki repo aynı domaini talep etmesin),
     `baseurl: /tasarim`, `_config.yml` `defaults` ile tüm sayfalara `noindex`.
   - **Tuzak:** sitedeki kök-mutlak yollar (`/css/main.css` vb., ~87 adet, 24 dosya)
     `relative_url`'e çevrilmeli. Çevrilmezse önizleme canlı sitenin CSS'ini yükler
     ve hata vermeden **eski tasarımı** gösterir. Canlıda çıktı aynı kalır.
   - Birleştirirken `_config.yml` ve `CNAME` ana sitedeki haliyle kalır.
   - Menü etiketi ve `/klinik` sayfa başlığı "Klinik" → **"Hizmetler"** olacak. Gerekçe:
     menüdeki "Klinik" tesis adı gibi okunuyor (mevzuat). URL `/klinik` **değişmez**
     (trafik ve linkler var). Değişecek yerler: `_includes/navigation-lib/links.html`,
     `klinik.html` `title`; tutarlılık için `404.html` ve `llms.txt`'deki "Muayenehane" etiketi.
   - `design-taste-frontend` skill'i kullanılacak; npm/React/GSAP kısımları hariç,
     Jekyll + SCSS + vanilla JS'e uyarlanarak. Önce mevcut tasarım denetlenir.

---

## Çalışma şekli

- Değişiklikten önce dosyayı oku; varsayımla düzenleme yapma.
- **Site metni yazıldıktan ya da düzenlendikten sonra `metin-denetimi` skill'ini çalıştır.**
  Önce denetim raporu; düzeltme yalnız onayla, ardından `denetle.py --karsilastir` BAŞARILI
  dönmeden iş bitmiş sayılmaz. Mevzuat bulguları raporlanır, kendiliğinden düzeltilmez.
- Toplu değişiklikten sonra doğrula (grep sayımı, JSON geçerliliği, link kontrolü).
- Commit ve push kullanıcıya aittir — istemeden commit etme.
- Push sonrası canlı doğrulama `curl` ile yapılır.

---

## Bu dosyanın bakımı

Bu dosya **şu an neyin doğru olduğunu** anlatır, ne olduğunu değil. Değişiklik
geçmişi `git log`'da zaten duruyor; buraya ikinci kez yazma.

**Kullanıcı ayrıca söylemese bile güncelle:**

- Bir iş bitti → "Kalan işler"den çıkar
- Yeni iş çıktı → listeye ekle
- Kalıcı bir karar verildi (hizmet kapsamı, mevzuat yorumu, teknik kısıt,
  URL yapısı) → ilgili bölüme işle, gerekçesiyle
- Tekrar edebilecek bir tuzak keşfedildi → "Bilinen tuzaklar"a ekle
- NAP bilgisi, hizmet listesi veya dosya yapısı değişti → ilgili bölümü düzelt

**Buraya yazma:**

- Tek tek dosya değişiklikleri ("şu satırı güncelledim")
- Yapılan işin anlatımı veya oturum özeti
- Geçici durumlar, tek seferlik notlar

Güncellemeyi işin sonunda, tek seferde yap ve kullanıcıya bir satırla bildir.
Dosya uzadıkça değerini kaybeder; yeni bilgi eklerken eskiyen satırı sil.
