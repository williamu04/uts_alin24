import numpy as np
import scipy.linalg

def matriks_diagonal():
    n = int(input("Masukkan jumlah baris/kolom: "))

    print(f"Masukkan koefisien matriks A (ukuran {n}x{n}):")
    A = []
    for _ in range(n):
        row = [float(x) for x in input().split()]
        A.append(row)
    A = np.array(A)

    eigenvalues, eigenvectors = scipy.linalg.eig(A)
    diagonal_matrix = np.diag(eigenvalues)
    inverse_eigenvectors = np.linalg.inv(eigenvectors)
    diagonalized_matrix = np.matmul(np.matmul(eigenvectors, diagonal_matrix), inverse_eigenvectors)

    print("D:")
    print(diagonal_matrix)
    print("Diagonalized Matrix:")
    print(diagonalized_matrix)

    result = (f"Eigenvalues:\n{eigenvalues}\nEigenvector (P):\n{eigenvectors}\nD:\n{diagonal_matrix}\nMatriks Terdiagonalisasi:\n{diagonalized_matrix}\n")
    with open("readme.txt", "a") as file:
        file.write(result)