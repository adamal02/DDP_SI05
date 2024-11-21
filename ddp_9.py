print('\n--- Celcius Ke Fahrenheit---')
def celcius_ke_fahrenheait (celcius):
    print(celcius * 9/5 + 32)
celcius_ke_fahrenheait(0)
celcius_ke_fahrenheait(100)

print('\n--- menentukan bilangan genap---')
def is_genap (genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print('\n--- ketrangan lulus atau tidak lulus ---')
def hasil (nilai):
    if nilai >= 80:
        print("Lulus")
    else:
        print("Gagal")
hasil(80)
hasil(60)

print('\n--- mencetak nilai ganjil ---')
def nilai (ganjil):
    for i in range(1, ganjil+1, 2):
        print(i, end=",")
nilai(20)
