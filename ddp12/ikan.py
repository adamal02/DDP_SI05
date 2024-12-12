from animals import *

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.jenis = jenis
        
    def cetak_ikan(self):
        super().cetak()
        print(f"Warna ikan ini adalah : {self.warna}")
        print(f"Jenis ikan ini adalah : {self.jenis}")

print("\n ====== class child ikan ======")    
koi = ikan("Ikan Koi", "Pelet", "Air Aquarium", "Bertelur", "Merah dan Putih", "Ikan hias")    
koi.cetak_ikan()

print()

arwana = ikan("Ikan Arwana", "Ikan Kecil", "Air Sungai", "Bertelur", "Merah", "Ikan Predator")    
arwana.cetak_ikan()