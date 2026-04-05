import json
from kampus import kampus_olustur, binalar, bolumler, laboratuvarlar, kantinler
from veri_yapilari import UndoStack, ServiceQueue, VisitHistoryLinkedList, CampusTree

def veri_yukle():
    try:
        with open('veri.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

islem_gecmisi = UndoStack()
kuyruk = ServiceQueue()
ziyaret_gecmisi = VisitHistoryLinkedList()
kampus = kampus_olustur()

# Ana Menü
while True:
    print("\n1. Kampüs haritasını göster")
    print("2. Kuyruğa öğrenci ekle")
    print("3. Sıradaki öğrenciyi işle")
    print("4. Kampüs listelerini göster")
    print("5. Son işlemi geri al")
    print("6. Gezilen yerleri göster")
    print("7. Yer ara")
    print("0. Çıkış")

    secim = input("Seçim: ")

    if secim == "0":
        break

    if secim == "1":
        kampus.yazdir()

    if secim == "2":
        isim = input("Öğrenci Adı: ")
        kuyruk.enqueue(isim)
        islem_gecmisi.push(f"Kuyruğa eklendi: {isim}")
        print(f"{isim} kuyruğa eklendi!")

    if secim == "3":
        ogrenci = kuyruk.dequeue()
        if ogrenci:
            islem_gecmisi.push(f"İşleme alındı: {ogrenci}")
            print(f"{ogrenci} işleme alındı!")
        else:
            print("Kuyruk boş!")

    if secim == "4":
        print("\nBinalar:", binalar)
        print("Bölümler:", bolumler)
        print("Kantinler:", kantinler)
        print("Laboratuvarlar:", laboratuvarlar)

    if secim == "5":
        geri = islem_gecmisi.pop()
        if geri:
            print(f"Geri alındı: {geri}")
        else:
            print("Geri alınacak işlem yok!")

    if secim == "6":
        gecmis = ziyaret_gecmisi.bas
        if gecmis is None:
            print("Henüz yer gezilmedi!")
        while gecmis:
            print(gecmis.veri)
            gecmis = gecmis.sonraki

    if secim == "7":
        aranan = input("Aranacak yer: ")
        bulunanlar = [b for b in binalar if aranan.lower() in b.lower()]
        print(bulunanlar if bulunanlar else "Bulunamadı!")
