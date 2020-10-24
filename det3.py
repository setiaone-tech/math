baris1=[a,b,c]
baris2=[d,e,f]
baris3=[g,h,i]

print(baris1)
print(baris2)
print(baris3)


det = (baris1[0]*baris2[1]*baris3[2] + baris1[1]*baris2[2]*baris3[0] + baris1[2]*baris2[0]*baris3[1] - baris3[0]*baris2[1]*baris1[2] - baris3[1]*baris2[2]*baris1[0] - baris3[2]*baris2[0]*baris1[1])
print("Hasil Determinan Matriks:",det)