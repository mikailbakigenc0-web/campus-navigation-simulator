# campus-navigation-simulator
Terminal tabanlı, veri yapıları destekli akıllı kampüs yönetim sistemi.

Bu proje, temel veri yapılarını (Stack, Queue, Linked List, Tree) gerçek bir senaryo üzerinde uygulayan bir kampüs simülasyon sistemidir. Öğrenci işleri kuyruğu, ziyaret geçmişi, işlem geri alma ve kampüs hiyerarşisi gibi gerçek hayat problemleri veri yapılarıyla çözülmüştür.

## 🛠️ Kullanılan Veri Yapıları

| Veri Yapısı | Sınıf | Kullanım Amacı |
|---|---|---|
| Stack | `UndoStack` | Son işlemi geri alma (Ctrl+Z mantığı) |
| Queue | `ServiceQueue` | Öğrenci işleri sırası (FIFO) |
| Linked List | `VisitHistoryLinkedList` | Ziyaret edilen yerlerin geçmişi |
| Tree | `CampusTree` | Kampüs hiyerarşik yapısı |

##  Özellikler

- Kampüs hiyerarşik haritasını görüntüleme (Üniversite → Fakülte → Bina → Kat)
- Öğrenci işleri kuyruğuna sıra alma
- Sıradaki öğrenciyi işleme alma
- Son yapılan işlemi geri alma
- Gezilen yerlerin geçmişini görüntüleme
- Kampüs alanlarında arama yapma
- Binalar, bölümler, kantinler ve laboratuvarları listeleme

## 📁 Dosya Yapısı

```
kampus-navigasyon/
├── main.py              # Ana program ve menü
├── veri_yapilari.py     # UndoStack, ServiceQueue, VisitHistoryLinkedList, CampusTree
├── kampus.py            # Kampüs verileri ve ağaç yapısı
├── campus_manager.py    # Sistem yönetici sınıfı
├── location.py          # Konum sınıfı
└── README.md
```

## ⚙️ Kurulum ve Çalıştırma

Python 3 yeterli, harici kütüphane gerekmez.

```bash
python main.py
```

## 📷 Örnek Çıktı

```
🏫 İstanbul Teknik Üniversitesi
 📚 Mühendislik Fakültesi
  🏢 Bilgisayar Mühendisliği
   📋 Kat 1 - Derslikler
   🔬 Kat 2 - Laboratuvarlar
   💼 Kat 3 - Akademik Ofisler
  🏢 Elektrik-Elektronik Mühendisliği
 📚 Fen-Edebiyat Fakültesi
 📚 İktisat Fakültesi
 🏛️  Ortak Alanlar
```

## 💡 Teknik Detaylar

- **Dil:** Python 3
- **Paradigma:** OOP (Nesne Yönelimli Programlama)
- **Harici Kütüphane:** Yok (saf Python)
- **Veri Kalıcılığı:** JSON
