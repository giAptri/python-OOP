def pilihan(i):
    switcher = {
        1:'---Cuaca Hujan---',
        2:'---Cuaca Adem---'
    }
    return switcher.get(i, "Masukan Pilihan Yang Benar")

print("1. Hujan")
print("2. Adem")
nomor = int(input("Masukan Pilihan: "))
cuaca = pilihan(nomor)
print(cuaca)

if nomor==1:
    print("Karena Cuaca Hujan. Maka, Kuliah Naik Gocar")
if nomor==2:
    print("Karena Cuaca Adem. Maka, Kuliah Naik Motor")