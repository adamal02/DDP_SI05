from gempa import*

# membuat objek gempa dengan lokasi dan skala
gempa1 = gempa("banten", 1.2)
gempa2 = gempa("palu", 6.1)
gempa3 = gempa("cianjur", 5.6)
gempa4 = gempa("jayapura", 3.3)
gempa5 = gempa("garut", 4.0)

# info gempa
print("## gempa bumi Informasi ##")
print()
#memanggil method
gempa1.dampak()
print()
gempa2.dampak()
print()
gempa3.dampak()
print()
gempa4.dampak()
print()
gempa5.dampak()