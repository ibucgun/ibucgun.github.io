# Yapay zekâ yazım izleri (Türkçe)

Sinyal taksonomisi **bushrabeg/turkce-humanizer** (Büşra Begçecanlı, MIT lisansı, v3.2)
projesinden uyarlanmıştır; hasta bilgilendirme metnine ve sağlık mevzuatına göre daraltılmış
ve değiştirilmiştir. Değişiklikler en sondaki "Alınmayan kurallar" bölümünde gerekçeleriyle yazılıdır.

**Her onarımdan önce `mevzuat.md` → B ve C'ye bak.** Bir onarım bir çekinceyi, onaylı bir
kalıbı, bir atfı ya da bir sayıyı kaldıracaksa, onarım yapılmaz ve iz raporda "bilerek
dokunmadım" olarak kalır.

Betik (`scripts/denetle.py`) 1–12'yi sayar; 13–17'yi okuyarak bulursun.

---

## Baskın izler

### 1. Noktalı virgül
Türkçe yapay zekâ çıktısının en sık izi: İngilizce "; however / ; also" mantığının çevirisi.
- **Onarım:** İki cümleye böl. İkinci cümle bağlaçla başlamasın, bağlaç gerekiyorsa cümlenin
  içine al. İki kısım gerçekten tek düşünceyse virgül ve bağlaçla birleştir.
- Örnek: "Tedavinin süresi hastadan hastaya değişir; belirtiler gerilediğinde tedavi hemen
  sonlandırılmaz." → "Tedavinin süresi hastadan hastaya değişir. Belirtiler gerilediğinde
  tedavi hemen sonlandırılmaz."
- Kaynak listesindeki (`refs`) noktalı virgüller bibliyografik biçimdir, dokunulmaz.

### 2. Karşıtlık bağlacından önce virgül
", ancak", ", ama", ", fakat", ", lakin": İngilizce "but" öncesi virgül kuralının çevirisi.
- **Onarım:** Virgülü kaldır. "…en sık kullanılan tanımdır, ancak çalışmalar arasında
  farklılıklar bulunmaktadır." → "…en sık kullanılan tanımdır ancak çalışmalar arasında
  farklılıklar vardır."

### 3. "X değil, Y" ailesi
"sadece X değil aynı zamanda Y", "X'in ötesinde Y", "salt X değil Y meselesi",
"… anlamına gelmez; … gösterir". Retorik bir karşıtlık kurup asıl söyleneni geciktirir.
- **Onarım:** Y'yi doğrudan söyle. X gerçekten yaygın bir yanlış anlamaysa ve hasta için
  önemliyse, X'i ayrı bir olgu cümlesi olarak yaz.
- Örnek: "Tedaviye dirençli depresyon, tedavinin bittiği anlamına gelmez; değerlendirmenin
  daha ayrıntılı yapılması gerektiğini gösterir." → "Tedaviye dirençli depresyonda
  değerlendirme daha ayrıntılı yapılır ve sonraki basamak seçenekler gözden geçirilir."

### 4. "-mektedir / -maktadır" yığını
Bir paragrafta üç ya da daha fazla.
- **Onarım:** Bir kısmını geniş zamana çevir: "yer almaktadır" → "yer alır", "kullanılmaktadır"
  → "kullanılır", "bulunmaktadır" → "vardır".
- **Dokunma:** "bildirilmiştir" (geçmiş zaman, çekince). Onaylı notlardaki
  "uygulanmamaktadır", "verilmemektedir" (`mevzuat.md` → C).

### 5. Bürokratik bağlaç yığını
"bu bağlamda", "söz konusu", "bu doğrultuda", "bu çerçevede", "öte yandan", "bunun yanı sıra".
- **Onarım:** Gerçek mantıksal bağı yaz ("çünkü", "bu nedenle", "oysa") ya da sil.

### 6. Boş önem ve boş kapanış
"kritik bir rol oynar", "önemli bir rol üstlenir", "büyük önem taşır", "hayati öneme sahiptir",
"vazgeçilmezdir", "göz ardı edilmemelidir", "unutulmamalıdır".
- **Onarım:** Sil; paragraf önceki olguda bitsin. Bilgi taşıyorsa somut olguya çevir.
- **Mevzuat bağı:** Önem abartısı tedavi bağlamında kesinlik iddiasına kayar (A3).

### 7. Boş değerlendirici sıfat
"eşsiz", "benzersiz", "paha biçilmez", "kapsamlı", "bütüncül", "yenilikçi", "son teknoloji".
- **Onarım:** Sil.
- **Mevzuat bağı:** Muayenehane ya da hekim için kullanılmışsa üstünlük iddiasıdır (A1, A4).

### 8. Vurgu doldurucuları
"tam da", "gerçekten de", "aslında", "esasen", "nihayetinde", "kesinlikle", "bir bakıma",
"gerçek anlamda", cümle başında "işte", dolgu olan "sonuç olarak".
- **Onarım:** Sil. "Kesinlikle" ayrıca kesinlik iddiası riski taşır (A3).

## İkincil izler

### 9. "Şudur:" kalıbı
"Kesin olan şudur: …", "Ortaya çıkan tablo şudur: …".
- **Onarım:** İki noktayı kaldır, cümleyi düz kur.

### 10. Cümle içi iki nokta ile açıklama
Bir paragrafta iki ya da daha fazla. Liste girişleri ("şunlardır:") ve `<b>Etiket:</b>`
biçimindeki liste etiketleri bu sayfaların yapısıdır, sayılmaz.

### 11. Slash ayırıcı
"hasta/yakını", "ilaç/terapi" → "hasta veya yakını". Adresteki "No:4/107" gibi sayılar hariç.

### 12. Uzun çizgi (—)
Cümle içi ara söz için. **Onarım:** Virgül ya da parantez, ya da cümleyi böl.

### 13. Cümle monotonluğu
Paragraftaki cümlelerin hepsi 20–25 kelime, arada kısa cümle yok.
- **Onarım:** En uzun cümleyi böl. **Yarım cümle üretme** ("Bitti." gibi); kısa cümle de
  özne ve yüklem taşır.

### 14. Eş anlamlı rotasyonu
Aynı şeye bir paragrafta üç farklı ad. Tıbbi metinde özellikle zararlı: "TMS", "manyetik
uyarım", "beyin stimülasyonu" aynı paragrafta okuru üç ayrı yöntem sandırır.
- **Onarım:** Bir terim seç, onu kullan.

### 15. Zorlama üçlü
Üç öğe arasında gerçek fark yoksa dolgu. **Onarım:** Anlamın gerektirdiği sayıda öğe.

### 16. Kanca açılış, dramatik cümle, retorik soru, ünlem
Sitenin dil rehberi bunları zaten yasaklıyor (`CLAUDE.md` → *Dil rehberi*). Hasta
bilgilendirmede gövdede soru işareti ve ünlem olmaz. Blogda ölçülü retorik soru serbest.

### 17. Sayfalar arası kalıp tekrarı
Birden fazla sayfada aynı cümle ya da aynı açılış. Betik birden fazla dosyayla çalıştığında
bunları listeler.
- **Bilinçli tekrarlar iz değildir:** acil kalıbı, psikoterapi kalıbı, yasal uyarı
  (`mevzuat.md` → C). Tutarlılık için her sayfada aynı olmaları gerekir.

### 18. Ödünç otorite
"Çalışmalar gösteriyor", "uzmanlar belirtiyor", "kılavuzlarda önerilir" ama kaynak yok.
Bu sitede mevzuat konusudur: `mevzuat.md` → A10. Yazım izi diye çerçeveyi silmek yasaktır;
çözüm atıftır.

---

## Alınmayan kurallar (turkce-humanizer'dan farklar)

| turkce-humanizer kuralı | Burada | Neden |
|---|---|---|
| Pasif cümleleri aktife çevir | **Uygulanmaz** (tıbbi bilgide) | Dil rehberi: tıbbi bilgi nesnel ve edilgen. Aktife çevirmek ya hekimi özne yapar (kanıt kişisel görüşe döner) ya da tedaviyi özne yapar ("TMS iyileştirir": kesinlik iddiası) |
| Birinci çoğul ekle ("görüyoruz") | **Uygulanmaz** | Tek hekim; "biz" yok (A9) |
| Retorik soru ekle | **Uygulanmaz** (hasta bilgilendirmede) | Dil rehberi yasaklıyor |
| Öz-düzeltme ekle ("daha doğrusu", "aslında") | **Uygulanmaz** | Hasta bilgilendirmede kararsızlık izlenimi verir |
| Devrik cümle yerleştir | **Uygulanmaz** (hasta bilgilendirmede) | Tıbbi metinde netliği azaltır |
| Konuşma bağlaçları ekle ("Zaten", "Meğer") | **Uygulanmaz** (hasta bilgilendirmede) | Register'a uymaz |
| Bağlaçla başlayan cümle **mutlak yasak** | **Mutlak değil** | Bilinçli, kalın uyarı cümleleri korunur ("Ancak psikoterapi için…"). Dolgu olanlar birleştirilir |
| "-mektedir"leri azalt | **Kısmen** | "bildirilmiştir" ve onaylı notlar dokunulmaz |
| Edebi yazar ritmi (Tanpınar, Ortaylı…) | **Uygulanmaz** | Hedef sade, açık, ölçülü hasta metni |
| Her seferinde tür ve profil sorusu | **Sorulmaz** | Tür dosya yolundan belli; bu site için sabit |
