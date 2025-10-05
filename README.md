# JSON'dan Excel'e Dönüştürücü

JSON dosyalarını Excel formatına dönüştürmek için geliştirilmiş güçlü bir Python aracı. Kapsamlı hata yönetimi ve profesyonel çıktı formatlaması ile donatılmıştır.

## Genel Bakış

Bu komut satırı aracı, JSON veri yapılarının Excel (.xlsx) formatına sorunsuz dönüştürülmesini sağlar. Hem tek nesneleri hem de nesne dizilerini destekler. Dönüştürücü, veri bütünlüğünü korurken işleme durumu ve çıktı konumu hakkında net geri bildirim sağlar.

## Özellikler

### Temel İşlevsellik

- **Evrensel JSON Desteği**: Hem dizi tabanlı hem de tek nesne JSON yapılarını işler
- **Akıllı Veri İşleme**: İç içe nesneleri ve dizileri optimal Excel gösterimi için otomatik düzleştirir
- **Güçlü Hata Yönetimi**: Açıklayıcı hata mesajları ile kapsamlı doğrulama
- **Çıktı Yönetimi**: Zaman damgalı çıktılarla organize dosya yapısı
- **Çapraz Platform Uyumluluğu**: Windows, macOS ve Linux'ta sorunsuz çalışır

### Teknik Özellikler

- **Giriş Formatı**: Geçerli JSON dosyaları (.json)
- **Çıkış Formatı**: Excel Çalışma Kitabı (.xlsx)
- **Kodlama Desteği**: Uygun karakter işleme ile UTF-8
- **Bellek Verimli**: Büyük JSON dosyalarını bellek taşması olmadan akışla işler

## Ön Koşullar

### Sistem Gereksinimleri

- Python 3.7 veya üzeri
- 50MB kullanılabilir disk alanı
- Çalışma dizininde okuma/yazma izinleri

### Bağımlılıklar

```bash
pip install -r requirements.txt
```

**Gerekli paketler:**

- `pandas>=1.3.0` - Veri manipülasyonu ve Excel dışa aktarımı
- `openpyxl>=3.0.0` - Excel dosya formatı desteği

## Kurulum

1. **Proje dosyalarını** yerel makinenize kopyalayın veya indirin
2. **Proje dizinine** gidin
3. **Bağımlılıkları yükleyin**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Kurulumu doğrulayın**:
   ```bash
   python main.py --help
   ```

## Kullanım

### GUI (Önerilen Kolay Yol)

```bash
python main.py --gui
```

- "JSON Dosyası" alanından giriş `.json` dosyanızı seçin.
- "Çıktı (xlsx)" için kaydetme yerini belirleyin veya varsayılanı kullanın.
- "Dönüştür" tuşuna basın.

### Temel Kullanım

```bash
python main.py <giris_json_dosyasi>
```

### Örnekler

```bash
# Basit bir JSON dosyasını dönüştür
python main.py data/musteriler.json

# Mutlak yol ile dönüştür
python main.py /home/kullanici/belgeler/api_yaniti.json

# İç içe JSON yapısını dönüştür
python main.py karmasik_veri.json
```

### Çıktı Yapısı

```
proje_koku/
├── main.py
├── requirements.txt
├── input/
│   └── dosyaniz.json
└── output/
    ├── donusturulen_YYYYAAGG_SSDDSS.xlsx
    └── isleme_kaydi.txt
```

## Hata Yönetimi

Uygulama, yaygın senaryolar için kapsamlı hata yönetimi sağlar:

| Hata Türü            | Açıklama                                   | Çözüm                                              |
| -------------------- | ------------------------------------------ | -------------------------------------------------- |
| **Dosya Bulunamadı** | JSON dosyası belirtilen yolda mevcut değil | Dosya yolunu ve izinleri doğrulayın                |
| **Geçersiz JSON**    | Hatalı JSON syntax'ı                       | JSON yapısını çevrimiçi araçlarla doğrulayın       |
| **İzin Reddedildi**  | Yetersiz dosya sistemi izinleri            | Okuma/yazma izinlerini kontrol edin                |
| **Bellek Hatası**    | Dosya mevcut bellek için çok büyük         | Akış modunu kullanın veya sistem belleğini artırın |

### Yaygın Hata Mesajları

```bash
❌ Hata: JSON dosyası 'veri.json' konumunda bulunamadı
❌ Hata: Geçersiz JSON formatı - 15. satırdaki syntax'ı kontrol edin
❌ Hata: İzin reddedildi - Çıktı dizinine yazılamıyor
✅ Başarılı: Dosya başarıyla 'cikti/donusturulen_20241201_143022.xlsx' konumuna dönüştürüldü
```

## Gelişmiş Konfigürasyon

### Ortam Değişkenleri

```bash
# Özel çıktı dizini ayarla
export JSON_CONVERTER_OUTPUT_DIR="/ozel/cikti/yolu"

# Debug modunu etkinleştir
export JSON_CONVERTER_DEBUG=true

# Maksimum dosya boyutunu ayarla (MB)
export JSON_CONVERTER_MAX_SIZE=500
```

### Komut Satırı Seçenekleri

```bash
# Özel çıktı dosya adı belirt
python main.py giris.json --output ozel_ad.xlsx

# Ayrıntılı kayıtlamayı etkinleştir
python main.py giris.json --verbose

# Çıktı dizini ayarla
python main.py giris.json --output-dir /ozel/yol
```

## Veri İşleme Mantığı

### JSON Yapı İşleme

- **Diziler**: Her öğe Excel'de bir satır olur
- **İç İçe Nesneler**: Nokta notasyonu kullanılarak düzleştirilir (örn. `kullanici.adres.sehir`)
- **Karışık Türler**: Uygun Excel veri türlerine otomatik dönüştürülür
- **Null Değerler**: Boş hücreler olarak temsil edilir

### Excel Formatlama

- **Başlıklar**: Kalın formatla otomatik boyutlandırılır
- **Veri Türleri**: Korunur (sayılar, tarihler, metinler, boolean'lar)
- **Kodlama**: Uluslararası karakterler için UTF-8 desteği
- **Çalışma Sayfaları**: Açıklayıcı adla tek sayfa

## Performans Metrikleri

| Dosya Boyutu | İşleme Süresi | Bellek Kullanımı |
| ------------ | ------------- | ---------------- |
| < 1MB        | < 1 saniye    | < 50MB           |
| 1-10MB       | 1-5 saniye    | 50-200MB         |
| 10-100MB     | 5-30 saniye   | 200-500MB        |
| > 100MB      | Akış modu     | < 1GB            |

## Sorun Giderme

### Yaygın Sorunlar

**S: "ModuleNotFoundError: No module named 'pandas'"**

```bash
C: Gerekli bağımlılıkları yükleyin: pip install -r requirements.txt
```

**S: "PermissionError: [Errno 13] Permission denied"**

```bash
C: Yönetici ayrıcalıklarıyla çalıştırın veya dosya izinlerini kontrol edin
```

**S: "JSONDecodeError: Expecting ',' delimiter"**

```bash
C: JSON syntax'ını jsonlint.com veya benzer araçlarla doğrulayın
```

## Geliştirme ve Katkı

### Proje Yapısı

```
json-excel-donusturucu/
├── input/
│   ├── test_donusturucu.py
│   └── test_verisi/
├── output/
│   └── API.md
├── main.py               # CLI giriş noktası
├── requirements.txt
└── README.md
```

### Katkı Kılavuzu

1. **Fork** yapın
2. **Özellik dalı** oluşturun (`git checkout -b ozellik/harika-ozellik`)
3. **Değişikliklerinizi** commit edin (`git commit -m 'Harika özellik ekle'`)
4. **Dala** push yapın (`git push origin ozellik/harika-ozellik`)
5. **Pull Request** açın

### Kod Standartları

- **PEP 8** uyumluluğu Python kod stili için
- **Tür ipuçları** tüm fonksiyon parametreleri ve dönüş değerleri için
- **Docstring'ler** tüm genel fonksiyonlar ve sınıflar için
- **Birim testleri** tüm yeni özellikler için

### Destek Kanalları

- **GitHub Issues**: Hata raporları ve özellik istekleri

### Sürümleme

- **Mevcut Sürüm**: 2.1.0
- **Uyumluluk**: Python 3.7+
- **Son Güncelleme**: Aralık 2024

---
