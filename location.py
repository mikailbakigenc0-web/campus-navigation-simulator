class Location:
    def __init__(self,isim,tur,konum):
        self.isim = isim
        self.tur = tur
        self.konum = konum
    def  __str__(self):
        return f"{self.isim} ({self.tur}) - {self.konum}"
