import numpy as np

matriks = np.array([(a,b,c),
              (d,e,f),
              (g,h,i)])
matriks_hasil = np.array([(x),
              (y),
              (z)])
hasil = np.linalg.solve(matriks,matriks_hasil)
print(hasil)