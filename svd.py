import numpy as np
import scipy.linalg

def svd():
    n = int(input("Masukkan jumlah baris/kolom: "))

    print(f"Masukkan koefisien matriks A (ukuran {n}x{n}):")
    A = []
    for _ in range(n):
        row = [float(x) for x in input().split()]
        A.append(row)
    A = np.array(A)
    
    mat_u, mat_s, mat_vh = scipy.linalg.svd(A)

    print("Matriks U:")
    print(mat_u)
    print("Matriks S:")
    print(np.diag(mat_s))
    print("Matriks Vh:")
    print(mat_vh)

    result = (f"Matriks U:\n{mat_u}\nMatriks S:\n{np.diag(mat_s)}\nMatriks Vh:\n{mat_vh}\n")
    with open("readme.txt", "a") as file:
        file.write(result)