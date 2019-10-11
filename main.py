nama = 'friesca ayazya'
program = 'Gerak Lurus'

print(f'Program {program} oleh (nama)')

def hitung_kecepatan(jarak, waktu):
    kecepatan = jarak / waktu
    print(f'Jarak = {jarak/1000}km ditempuh dalam waktu = {waktu/60}menit')
    print(f'sehingga kecepatan = {kecepatan} m/s')
    return kecepatan

#jarak = 1000
#waktu = 5* 60
keceptan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan (3000, 70 * 60)

#TUGAS: buat fungsi  _APA_SAJA_YANG_KALIAN_TAHU
#DAN GUNAKAN

def hitung_arus(tegangan, hambatan):
    arus = tegangan / hambatan
    print(f'tegangan = {tegangan/30}volt diperoleh dari hambatan = {hambatan/15}ohm')
    print(f'sehingga arus = {arus} ampere')


# tegangan = 30
# hambatan = 15
arus = hitung_arus(30, 15)
arus = hitung_arus(60, 30)
