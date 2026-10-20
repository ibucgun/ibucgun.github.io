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
| Esketamin | Muayenehanede uygulanabilir ama henüz uygulanmadı. Sitede ne "uygulanır" ne "uygulanmaz" yazılır |
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
| `_includes/head.html` | Meta, OG, canonical, schema çağrıları, GA4 |
| `_includes/schema/hekim-klinik.html` | Ana sayfa JSON-LD (Physician + MedicalClinic) |
| `_includes/schema/tms.html` | `/tms` JSON-LD (FAQPage + MedicalProcedure) |
| Kökteki hastalık sayfaları | `depresyon.html` vb.; `tms-content` + `tms-toc` yapısı |
| `_includes/iletisim-cta.html` | Ara / WhatsApp butonu; `baslik`, `metin`, `buton` parametreleri |
| `_data/categories.yml` | Blog kategori renkleri |
| `llms.txt` | Dil modelleri için site özeti — **hizmet değişince güncelle** |

### Hastalık sayfası düzeni

Sırası sabittir; yeni sayfa da aynı düzende olmalı:

1. Giriş paragrafı → `<nav class="tms-toc">` → numaralı `<h2>` bölümleri
2. `<div class="page-refs" id="kaynaklar">` — `<h3>Kaynaklar</h3>` + `<ol>`
3. `<p class="page-note">` — yasal uyarı, **kutunun dışında**, kutusuz
4. `{% include iletisim-cta.html %}` — **en sonda**

Punto kademeli küçülür, böylece hiyerarşi gözle okunur:
gövde 1.18rem → TOC 0.88rem → kaynaklar 0.8rem → uyarı 0.75rem.
TOC ve kaynak kutuları blogdaki `.post-toc` / `.post-refs` ile aynı dili
konuşur (yuvarlak köşe, büyük harfli küçük başlık). Uyarıya kutu verme —
üçüncü bir kutu sayfayı ağırlaştırır; ince yazı zaten ince yazı gibi okunur.
CTA en sonda durur ki sayfa eylemle kapansın.

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
1. **8 hastalık sayfası `noindex` + sitemap dışı.** İçerikleri hazır ve yayında,
   ama arama sonuçlarına kapalı. Her sayfa gözden geçirilip onaylandıkça front
   matter'daki `noindex: true` ve `sitemap:` satırları **tek tek** silinerek açılır.
   Ana sayfa kutuları, blog geri linkleri ve `llms.txt` kayıtları duruyor —
   kaldırma, sayfalar çalışıyor, sadece indekslenmiyor.

   | Sayfa | Açıldı mı |
   |---|---|
   | `depresyon` · `tedaviye-direncli-depresyon` · `okb` · `bipolar-bozukluk` | hayır |
   | `anksiyete-bozukluklari` · `eriskin-dehb` · `yaslilik-psikiyatrisi` · `sizofreni` | hayır |

2. İç linkleme — şu sayfalardan hiç iç link çıkmıyor: `tms`, `randevu`,
   `iletisim`, `tdcs`, `blog`, `eriskin-dehb`, `yaslilik-psikiyatrisi`, `sizofreni`.
   `/tms` en çok gösterim alan sayfa (62.437) ve oradan hiçbir yere gidilemiyor;
   öncelik orada.

> Hastalık sayfaları muayenehanedeki **değerlendirme ve tedavi sürecini** anlatır,
> hastalığın "nedir"ini **blog yazıları** anlatır. Aynı metni iki yere yazma;
> birbirine link ver. Ana sayfa kutuları, `llms.txt` ve blog geri linkleri bağlandı.

**Ölçüm**
3. `/tms` başlık ve açıklama CTR yazımı — 62.437 gösterim, %0,73 tıklama.
   Ölçüm kuruldu; referans dönemi bittikten sonra (2026-11-10) yapılır.

**Bekleyen**
4. `/parlakisik` içeriği yazılacak. Şu an `noindex` + sitemap dışı, içeriği
   boşaltıldı. Tedavi **uygulanıyor**, eksik olan sadece sayfa.
5. **`/hakkimda` — taslak, yayında değil.** Amaç: ana sayfayı özgeçmiş görünümünden çıkarmak.
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
6. İyi Psikolog ve Türkiye Psikiyatristleri'ne adres güncelleme maili gönderildi,
   takip edilecek. Doktorum360 için KVKK 11. madde talebi opsiyonel.
   (DoktorTakvimi ve Doktorsitesi düzeltildi.)

**En son — içerik bittikten sonra**
7. Yeniden tasarım ("yapay zeka yapımı" görünümden çıkarmak). Yöntem kararlaştırıldı:
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
