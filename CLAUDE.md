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
| Esketamin | Muayenehanede uygulanabilir ama henüz uygulanmadı. Sitede ne "uygulanır" ne "uygulanmaz" yazılır |
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
gövde 1.125rem → TOC 0.88rem → kaynaklar 0.8rem → uyarı 0.75rem.
TOC ve kaynak kutuları blogdaki `.post-toc` / `.post-refs` ile aynı dili
konuşur (yuvarlak köşe, büyük harfli küçük başlık). Uyarıya kutu verme —
üçüncü bir kutu sayfayı ağırlaştırır; ince yazı zaten ince yazı gibi okunur.
CTA en sonda durur ki sayfa eylemle kapansın.

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
1. **8 hastalık sayfası `noindex` + sitemap dışı.** İçerikleri hazır ve yayında,
   ama arama sonuçlarına kapalı. Her sayfa gözden geçirilip onaylandıkça front
   matter'daki `noindex: true` ve `sitemap:` satırları **tek tek** silinerek açılır.
   Ana sayfa kutuları, blog geri linkleri ve `llms.txt` kayıtları duruyor —
   kaldırma, sayfalar çalışıyor, sadece indekslenmiyor.

   | Sayfa | Açıldı mı |
   |---|---|
   | `depresyon` · `tedaviye-direncli-depresyon` · `okb` · `bipolar-bozukluk` | hayır |
   | `anksiyete-bozukluklari` · `eriskin-dehb` · `yaslilik-psikiyatrisi` · `sizofreni` | hayır |

2. İç linkleme — şu sayfalardan hiç iç link çıkmıyor: `tms`, `klinik`, `randevu`,
   `iletisim`, `tdcs`, `blog`, `eriskin-dehb`, `yaslilik-psikiyatrisi`, `sizofreni`.
   `/tms` en çok gösterim alan sayfa (62.437) ve oradan hiçbir yere gidilemiyor;
   öncelik orada.

> Hastalık sayfaları muayenehanedeki **değerlendirme ve tedavi sürecini** anlatır,
> hastalığın "nedir"ini **blog yazıları** anlatır. Aynı metni iki yere yazma;
> birbirine link ver. Ana sayfa kutuları, `llms.txt` ve blog geri linkleri bağlandı.

**Ölçüm**
3. GA4 dönüşüm takibi yok. `head.html`'de GA kurulu (lazy-load, PageSpeed için)
   ama `tel:` / `wa.me` tıklamaları ölçülmüyor.
4. `/tms` başlık ve açıklama CTR yazımı — 62.437 gösterim, %0,73 tıklama.
   3. madde kurulmadan etkisi ölçülemez.

**Bekleyen**
5. `/parlakisik` içeriği yazılacak. Şu an `noindex` + sitemap dışı, içeriği
   boşaltıldı. Tedavi **uygulanıyor**, eksik olan sadece sayfa.
6. `/hakkimda` sayfası. Ham malzeme: silinen `_data/meslekiilgialanlari.yml`
   (git geçmişinde). Nöropsikiyatri başlığı sitede hiç ayrı anlatılmıyor.

**Site dışı**
7. İyi Psikolog ve Türkiye Psikiyatristleri'ne adres güncelleme maili gönderildi,
   takip edilecek. Doktorum360 için KVKK 11. madde talebi opsiyonel.
   (DoktorTakvimi ve Doktorsitesi düzeltildi.)

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
