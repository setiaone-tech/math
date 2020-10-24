nama=input('\nNama Matriksmu = ')

print('\n         " Matriks',nama,'"')

s=nama



e11=int(input('Masukkan angka pada baris 1 kolom 1 ='))

e21=int(input('Masukkan angka pada baris 2 kolom 1 ='))

e31=int(input('Masukkan angka pada baris 3 kolom 1 ='))

e12=int(input('Masukkan angka pada baris 1 kolom 2 ='))

e22=int(input('Masukkan angka pada baris 2 kolom 2 ='))

e32=int(input('Masukkan angka pada baris 3 kolom 2 ='))

e13=int(input('Masukkan angka pada baris 1 kolom 3 ='))

e23=int(input('Masukkan angka pada baris 2 kolom 3 ='))

e33=int(input('Masukkan angka pada baris 3 kolom 3 ='))



print('    |',e11, e12, e13, '|')

print(s,' =|',e21, e22, e23, '|')

print('    |',e31, e32, e33, '|')



#determinan

det=((e11*e22*e33)+

 (e12*e23*e31)+

 (e13*e21*e32))-(

 (e31*e22*e13)+

 (e32*e23*e11)+

 (e33*e21*e12))

print('\n |',s,'| =',det,'\n')



#Adjoin A

a11=(e22*e33)-(e32*e23)

a21=-((e12*e33)-(e32*e13))

a31=(e12*e23)-(e22*e13)

a12=-((e21*e33)-(e31*e23))

a22=(e11*e33)-(e31*e13)

a32=-((e11*e23)-(e21*e13))

a13=(e21*e32)-(e31*e22)

a23=-((e11*e32)-(e31*e12))

a33=(e11*e22)-(e21*e12)



print(' |',a11, a12, a13, '|')

print('Adj',s,' =|',a21, a22, a23, '|')

print(' |',a31, a32, a33, '|\n')



#Tranpose

print('  |', a11, a21, a31, '|')

print('Tranpose Adj',s,'=|',a12, a22, a32, '|')

print('  |',a13, a23, a33, '|\n')



#Invers

i11=a11/det

i21=a21/det

i31=a31/det

i12=a12/det

i22=a22/det

i32=a32/det

i13=a13/det

i23=a23/det

i33=a33/det



#saya ambil 3 angka belakang koma

x11=round(i11,3)

x21=round(i21,3)

x31=round(i31,3)

x12=round(i12,3)

x22=round(i22,3)

x32=round(i32,3)

x13=round(i13,3)

x23=round(i23,3)

x33=round(i33,3)



print('    |', x11, x21, x31, '|')

print('Invers ',s,'=|',x12, x22, x32, '|')

print('    |', x13, x23, x33, '|')