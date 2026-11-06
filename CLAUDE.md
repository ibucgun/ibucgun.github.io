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
ayrı bir ruhsat türüdür; yerine "ayaktan muayene ve tedavi". `/klinik` sayfasının başlığı ve menü,
404, `llms.txt` etiketi **"Hizmetler"**dir; URL `/klinik` trafik ve linkler nedeniyle değişmez. Google Business Profile adı
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

**Tedavi yanıtı terimleri TPD Depresyon Tedavi Kılavuzu'na göre** (Öztürk, Tatlı, Buçgün ve ark.
2025; hekimin yazarı olduğu kılavuz, hastalık sayfalarında kaynak): yanıt = ölçek puanında en az
%50 azalma · **düzelme = remisyon** · **iyileşme = düzelmeden sonra en az 6 ay iyilik hâli**
(recovery) · depreşme = relapse · yineleme = recurrence. "İyileşme (remisyon)" yazılmaz.

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

## Görsel kimlik

Kurumsal font **Poppins**, tek font (gövde için ikinci font eklenmez: yükü artırır, kullanıcı kararı
2026-11-06). İstenen izlenim: sakin, sıcak, sade, modern ve çağdaş; yeniden tasarımda yön
**akademik ve kanıta dayalı**. Logo/monogram yok, site adı düz metin kalır.
Yalnız **400 ve 600** yüklenir (yükleme hızı); yeni kalınlık eklenmez. Mobil (≤600px) yazı
kademeleri ana sayfaya göre `_variables.scss`'te: `$fs-m-title` 1.75rem · `$fs-m-h2` 1.4rem ·
`$fs-m-h3` 1.2rem · `$fs-m-body` 1.1rem / `$lh-m-body` 1.75. İç sayfa, hastalık sayfası ve blog
bunları kullanır; yeni bileşende mobil boyut sayı olarak yazılmaz. Telefonda gövde metni sola
yaslıdır (iki yana yaslama dar ekranda kelime arası boşluk açar); masaüstünde iki yana yaslı (iç sayfalar ve blog yazıları dahil).
**Metin içi bağlantılar:** zeytin, altı çizili; site içi sayfa bağlantıları (`href="/…"`) ayrıca kalın.
`inline-block` **verilmez**: tek parça bağlantı alt satıra inip kalan satırın kelime aralarını açıyordu
(kullanıcı kararı 2026-11-06, ölçümle). Paragraflarda `text-wrap: pretty`; heceleme (`hyphens: auto`)
masaüstünde açık ama Chrome Türkçe hecelemiyor, yalnız Firefox/Safari'de etkili. Metin sütunu
daraltılmaz (~70 karaktere daraltma denendi, iki yana yaslı metinde boşlukları artırdığı için geri alındı).
Telefon ve e-posta bağlantıları otomatik olarak yuvarlak zeminli etiket (açık zeytin); başka bir
bağlantı için `.link-chip` sınıfı var, sayfa bağlantılarında kullanılmaz (telefonla karışıyor).

### Marka renkleri (2026-11-04'te son hâli)

**Ana renk: zeytin #59643a** (beyazda 6,3:1) — sitenin genel tonu. **Eylem rengi: çini kiremidi
#9d4c2f** (6,0:1) — **yalnız butonlar**. Kaynak: muayene odasındaki kiremit kadife koltuk; zeytin
Akdeniz paletinin eşi (kiremit çatı, zeytin ağacı). Canlı site kopyası üzerinde demo yapılarak
seçildi. Koyu zeytin #4b5431 gövde metnine çok yakın kaldığı için (H3 ve bağlantılar siyah
okunuyordu) bir ton açıldı; #606c3d 5,7:1 ile kontrast sınırına yakın bulundu.

| Görev | Zeytin (`$brand…`) | Kiremit (`$action…`) |
|---|---|---|
| Ana ton | #59643a | #9d4c2f |
| Koyu (üzerine gelince) | #424a2b | #7a3b24 |
| Açık zemin (rozet, simge kutusu) | #eff2e4 | #f7f1ee (çerçeveli buton hover) |
| Yüzey (İçindekiler, açık akordeon, bilgi kutusu, altbilgi) | #f4f6eb (`$surface-alt`) | — |
| Çok açık zemin (hastalık kutuları, kaynak kutusu) | #f9faf3 | — |
| Kenarlık | #dde0d7 · belirgin #cacec0 | — |

**Görev ayrımı:**
- **Kiremit = yalnız buton:** "Randevu Al" (ana sayfa, sayfa sonları, sabit çubuk), menüdeki "Randevu", WhatsApp, blog
  yazısındaki randevu kutusunun butonu. Başka hiçbir öğeye kiremit verilmez.
- **Buton hiyerarşisi:** "Randevu Al" **dolu** kiremit (birincil); WhatsApp **çerçeveli**
  (beyaz zemin, kiremit yazı ve 2px çerçeve; çerçeve `inset` gölgeyle çizilir ki boy değişmesin).
- **Etiketler:** arama açan butonlar "Randevu Al" + altında numara; menüdeki `/randevu` bağlantısı
  "Randevu" (aynı etiket iki ayrı iş yapmasın, kullanıcı kararı 2026-11-06). `/tms` ve `/tdcs` "Bilgi Al".
- **Hareket:** üzerine gelince yukarı kalkma, dönme, büyüme yok (hazır tema izi); yalnız renk, kenar ve
  gölge değişir. Fotoğraf arkasında parlama yok. Simgeler satır içi SVG, emoji simge kullanılmaz.
  `prefers-reduced-motion` genel kuralı `_base.scss`'te.
- **Zeytin = geri kalan her şey:** başlık altı çizgisi, H2 yanındaki dikey çubuk, H3, metin içi
  bağlantılar, rozetler, simgeler ve simge kutuları, kart kenarları, hover, İçindekiler başlığı,
  ikincil bilgi satırları ("Adana Psikiyatri ve TMS", tarih).
- Renk körlüğünde iki renk karışabilir; kiremit yalnız butonda olduğu için ayrım biçimle
  (buton şekli ve yazısı) korunur.
- İkisi dışında renk yok; geri kalan her şey sıcak nötrlerle.

**Değişkenler:** `$brand`, `$brand-dark`, `$brand-tint`, `$brand-wash`, `$brand-line(-strong)`
(zeytin) ve `$action`, `$action-dark`, `$action-tint` (kiremit, yalnız butonlarda). Eski
`$brand-alt…` değişkenleri kaldırıldı (ana renkle birleşti). Kutu zeminleri zeytin tonunda
(ton açısı ana renkle aynı, az doygun): İçindekiler, açık akordeon, bilgi kutusu ve altbilgi
`$surface-alt`, hastalık kutuları ve kaynak kutusu `$brand-wash`; etiketleri zeytin. Acil kırmızısı `$danger`
#a61b3a. Favicon, `apple-touch-icon.png` ve harita görselindeki etiket zeytine boyandı (eski
kiremit ve mor hâlleri git geçmişinde); harita iğnesi Google kırmızısı kalır.

**Bu seçimde geçerli olan ilkeler** (renk yeniden tartışılırsa):
- Zemin **beyaz**. Sıcaklık metin (#2b2724, gövde #4a4540, ikincil #6f6a64), nötr griler
  (kenarlık #e6e3de, belirgin #d6d2cb). Kutu zeminleri ana rengin açık tonudur; kiremide uyan
  krem Skylight yüzey (#f6f5ee) zeytin ana renge geçince açık zeytine (#f4f6eb) çevrildi.
- Renk, şablon renklerinin **hepsinden** ΔE ≥ 10 uzak olmalı: Tailwind, Bootstrap, Material,
  shadcn/Vercel, Stripe ve Discord "blurple". Eski #4d41e0 Tailwind `indigo-600`'e ΔE 2'ydi,
  "yapay zekâ / şablon" görüntüsünün ana kaynağıydı. Ölçü CIE76 ΔE; Tailwind 3 **ve 4**
  (v4'te gri "olive" skalası var) ile Radix de kontrol edilir. Zeytin #59643a ≥ 15 (en yakın
  Radix lime12 15,2); çini kiremidi 11,9 (Tailwind 3 amber-800). Koyu zeytin #4b5431 Radix
  lime12'ye 8,8'di.
- Rengin **fiziksel bir kaynağı** olmalı (boya, toprak, kumaş); az doygun, hafif kırık.
- Beyazda en az 5,5:1. İki renk birlikte kullanılacaksa renk körlüğü simülasyonunda
  (protanopi, deuteranopi) ayrışma kontrol edilir; ayrışmıyorsa görevler biçimle ayrılır.
- Bekleme salonundaki yanık turuncu kullanılmaz (eski turuncuya yakın); açık gri koltuklar
  nötr tonların kaynağı.

**Elenenler ve gerekçesi** (tekrar önerme):
- #4d41e0 ve "biraz yumuşatılmış" hâlleri (doygunluk %46'ya kadar hâlâ Tailwind indigo
  skalasında); "sakin mor" #5048a8 Material indigo'ya ΔE 6,7.
- Erik, mürdüm, fuşya, gül tonları (ton 300–340°): kadın sağlığı / tüp bebek çağrışımı.
- Sage ve açık yeşiller: "wellness / alternatif tıp" çağrışımı; sage 2026'da "fazla
  kullanılmış", açık hâli beyazda 2,4:1. (Zeytin bu kaygıya rağmen 2026-11-04'te kullanıcı
  kararıyla ana renk oldu: koyu ve kırık tonu, kiremitle birlikte Akdeniz paleti.)
- Mürekkep indigo, gece mavisi gibi çok koyu tonlar: "eski usul".
- Önceki kiremit #9b4c36: kahve alt tonlu, "ölü" bulundu. Canlı kiremit #a9462d: Tailwind
  `orange-800`'e ΔE 9,4.
- Mavi aile (denim #43559d, lacivert-mavi #3e5998): şablondan ayrışıyor ama fiziksel
  kaynağı/hikâyesi zayıf, sağlıkta en kalabalık renk bölgesi; 210°'nin altı Tailwind
  sky/cyan'a giriyor.
- Eski sitenin turuncusu #cc5400 ve ona yakın tonlar (ΔE < 20): "eski siteye dönüş".

### Renk kuralı — kalıcı

**Sitenin bütün renkleri `_sass/_variables.scss`'te, görev adıyla tanımlıdır** (`$brand`,
`$brand-tint`, `$action`, `$text-body`, `$border`, `$danger` …; listenin kendisi ve her birinin görevi
dosyada yazılı). Başka hiçbir SCSS dosyasına, layout'a, include'a, sayfaya ya da yazıya sabit
renk kodu (`#rrggbb`, `#rgb`, `rgb(…)`, `rgba(0,0,0,…)`) **yazılmaz**:

- Renk gerekiyorsa mevcut görevlerden biri kullanılır. Hiçbiri uymuyorsa önce
  `_variables.scss`'e **görev adıyla** yeni değişken eklenir, sonra o kullanılır.
  Birbirine yakın yeni bir ton eklenmez: aynı iş için tek değer.
- Saydamlık için sayı yazılmaz: `rgba($brand, $alpha-soft|mid|strong)`,
  gölgede `rgba($shadow-color, $shadow-faint|soft)`.
- Satır içi SVG'lerde renk `currentColor`'dır; rengi kapsayan öğenin CSS `color`'ı verir.
  Simge `<img>` olarak eklenmez (dış SVG dosyasının rengi CSS'ten değiştirilemez).
- Blog kategori rozetlerinin hepsi aynı marka rengindedir; kategoriye özel renk yoktur.
- Vurgu için yalnızca iki renk var: ana renk (zeytin) ve eylem rengi (kiremit, yalnız buton),
  görevleri yukarıda. Üçüncü bir vurgu rengi eklenmez.
- Marka rengini değiştirmek = `_variables.scss`'te tek satır. Favicon, `apple-touch-icon.png`,
  harita görseli (`images/klinikkonumu.webp`) ve paylaşım görseli ayrıca güncellenir.

**Kontrol (her SCSS/şablon değişikliğinden sonra; çıktı boş olmalı):**

```bash
grep -rniE '#[0-9a-f]{6}\b|#[0-9a-f]{3}\b|rgba?\( *[0-9]' _sass _layouts _includes _posts *.html | grep -vE '^_sass/_(variables|normalize)\.scss:|^_includes/(icons|schema)/'
```

İstisnalar: `_normalize.scss` (tarayıcı sıfırlama, dokunulmaz), `_includes/schema/`
(JSON-LD; renk yok, `#hekim` gibi kimlikler var), `_includes/icons/` (temadan kalma, hiçbir
yerden çağrılmayan sosyal medya ikonları). Komut `href="#abc"` gibi yalnız a–f harfli bir
sayfa içi bağlantıyı da yakalayabilir; öyle bir satır renk değildir, atlanır.

## Muayenehane bilgileri (NAP — her yerde birebir aynı olmalı)

Adres açık biçimde yazılır ("Mahallesi", "Sokak"; "Mah./Sok." kısaltması yok), Google Business
Profile ile aynı (kullanıcı kararı 2026-11-06). Schema'da `streetAddress` yalnız sokak kısmıdır.

```
Uzm. Dr. İsmail Buçgün
Güzelyalı Mahallesi 81161. Sokak No:4/107, 01170 Çukurova / Adana
+90 551 033 48 96
bilgi@ismailbucgun.com
Pazartesi–Cuma 09:00–19:00
```

Sitede görünen telefon biçimi her yerde **0 (551) 033 48 96** (`tel:+905510334896`); "0551 033 48 96"
yazılmaz. `+90 551 …` yalnız schema ve dış profiller içindir.

**Randevu:** yalnızca bu telefon numarasından verilir; başka site ya da uygulamadan randevu verilmez
(sitede yazılı). Aramaları muayenehane asistanı yanıtlar (yalnız `/randevu`'da yazılı: hasta doğrudan
hekime ulaştığını sanıyordu). Sitede **tek saat** yazılır: çalışma
saatleri = Google Business Profile = schema, Pazartesi–Cuma 09:00–19:00. Ayrı "muayene saati" ya da
Cumartesi telefon saati yazılmaz (asistan Cumartesi de yanıtlıyor ama Business Profile'da Cumartesi
kapalı; az söz verilir, kullanıcı kararı 2026-11-05). Business Profile saati aramalarda görünürlük için
telefona göre ayarlı. Yönlendirme sırası her yerde **önce arama**,
WhatsApp "arayamadığınız durumlarda" (WhatsApp dönüş süresi yazılmaz).

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
| **Psikoterapi** (BDT, KİPT, destekleyici, psikanalitik) | Muayene ve takip görüşmeleri bu eğitimlerle şekillenir (teknikleri kullanılır), ama **haftalık seanslarla yürütülen yapılandırılmış psikoterapiye şu anda yeni hasta kabul edilemiyor.** **Çift ve aile terapisi uygulanmıyor.** İhtiyacı olan yeni hasta ilk muayenede veya takipte belirlenip o yöntemle çalışan uzmana **yönlendirilir**; psikiyatrik takip ve ilaç muayenehanede sürebilir |
| **Acil durumlar** (intihar riski, kendine/başkasına zarar, akut kriz, deliryum) | Muayenehane acil hizmet vermez. "Randevu alabileceğiniz durumlar" listelerine **yazılmaz**; her zaman "randevu beklemeden 112 Acil Çağrı Merkezi'ni arayın veya en yakın hastanenin acil servisine başvurun" kalıbıyla yönlendirilir |
| Çocuk ve ergen psikiyatrisi | Hizmet verilmiyor (18+) |
| **Online muayene ve takip** | **Hiç yapılmıyor** — ilk muayene, kontrol ve takip dahil yalnızca yüz yüze. "İlk muayene yüz yüze" diye **yazılmaz**: kronik hastalar kontrollerin online olabileceğini sanıp geliyordu |

Eğitim ve sertifika kayıtları (`_data/aldigiegitimler.yml`, schema `hasCredential`,
`knowsAbout`) **kalır** — eğitim beyanı serbesttir, hizmet beyanı değildir.

**Psikoterapi nasıl yazılır:** Çerçeve "yapmıyorum" değil, **"haftalık seanslarla yürütülen
yapılandırılmış psikoterapi için şu anda yeni hasta kabul edemiyorum"** — nitelemesi düşürülmez
(yalnız "psikoterapi" yazınca hekim terapi bilmiyor/yapmıyor diye okunuyordu). `/klinik` ve SSS'de
ayrıca "Muayene ve takip görüşmelerim aldığım psikoterapi eğitimleriyle şekillenir … tekniklerinden
yararlanıyorum" yazılır; hastalık sayfalarına eklenmez (kalıp tekrarı). Seyrek görüşme "psikoterapi"
diye sunulmaz, başkalarının uygulamasına atıf yapılmaz (karşılaştırma). Hastalık sayfalarında kılavuz
bilgisi kalır ("OKB'de kılavuzlarda önerilen yöntem BDT'dir"), ardından: "Şu anda haftalık seanslarla
yürütülen yapılandırılmış psikoterapi için yeni hasta kabul edemediğimden, … hastaları bu yöntemle
çalışan bir uzmana yönlendiriyorum." Yalnız
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
| `images/paylasim-2026-11.jpg` | Paylaşım önizlemesi (OG/Twitter, 1200×630): ana sayfa üst bölümünün ekran görüntüsü. Tasarım ya da renk değişince yeniden çekilir, **dosya adı da değişir** (WhatsApp/Facebook önbelleği). Çekim: Firefox headless `--window-size=1394,732 --screenshot`, ardından `sips -z 630 1200` (çerçeve eskisiyle aynı kalır) |
| `_includes/schema/hekim-klinik.html` | Ana sayfa JSON-LD (Physician + MedicalClinic) |
| (kural) | Yapısal veri **yalnız JSON-LD**; şablonlarda mikro veri (`itemscope`/`itemprop`) kullanılmaz. `page.html` eskiden her sayfayı `Person` işaretliyordu ("Depresyon adında kişi"), 2026-11-06'da kaldırıldı |
| `_includes/schema/tms.html` | `/tms` JSON-LD (FAQPage + MedicalProcedure) |
| Kökteki hastalık sayfaları | `depresyon.html` vb.; `layout: hastalik` |
| `_layouts/hastalik.html` | Hastalık sayfası şablonu: kaynaklar, uyarı (otomatik tarih), acil kutusu, CTA |
| `_includes/schema/hastalik.html` | `MedicalWebPage` + `MedicalCondition`; yazar ve gözden geçiren `/#hekim` |
| `_includes/iletisim-cta.html` | Ara / WhatsApp butonu; `baslik`, `metin`, `buton` parametreleri |
| `_includes/sabit-arama-cubugu.html` | Telefonda (≤600px) altta sabit Randevu Al / WhatsApp çubuğu; `footer.html`'den çağrılır (`.page-footer` dışında). Sayfadaki arama butonları ekrandayken çekilir. GA4 `sabit_cubuk` |
| `_includes/acil-kutusu.html` | Acil durum kutusu (112 kalıbı); hastalık şablonu ve `/randevu`; `baslik`, `metin` parametreleri |
| `_sass/_variables.scss` | Sitenin tüm renkleri (görev adlı değişkenler) ve saydamlık seviyeleri |
| `llms.txt` | Dil modelleri için site özeti — **hizmet değişince güncelle** |
| `.claude/skills/metin-denetimi/` | Metin denetimi skill'i: mevzuat + yapay zekâ yazım izleri; `scripts/denetle.py` tarama, yedek ve karşılaştırma |

### Hastalık sayfası düzeni

Hepsi **`layout: hastalik`** kullanır. Sayfa dosyasında yalnızca içindekiler ve 6 bölüm
bulunur. **Kaynaklar → yasal uyarı → acil durum kutusu → CTA** şablondan gelir, sırası
sabittir. Acil kutusu her sayfada var ve **CTA'nın hemen üstünde**: sayfa tek bir "ne
yapmalıyım" bloğuyla kapanır (acilse 112, değilse randevu).

**Front matter:** `title` (H1, kısa) · `seo_title` (`<title>`; kalıp **"[X] Tedavisi"**, sonek
dahil ≤55 karakter — uzarsa Google sondan keser ve "Adana" kaybolur; şemsiye sayfada yazılmaz, H1 kullanılır) · `description` (≤155, tırnaklı) · `lead` (tek cümle) ·
`kosul` / `kosul_diger` (schema `MedicalCondition`) · `refs` (kaynak listesi) · `acil` /
`acil_baslik` (yoksa genel metin; OKB'de yalnız intiharı anan kısa metin — genel metindeki "başkalarına
zarar verme düşünceleri" zarar obsesyonu olan hastayı korkutur) · `last_modified_at` (uyarıdaki tarih ve schema
`lastReviewed` buradan gelir; elle tarih yazılmaz).

**Bölümler — her sayfada aynı sıra ve aynı kalıp.** 1–5 **genel bilgidir**: nesnel, edilgen,
kaynaklı; birinci şahıs yok. Hekimin kendi yaklaşımı yalnız 6. bölümdedir (kullanıcı kararı,
2026-10-26: genel bilgi arasına giren "ben böyle yapıyorum" cümleleri sesi bölüyordu).
1. **[X] nedir?** — Blog yazısı varsa kısa tutulur, yazıya link verilir.
2. **[X]'in belirtileri nelerdir?** — liste.
3. **[X]'te değerlendirme nasıl yapılır?** — kılavuzlara göre genel değerlendirme.
4. **[X] nasıl tedavi edilir?** — alt başlıklar sabit sırada: ilaç → TMS / derin TMS (varsa,
   `/tms` linki) → diğer ilaç seçenekleri (esketamin gibi, varsa) → psikoterapi → muayenehanede
   uygulanmayanlar (EKT) → diğer (parlak ışık vb.). **İstisna:** muayenehane notları
   (EKT kutusu, psikoterapi yeni hasta kalıbı, esketamin kalıbı) ilgili seçeneğin yanında kalır;
   notsuz anılan seçenek sunuluyormuş gibi okunur.
5. **[X] tedavisi ne kadar sürer, takip nasıl yapılır?** — genel seyir ve kılavuz süreleri.
6. **Adana'da [X] değerlendirmesi ve tedavisi** (`id="muayenehane"`) — birinci tekil. İlk cümle
   yerel: "Adana Çukurova'daki muayenehanemde…". Değerlendirmede neye bakıldığı, ölçekler,
   testler, muayenehanede uygulanan tedaviler, kontrol aralıkları. Kendi içinde tam bir pasaj:
   "Adana'da X tedavisi" sorusunda alıntılanacak yer burası.

Neden böyle (arama ve yapay zekâ): yapay zekâ sistemleri sayfayı pasaj pasaj alıntılar.
Başlıklarda hastalık adı geçer ki pasaj başlığıyla alıntılandığında bağlam kalsın. Her
bölümün **ilk cümlesi soruyu tek başına cevaplar** ("Bu yöntem…" diye başlamaz). Yerel
cümle olmadan "Adana'da X için kime gidilir?" sorusunda sayfa kaynak gösterilemez. Metin
içinde en az 2 ilgili sayfaya link. "Sık sorulanlar" bölümü **eklenmez** (karar).

**Kapsam:** Sayfa yalnız muayenehanede yapılanı değil, **kılavuzdaki seçenekleri** anlatır.
Muayenehanede uygulanmayan bir seçenek (EKT gibi) genel bilimsel bilgi olarak, kaynağıyla
yazılır; hemen yanında "muayenehanede uygulanmamaktadır, … yönlendirilir" notu bulunur.
Seçeneği hiç anmamak sayfayı eksik bırakır; notsuz anmak sunuluyormuş gibi okunur.
**İstisna:** kılavuzun o hastalıkta önermediği bir yöntem (OKB'de EKT) tedavi seçeneği olarak
yazılmaz (alt başlık yok, muayenehane notu yok); tedavi bölümünün giriş paragrafında tek cümleyle
"rutin olarak önerilmez" diye anılır — hasta ve yakınlarının yanlış inancını düzeltmek için
(kullanıcı kararı, 2026-10-27).

**Uzunluk: 650–1050 kelime** (bağlayıcı; 6 bölümlük düzene geçince 950'den yükseltildi, kullanıcı kararı 2026-10-27) — bölüm aralıkları yol göstericidir: nedir 80–120 ·
belirtiler 80–150 · değerlendirme 60–120 · tedavi 200–300 · takip 80–130 · muayenehane 120–180. Tedavinin asıl konu
olduğu sayfada (dirençli depresyon) tedavi bölümü uzayabilir. Büyüme eksik konudan gelir,
dolgudan değil.

**Yeni sayfa akışı:** kullanıcı kaynakları verir, 1–5. bölümler 6. bölüm düşünülerek
yazılır, 6. bölüm kullanıcının anlattığı uygulamayla en son yazılır. O zamana kadar `noindex` + sitemap
dışı; kullanıcı onayıyla bu iki satır silinir, `last_modified_at` güncellenir. `metin-denetimi`'nin
A10 (atıfsız otorite) bulgularına atıf eklenir. 8 sayfanın hepsi yayında (2026-11-01).

**Sayfaya özgü kararlar** (kullanıcı kararı/beyanı, 2026-10):
- `anksiyete-bozukluklari`: TMS ve pregabalin anılmaz (pregabalin kötüye kullanım nedeniyle).
- `eriskin-dehb`: Türkiye'de amfetamin grubu yok, uyarıcı olarak metilfenidat.
- `sizofreni`: TMS (4.2 ve 6. bölüm, `/tms` 3.2 ile uyumlu): işitsel halüsinasyonda klozapin sonrası, negatif belirtilerde ilaç tedavisine rağmen süren durumda, tedaviye ek olarak. Uzun etkili
  enjeksiyon reçete edilir, başka kurumda uygulanır.
- `yaslilik-psikiyatrisi`: **alan sayfası**, hastalık iskeleti uymaz; 5 bölüm (nedir · neden ayrı
  alan · konular · değerlendirme ve tedavi · muayenehane), ~1200 kelime. "Neden ayrı alan"
  tanı üstü yazılır, tek hastalık üzerinden değil. "Pozitif yaşlılık psikiyatrisi" bölümü
  yazılmaz. Türkiye'de yan dal olmadığı kaynaksız yazılır. TMS tedaviye yanıt alınamayan
  durumlarda, özellikle depresyonda; Adler 2026 *Am J Psychiatry* "ilaçtan üstün" diyor ama
  karşılaştırma yazılmaz, yalnız "daha erken kullanılabilir" sonucu. Deliryum kutusu konuya
  özgü, içerikte kalır. Hedef kitle halk: tıbbi terim yerine sade ifade.
- `tms` (hastalık şablonu dışında, `layout: page`; kaynak kutusu elle): **gebelik hiç anılmaz**
  (gebelere TMS uygulanmıyor); doğum sonrası ve emzirme dönemi kalır. Kafa içi metal implantta
  "uygulanmaz"; kalp pili, nöbet/epilepsi öyküsü ve nöbet eşiğini düşüren ilaçta "muayenehane
  ortamında uygulama güvenli olmayabilir". 2021 anksiyetenin eşlik ettiği depresyon onayı **derin
  TMS**'e aittir. OKB onay yılı (2018) FDA duyurusundan; Cohen 2022 2017 yazıyor, kullanılmaz.
  Sayfa metni hekimin kendi yazısı: kaynak eklerken dili değiştirilmez.

Punto kademesi: gövde 1.18rem → TOC 0.88rem → kaynaklar 0.8rem → uyarı 0.75rem. TOC ve
kaynak kutusu blogdaki `.post-toc` / `.post-refs` ile aynı dili konuşur; uyarıya kutu verilmez.

### Ölçüm (GA4)

`head.html` telefon ve WhatsApp tıklamalarını `phone_click` / `whatsapp_click` olayı ve
`link_location` parametresiyle gönderir (`hero`, `cta`, `iletisim_karti`, `menu`, `footer`,
`sabit_cubuk`, `icerik`). GA4'te ikisi **anahtar etkinlik**, `link_location` özel boyut ("Buton konumu").
Uçtan uca 2026-10-20'de doğrulandı. `gtag` kuyruğu sayfa başında tanımlı (erken tıklama
kaybolmasın), ağ yüklemesi gecikmeli. Yeni bir buton kapsayıcısı eklenirse `konum`
eşlemesine ekle.

**Referans dönemi: 2026-10-20 → 2026-11-10.** Bu tarihe kadar dönüşümü etkileyecek büyük
değişiklik (`/tms` başlığı, ana sayfanın sadeleşmesi) yapılmaz; önce mevcut durum ölçülür.
Veri çok azsa dönem uzatılır. **İstisnalar** (kullanıcı kararı): 2026-10-25'te butonlar mordan
kiremide; 2026-11-04'te ana renk zeytin oldu ve WhatsApp butonu çerçeveli ikincil butona döndü
(büyük olasılıkla `whatsapp_click`'i etkiler); aynı gün `/tms` arama başlığı "TMS ve Derin TMS
Tedavisi Nedir?" ve açıklaması yeniden yazıldı (önceki CTR: 62.437 gösterim, %0,73; Search
Console'da 11-04 öncesi ve sonrası karşılaştırılır). 2026-11-06'da telefonda altta sabit arama
çubuğu eklendi (kullanıcı kararı: dönüşüm bütün işler bitince toplu değerlendirilecek, acelesi yok).
Dönüşüm verisi dört parça okunur: 10-20 → 10-24 (mor), 10-25 → 11-03 (kiremit, iki dolu buton),
11-04 → 11-05 (zeytin, WhatsApp çerçeveli), 11-06 → (sabit arama çubuğu; aynı gün altbilgiye
adres · telefon · saat satırı eklendi, `footer` konumu o güne kadar telefon içermiyordu; menüdeki
"Randevu Al" "Randevu" oldu; hover efektleri kaldırıldı; blog yazısı sonundaki randevu kutusu `/randevu`
yerine doğrudan arar, GA4 `cta`).

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
  stilleniyor** (`_resume.scss`, "MODERN İÇERİK" bloğu: `h3` 1.4rem renkli + 2.5rem üst
  boşluk, `p` 1.18rem + 1.95 satır aralığı). Sayfa içinde küçük bir bileşen (kutu başlığı,
  ince yazı) yaparken `font-size`, `color`, `margin`, `line-height`'a **`!important`
  vermezsen kuralın sessizce ezilir.** Kaynak kutusu ve yasal uyarı bu yüzden ilk
  yayında büyük göründü. Alternatif: başlık için `h3` yerine `strong` kullan (TOC böyle).
  Global `!important`'ı kaldırma — 13 sayfadaki tüm başlık ve paragrafları yönetiyor.
- **Yazdırma stili `_resume.scss`'in en sonundaki "YAZDIRMA" bloğundadır**; ekrandaki `!important`
  kuralları ezebilmesi için sonda kalır. Sayfa kapsayıcısına (`article`) `no-print` verilmez:
  `page.html`'de verildiği için iç sayfalar yazdırılınca boş çıkıyordu. Yaşlı hastaların
  yakınları sayfayı yazdırıyor; telefon numarası baskıda düz metin olarak kalır.
- Mobil menü gerçek `<button>` + `navigation.html`'deki küçük betik (`aria-expanded`, ✕, Esc,
  odak döngüsü); onay kutusu yöntemine dönülmez. Tarayıcı paneli arka plandayken CSS geçişi
  ilerlemez: menü "gizli" ölçülürse önce ekran görüntüsü al.
- `noindex` için front matter'a `noindex: true` yaz (`head.html` bunu okur).
  `robots.txt`'ye `Disallow` **ekleme** — engellenen sayfa taranamaz, dolayısıyla
  `noindex` görülmez.

---

## Kalan işler

**Site içi**
1. İç linkleme — şu sayfalardan hiç iç link çıkmıyor: `tdcs`, `blog`.
   `/tms`'den hastalık sayfalarına link 3.1/3.2 listelerindeki hastalık adlarından verilir;
   `/anksiyete-bozukluklari`'na verilmez (o sayfa bilinçli olarak TMS'yi anmıyor).
2. **`/tdcs` kaynakları.** 6 atıfsız iddia var, kaynak listesi yok (yalnız tek bir satır içi
   "Kaynak:" notu). `/tms` ve `/klinik`'teki kaynak kutusu (`.page-refs`, elle eklenmiş) örnek alınır.

> Hastalık sayfaları muayenehanedeki **değerlendirme ve tedavi sürecini** anlatır,
> hastalığın "nedir"ini **blog yazıları** anlatır. Aynı metni iki yere yazma;
> birbirine link ver. Ana sayfa kutuları, `llms.txt` ve blog geri linkleri bağlandı.

**Bekleyen**
- **Blog yazısı: "Bipolar bozuklukta hastane yatışı ne zaman gerekir?"** Yatarak tedavi ölçütleri
  (CANMAT'ın tedavi ortamı değerlendirmesi), acil durumda 112 kalıbı; istemsiz yatış anlatılacaksa
  hukuki dayanak gerçek kaynakla. `medical-blog-writer` ile yazılır, `metin-denetimi` ile denetlenir.
  Bipolar sayfasının 6. bölümündeki yatış cümlesinden yazıya link verilir.
- **Blog yazısı: "Tedaviye dirençli bipolar depresyon".** Ana kaynak: ISBD task force raporu
  (kullanıcı gönderecek). Ek: tanım için Br J Psychiatry 2019;214:27-35 uzlaşı tanımı (en az iki
  yeterli tedavi denemesi, her biri en az 8 hafta), Schoeyen 2015 *Am J Psychiatry* (EKT RKÇ),
  Elsayed 2022 *Neuropsychiatr Dis Treat* derlemesi (üçü Singh 2025 *Lancet*'te atıflı; künyeler
  yazarken kaynaktan doğrulanır). Bipolar ve dirençli depresyon sayfalarından link verilir.
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
     Hekim dönem dönem halka açık psikoeğitim etkinlikleri düzenledi (konu ve sürüp sürmediği
     kullanıcıdan alınacak); olgu olarak yazılır, sayı ve ilgi beyanı yazılmaz.
   - **Sıra:** ölçüm kuruldu; yayın referans döneminden sonra (2026-11-10) — ana sayfa
     "adana psikiyatri"de üst sırada, değişikliğin etkisi ölçülebilmeli.
   - Yayın listesi: noindex/sitemap satırlarını sil, `last_modified_at` ekle · ana sayfadan
     4 bölümü kaldır, yerine kısa yeterlilik özeti (FEBP + uzmanlık sonrası eğitimler) ve
     `/hakkimda` linki · menü ve footer linki · blog yazar kutusundan link · `llms.txt` ·
     schema: `/hakkimda`'ya `ProfilePage` (`mainEntity` → mevcut `/#hekim`; ikinci kişi düğümü
     açılmaz, Physician ana sayfada kalır), `hasCredential`'a DUSEP, RCPsych, NEI · Search
     Console'dan dizine ekleme isteği · 2–3 hafta sıralama takibi.

- **Tasarım raporu (2026-11-06) — kalan işler.** Rapor kararları: masaüstünde iki yana yaslı
  kalır; Instagram **ana sayfada görünür kalır** (aktif kullanılıyor, oradan hasta geliyor;
  altbilgiye taşınmaz, yalnız dönme efekti kaldırılabilir); C5 alt metin önerisi reddedildi. Altbilgi sade kalır: tek iletişim satırı + yasal
  satırlar; hastalık bağlantıları ve sütunlu düzen denendi, kalabalık bulundu (kullanıcı kararı).
  `/iletisim`'deki Google Haritalar iframe'i kalır (`loading="lazy"`, çerez politikasında yazılı; yol
  tarifi için etkileşim gerekli); ana sayfada sabit harita görseli kalır.
  - **Tıklamayı etkileyenler, tek tek, başlangıç tarihi not edilerek:** hero: Türkçe unvan, kısa paragraf, mobilde sola yaslı, küçük fotoğraf · `/hakkimda` ile birlikte.
  - Hekim fotoğrafı 800 px + `srcset` (D3): büyük asıl fotoğraf kullanıcıdan bekleniyor.
  - `/tms` ve ana sayfadaki TMS görselleri üreticinin tanıtım görseli/stok: muayenehanedeki
    cihazın sade fotoğrafıyla değiştirilecek (çekilebilir; bina girişi fotoğrafı `/iletisim` için).
  - Okunabilirlik: kalın yazının azaltılması (B5; ana sayfa girişi, `/klinik`, `/tms` 7. madde) —
    metin işi, sayfa sayfa önerilir, `metin-denetimi` ile.

**Site dışı**
6. İyi Psikolog ve Türkiye Psikiyatristleri'ne adres güncelleme maili gönderildi,
   takip edilecek. Doktorum360 için KVKK 11. madde talebi opsiyonel.
   (DoktorTakvimi ve Doktorsitesi düzeltildi.)

**Sonra düşünülecekler** (şimdilik yapılmaz, kullanıcı kararı 2026-11-06)
- **Menüde hastalık sayfalarına erişim (A3).** Hastalık sayfalarına menüden ulaşılamıyor; altbilgiye
  bağlantı koymak kalabalık bulundu, menüye ekleme ertelendi. Konuşulan seçenekler: (1) menüde
  "Hastalıklar" → ana sayfadaki Çalışma Alanlarım bölümü (`/#…`), yeni sayfa yok; (2) yeni bir
  hastalıklar sayfası, kutular ana sayfayla **tek veri dosyasından** (`_data/`) gelir, kısa giriş ve
  gruplama ile (yalnız liste olursa "içi boş sayfa" olur); (3) `/klinik`'teki ilgili bölüme bağlantı.
  Menü etiketi hasta için "Hastalıklar" daha anlaşılır; telefonda tek madde (15 madde sığmaz).

**En son — içerik bittikten sonra**
7. Yeniden tasarım ("yapay zeka yapımı" görünümden çıkarmak). Marka renkleri uygulandı: bkz.
   "Görsel kimlik → Marka renkleri" (kalan iş orada). Yöntem kararlaştırıldı:
   ayrı public repo `tasarim`, önizleme `ismailbucgun.com/tasarim/` adresinde
   (ana site özel domain kullandığı için GitHub proje repolarını onun altına koyar).
   - Başlarken `master`'a `tasarim-oncesi` tag'i at — geri dönüş noktası.
   - Önizleme reposunda `CNAME`'i sil (iki repo aynı domaini talep etmesin),
     `baseurl: /tasarim`, `_config.yml` `defaults` ile tüm sayfalara `noindex`.
   - **Tuzak:** sitedeki kök-mutlak yollar (`/css/main.css` vb., ~87 adet, 24 dosya)
     `relative_url`'e çevrilmeli. Çevrilmezse önizleme canlı sitenin CSS'ini yükler
     ve hata vermeden **eski tasarımı** gösterir. Canlıda çıktı aynı kalır.
   - Birleştirirken `_config.yml` ve `CNAME` ana sitedeki haliyle kalır.
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
