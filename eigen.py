import numpy as np
import scipy.linalg

def polinom_eigen():
    n = int(input("Masukkan jumlah baris/kolom: "))

    print(f"Masukkan koefisien matriks A (ukuran {n}x{n}):")
    A = []
    for _ in range(n):
        row = [float(x) for x in input().split()]
        A.append(row)
    A = np.array(A)

    eigenvalues, eigenvectors = scipy.linalg.eig(A)
    poly_char = np.poly(eigenvalues)
    diagonal_matrix = np.diag(eigenvalues)
    inverse_eigenvectors = np.linalg.inv(eigenvectors)
    diagonalized_matrix = np.matmul(np.matmul(eigenvectors, diagonal_matrix), inverse_eigenvectors)

    print("Polinomial Karakteristik:")
    print(poly_char)
    print("Eigenvalues:")
    print(eigenvalues)
    print("Eigenvector (P):")
    print(eigenvectors)
    print("P^-1:")
    print(inverse_eigenvectors)

    result = (f"Polinomial Karakteristik:\n{poly_char}\nEigenvalues:\n{eigenvalues}\nEigenvector (P):\n{eigenvectors}\nP^-1:\n{inverse_eigenvectors}\n")
    with open("readme.txt", "a") as file:
        file.write(result)