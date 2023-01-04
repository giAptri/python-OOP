gorengan = ('bakwan','combro','misro')          
sop = ('sop iga','sop buntut','sop kaki')
nasi = ('nasi uduk','nasi goreng','nasi rames')
#membuat tuple di dalam tuple
makanan = (gorengan, sop, nasi)
# index      0        1     2

#cetak gorengan dari variable makanan di keluarkan dari buka tutup kurung
#for i in makanan[0]:
#    print(i)
    
#cetak sop buntut
# for i in makanan[1]:
print(sop[1])

#cetak nasi remes
print(makanan[2][2])

#cetak seluruhnya dan pastikan keluar dari buka tutp kurung
for i in makanan:
    for detail_makanan in i:
        print(detail_makanan)