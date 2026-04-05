class UndoStack:
    def __init__(self):
        self.items = []

    def push(self, item):          # ← __init__ ile aynı hizada!
        self.items.append(item)

    def pop(self):                 # ← __init__ ile aynı hizada!
        return self.items.pop()


class ServiceQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):       # Queue'da push değil enqueue denir
        self.items.append(item)

    def dequeue(self):             # Queue'da pop değil dequeue denir
        return self.items.pop(0)   # ← baştan çıkar (0. indeks)


class Dugum:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None


class VisitHistoryLinkedList:
    def __init__(self):
        self.bas = None

    def ekle(self, veri):
        yeni = Dugum(veri)         # ← küçük v, parantez ile
        yeni.sonraki = self.bas
        self.bas = yeni
class CampusTree:
    def __init__(self,isim):
        self.isim = isim
        self.öğrenciler =[]
    def ogrenci_ekle(self,öğrenci):
        self.öğrenciler.append(öğrenci)

      
    def yazdir(self,girinti=0):
        print(" " * girinti + self.isim)
        for ogrenci in self.öğrenciler:
            ogrenci.yazdir(girinti +1)
