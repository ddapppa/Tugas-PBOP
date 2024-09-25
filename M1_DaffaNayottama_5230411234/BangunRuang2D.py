# Perhitungan Segitiga (2D)
def segitiga(alas, tinggi, sisi1, sisi2, sisi3):
    luas = 0.5 * alas * tinggi
    keliling = sisi1 + sisi2 + sisi3
    return luas, keliling

alas_segitiga = 6
tinggi_segitiga = 4
sisi1_segitiga = 5
sisi2_segitiga = 6
sisi3_segitiga = 7
luas_segitiga, keliling_segitiga = segitiga(alas_segitiga, tinggi_segitiga, sisi1_segitiga, sisi2_segitiga, sisi3_segitiga)

print(f"Luas segitiga: {luas_segitiga}")
print(f"Keliling segitiga: {keliling_segitiga}")
