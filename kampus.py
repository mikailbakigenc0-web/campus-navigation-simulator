from veri_yapilari import CampusTree

def kampus_olustur():
    kampus = CampusTree("🏫 İstanbul Teknik Üniversitesi")

    # --- MÜHENDİSLİK FAKÜLTESİ ---
    muhendislik = CampusTree("📚 Mühendislik Fakültesi")

    bilgisayar = CampusTree("🏢 Bilgisayar Mühendisliği")
    bilgisayar.ogrenci_ekle(CampusTree("📋 Kat 1 - Derslikler"))
    bilgisayar.ogrenci_ekle(CampusTree("🔬 Kat 2 - Laboratuvarlar"))
    bilgisayar.ogrenci_ekle(CampusTree("💼 Kat 3 - Akademik Ofisler"))

    elektrik = CampusTree("🏢 Elektrik-Elektronik Mühendisliği")
    elektrik.ogrenci_ekle(CampusTree("📋 Kat 1 - Derslikler"))
    elektrik.ogrenci_ekle(CampusTree("🔬 Kat 2 - Elektronik Lab"))

    makine = CampusTree("🏢 Makine Mühendisliği")
    makine.ogrenci_ekle(CampusTree("📋 Kat 1 - Derslikler"))
    makine.ogrenci_ekle(CampusTree("⚙️  Kat 2 - Atölye"))

    insaat = CampusTree("🏢 İnşaat Mühendisliği")
    insaat.ogrenci_ekle(CampusTree("📋 Kat 1 - Derslikler"))
    insaat.ogrenci_ekle(CampusTree("🧱 Kat 2 - Malzeme Lab"))

    muhendislik.ogrenci_ekle(bilgisayar)
    muhendislik.ogrenci_ekle(elektrik)
    muhendislik.ogrenci_ekle(makine)
    muhendislik.ogrenci_ekle(insaat)

    # --- FEN-EDEBİYAT FAKÜLTESİ ---
    fen = CampusTree("📚 Fen-Edebiyat Fakültesi")

    matematik = CampusTree("🏢 Matematik Bölümü")
    matematik.ogrenci_ekle(CampusTree("📋 Kat 1 - Derslikler"))
    matematik.ogrenci_ekle(CampusTree("💻 Kat 2 - Bilgisayar Lab"))

    fizik = CampusTree("🏢 Fizik Bölümü")
    fizik.ogrenci_ekle(CampusTree("📋 Kat 1 - Derslikler"))
    fizik.ogrenci_ekle(CampusTree("🔭 Kat 2 - Fizik Lab"))

    kimya = CampusTree("🏢 Kimya Bölümü")
    kimya.ogrenci_ekle(CampusTree("📋 Kat 1 - Derslikler"))
    kimya.ogrenci_ekle(CampusTree("⚗️  Kat 2 - Kimya Lab"))

    fen.ogrenci_ekle(matematik)
    fen.ogrenci_ekle(fizik)
    fen.ogrenci_ekle(kimya)

    # --- İKTİSAT FAKÜLTESİ ---
    iktisat = CampusTree("📚 İktisat Fakültesi")

    ekonomi = CampusTree("🏢 Ekonomi Bölümü")
    ekonomi.ogrenci_ekle(CampusTree("📋 Kat 1 - Derslikler"))
    ekonomi.ogrenci_ekle(CampusTree("📊 Kat 2 - Araştırma Odaları"))

    isletme = CampusTree("🏢 İşletme Bölümü")
    isletme.ogrenci_ekle(CampusTree("📋 Kat 1 - Derslikler"))

    iktisat.ogrenci_ekle(ekonomi)
    iktisat.ogrenci_ekle(isletme)

    # --- ORTAK ALANLAR ---
    ortak = CampusTree("🏛️  Ortak Alanlar")
    ortak.ogrenci_ekle(CampusTree("📖 Merkez Kütüphane"))
    ortak.ogrenci_ekle(CampusTree("🍽️  Ana Yemekhane"))
    ortak.ogrenci_ekle(CampusTree("☕ Kafeterya"))
    ortak.ogrenci_ekle(CampusTree("⚽ Spor Salonu"))
    ortak.ogrenci_ekle(CampusTree("🏥 Sağlık Merkezi"))
    ortak.ogrenci_ekle(CampusTree("📝 Öğrenci İşleri"))

    kampus.ogrenci_ekle(muhendislik)
    kampus.ogrenci_ekle(fen)
    kampus.ogrenci_ekle(iktisat)
    kampus.ogrenci_ekle(ortak)

    return kampus


# Ana veri listeleri
binalar = [
    "Bilgisayar Mühendisliği Binası",
    "Elektrik-Elektronik Mühendisliği Binası",
    "Makine Mühendisliği Binası",
    "İnşaat Mühendisliği Binası",
    "Fen-Edebiyat Binası",
    "İktisat Fakültesi Binası",
    "Merkez Kütüphane",
    "Yemekhane",
    "Spor Salonu",
    "Sağlık Merkezi",
    "Öğrenci İşleri"
]

bolumler = [
    "Bilgisayar Mühendisliği",
    "Elektrik-Elektronik Mühendisliği",
    "Makine Mühendisliği",
    "İnşaat Mühendisliği",
    "Matematik",
    "Fizik",
    "Kimya",
    "Ekonomi",
    "İşletme"
]

kantinler = [
    "A Blok Kantin",
    "Merkez Kafeterya",
    "Kütüphane Kafesi",
    "Mühendislik Binası Kantin"
]

laboratuvarlar = [
    "Bilgisayar Lab 1",
    "Bilgisayar Lab 2",
    "Elektronik Lab",
    "Fizik Lab",
    "Kimya Lab",
    "Malzeme Lab",
    "Atölye"
]
