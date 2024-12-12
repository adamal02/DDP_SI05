from animals import *

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.jenis = jenis
        
    def cetak_ular(self):
        super().cetak()
        print(f"Warna ular ini adalah : {self.warna}")
        print(f"Jenis ular ini adalah : {self.jenis}")

print("\n ====== class child ular ======")    
mamba = ular("Ular Mamba", "Burung", "Pohon", "Bertelur", "Hitam dan Hijau", "Berbisa")    
mamba.cetak_ular()

print()

king_kobra = ular("Ular King Kobra", "Burung", "Hutan", "Bertelur", "coklat", "Berbisa")    
king_kobra.cetak_ular()