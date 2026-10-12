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
kelimeleri **tesis adı olarak** kullanılamaz. Google Business Profile adı
"Uzm. Dr. İsmail Buçgün - Adana Psikiyatri - TMS" ve en önemli hasta kaynağı.

> **Türkçe arama tuzağı:** `grep -i "klinik"` yetmez — ünsüz yumuşaması nedeniyle
> "kliniğimde" eşleşmez. `klini[kğ]` kalıbını kullan.

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
parlak ışık tedavisi · BDT · KİPT · psikometrik ve nöropsikolojik testler ·
ilaç kan düzeyi takibi

## Sunulmayan — bu ayrım önemli

| Yöntem | Durum |
|---|---|
| EKT | Anestezi gerektirir, hastanede uygulanır; hasta yönlendirilir |
| tDCS | Uygulanmıyor. `/tdcs` yalnızca bilgilendirme sayfası |
| Psikanalitik psikoterapi | Eğitimi var, **yeni hasta kabul edilmiyor** |
| Destekleyici psikoterapi | TPD sertifikası var, **yeni hasta kabul edilmiyor** |
| Çocuk ve ergen psikiyatrisi | Hizmet verilmiyor (18+) |
| Online görüşme | İlk muayene yalnızca yüz yüze |

Eğitim ve sertifika kayıtları (`_data/aldigiegitimler.yml`, schema `hasCredential`)
**kalır** — eğitim beyanı serbesttir, hizmet beyanı değildir.

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
| `_data/categories.yml` | Blog kategori renkleri |
| `llms.txt` | Dil modelleri için site özeti — **hizmet değişince güncelle** |

### Senkron tutulması gerekenler

- **Sayfa metni ↔ schema.** `/tms` SSS metinleri `_includes/schema/tms.html`
  içinde birebir tekrarlanır. Birini değiştirince diğerini de değiştir.
- **Hizmet listesi ↔ üç yer:** `klinik.html`, schema `availableService`, `llms.txt`.
- Blog yazılarının URL'leri `permalink: /:title` ile **kilitli**. Global ayar
  `/blog/:title` ama mevcut 6 yazının adresi değişmemeli (trafik var).

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
- `noindex` için front matter'a `noindex: true` yaz (`head.html` bunu okur).
  `robots.txt`'ye `Disallow` **ekleme** — engellenen sayfa taranamaz, dolayısıyla
  `noindex` görülmez.

---

## Kalan işler

**Site içi**
1. Ana sayfada 8 boş link — `_layouts/resume.html:91-129`, `practice-box-small`
   kutularının hepsi `href=""`. Hedefleri: bipolar ve anksiyete → ilgili blog
   yazısı, tedaviye dirençli depresyon → `/tms`, kalanlar → `/klinik` veya `/sss`.
2. İç linkleme yok — `index`, `tms`, `tdcs`, `klinik`, `randevu`, `iletisim`
   sayfalarında sıfır iç link. 1. madde ile birlikte çözülür.
3. `klinik`, `tdcs`, `sikca-sorulan-sorular` sayfalarında iletişim butonu yok.

**Ölçüm**
4. GA4 dönüşüm takibi yok. `head.html`'de GA kurulu (lazy-load, PageSpeed için)
   ama `tel:` / `wa.me` tıklamaları ölçülmüyor.
5. `/tms` başlık ve açıklama CTR yazımı — 62.437 gösterim, %0,73 tıklama.
   4. madde kurulmadan etkisi ölçülemez.

**Bekleyen**
6. `/parlakisik` içeriği yazılacak. Şu an `noindex` + sitemap dışı, içeriği
   boşaltıldı. Tedavi **uygulanıyor**, eksik olan sadece sayfa.
7. `/hakkimda` sayfası. Ham malzeme: silinen `_data/meslekiilgialanlari.yml`
   (git geçmişinde). Nöropsikiyatri ve şizofreni başlıkları sitede hiç
   ayrı anlatılmıyor.

**Site dışı**
8. İyi Psikolog ve Türkiye Psikiyatristleri'ne adres güncelleme maili gönderildi,
   takip edilecek. Doktorum360 için KVKK 11. madde talebi opsiyonel.
   (DoktorTakvimi ve Doktorsitesi düzeltildi.)

---

## Çalışma şekli

- Değişiklikten önce dosyayı oku; varsayımla düzenleme yapma.
- Toplu değişiklikten sonra doğrula (grep sayımı, JSON geçerliliği, link kontrolü).
- Commit ve push kullanıcıya aittir — istemeden commit etme.
- Push sonrası canlı doğrulama `curl` ile yapılır.
