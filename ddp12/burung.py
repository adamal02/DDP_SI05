from animals import *

class burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi
        
    def cetak_burung(self):
        super().cetak()
        print(f"Burung ini berbulu warna : {self.jenis_bulu}")
        print(f"Burung ini memiliki bunyi yang : {self.bunyi}")

print("\n ====== class child burung ======")        
kenari = burung("Burung Kenari", "Biji-bijian", "Ternakan", "Bertelur", "kuning", "nyaring")
kenari.cetak_burung()

print()

bangau = burung("Burung Bangau", "Ikan", "Sungai", "Bertelur", "Putih", "ngok ngok")
bangau.cetak_burung()


        