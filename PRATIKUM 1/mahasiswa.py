#membat class degan kata kunci "class"

class mahasiswa:
    #konstruktor
    def __init__(self, nama, nim, rombel):
        ##vaiabel objek
        self.nama = nama
        self.nim = nim
        self.rombel = rombel        
    #method
    def lulus(self, nilai):
        if (nilai>90):
            print("lulus")
        else:
            print("tidak lulus")
    #class ,ahasiswa memliki 3 atribut dan 1 fungsi
    
    def cetak(self):
        print("NAMA : ", self.nama)
        print("NIM : ", self.nim)
        print("ROMBEL : ", self.rombel)
        
    
#membuat object
mahasiswa1 = mahasiswa("argya", "0110222241", "TI-05")

#mencetak atirbut
mahasiswa1.cetak()
mahasiswa1.lulus(95)
    
#objek ke-2
mahasiswa2 = mahasiswa("sadam", "627262723326", "hati gia")


#mencetak atribut
mahasiswa2.cetak()
mahasiswa2.lulus(85)
    