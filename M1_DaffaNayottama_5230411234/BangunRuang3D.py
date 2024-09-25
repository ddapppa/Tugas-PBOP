# Perhitungan Balok (3D)
def balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return volume, luas_permukaan

panjang_balok = 10
lebar_balok = 5
tinggi_balok = 8
volume_balok, luas_permukaan_balok = balok(panjang_balok, lebar_balok, tinggi_balok)

print(f"Volume balok: {volume_balok}")
print(f"Luas permukaan balok: {luas_permukaan_balok}")
