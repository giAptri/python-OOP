buah = ["mangga","jeruk","apel","melon","apel"]
#index

#untuk mengaksesnya menggunakan indek
#index di mulai dari 0

#cetak mangga
print(buah[0])

#menambah list menggunakan append
buah.append("pisang")
print(buah)

#mengubah list
#variable (nilai indexnya)
buah[0]="jambu"
print(buah)

#menghapus list
del buah[1]
print(buah)

#mengambil data akhir menggunakan pop
print(buah.pop())

#mengetahui jumlah data dari list menggnakan len
print(len(buah))

#menyisipkan data sesuai yang di inginkan
#menggunakan insert
buah.insert(1,"strawberry")
print(buah)

#mengambil seluruh data di list
#menggunakan perulangan for
for i in buah:
    print(i)
    
