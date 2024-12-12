# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

# buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method  

# buat minimal 2 objek dari setiap child class. 

class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def cetak(self):
        print(f"Binatang ini adalah : {self.nama}")
        print(f"Makanan nya yaitu : {self.makanan}")
        print(f"Hidup di tempat : {self.hidup}")
        print(f"Berkembang Biak dengan cara : {self.berkembang_biak}")
        
hewan1 = animal("Harimau", "Daging", "Alam liar", "Melahirkan" )
hewan1.cetak()

print()