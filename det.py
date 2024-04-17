import numpy as np


def determinant_gauss_elimination(matrix):
    n = len(matrix)
    for i in range(n):
        max_idx = np.argmax(np.abs(matrix[i:, i])) + i
        matrix[[i, max_idx]] = matrix[[max_idx, i]]
        for j in range(i+1, n):
            factor = matrix[j][i]/matrix[i][i]
            matrix[j] -= factor * matrix[i]
    return np.prod(np.diagonal(matrix))

def determinant_gauss_jordan_elimination(matrix):
    n = len(matrix)
    for i in range(n):
        max_idx = np.argmax(np.abs(matrix[i:, i])) + i
        matrix[[i, max_idx]] = matrix[[max_idx, i]]
        for j in range(n):
            if j!= i:
                factor = matrix[j][i]/matrix[i][i]
                matrix[j] -= factor * matrix[i]
    return np.prod(np.diagonal(matrix))

def determinant_general_inverse(matrix):
    return np.linalg.det(matrix)

def determinant():
    n = int(input("Masukkan jumlah baris/kolom: "))

    print(f"Masukkan koefisien matriks A (ukuran {n}x{n}):")
    A = []
    for _ in range(n):
        row = [float(x) for x in input().split()]
        A.append(row)
    A = np.array(A)

    print("Pilih metode : ")
    print("1. Metode Eliminasi Gauss")
    print("2. Metode Eliminasi Gauss-Jordan")
    print("3. Metode Matriks Balikan")
    selection = int(input("Pilihan Anda: "))

    match selection:
        case 1: 
            print(determinant_gauss_elimination(A))
        case 2: 
            print(determinant_gauss_jordan_elimination(A))
        case 3: 
            print(determinant_general_inverse(A))
    


