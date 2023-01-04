hasil_akhir = [
    {'nama':'reza', 'nilai':70},
    {'nama':'ciut', 'nilai':63},
    {'nama':'dian', 'nilai':80},
    {'nama':'bayu', 'nilai':40}
]

def lulus_saja(data):
    for nilai in data:
        if nilai ['nilai'] > 65:
            print(nilai['nama'])
            
lulus_saja(hasil_akhir)