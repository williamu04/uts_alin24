import numpy as np
import scipy.linalg
import re
import os
from svd import svd
from eigen import polinom_eigen
from diagonal import matriks_diagonal
from invers import inverse_matrix
from det import determinant
from lu import lu_factorization

def method_gauss_jordan(A, b):
    n = len(A)
    
    for i in range(n):
        if A[i][i] == 0:
            return None
        
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            
            for k in range(n):
                A[j][k] -= ratio * A[i][k]
            
            b[j] -= ratio * b[i]
    
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1][n-1]
    
    for i in range(n-2, -1, -1):
        x[i] = b[i]
        
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        
        x[i] /= A[i][i]
    
    return x

def solve_gauss_jordan():
    n = int(input("Masukkan jumlah baris: "))
    m = int(input("Masukkan jumlah kolom: "))

    print(f"Masukkan koefisien matriks A (ukuran {n}x{m}):")
    A = []
    for _ in range(n):
        row = [float(x) for x in input().split()]
        A.append(row)
    A = np.array(A)

    print(f"Masukkan vektor b (ukuran {n}):")
    B = np.array([float(x) for x in input().split()])

    solution = method_gauss_jordan(A, B)

    augmented_matrix = np.hstack((A, B.reshape(-1, 1)))
    temp_matrix = scipy.linalg.matrix_rank(augmented_matrix)
    cols = A.shape[1]

    if solution is None:
        print("No Solution")
        result = "No Solution\n"
    elif temp_matrix < cols:
        print("Infinite Solutions")
        result = "Infinite Solutions\n"
    else:
        print("Unique Solution:")
        result = "Unique Solution:\n"
        for i, sol in enumerate(solution):
            print(f"x{i+1} = {sol}")
            result += (f"x{i+1} = {sol}\n")

    with open("readme.txt", "a") as file:
        file.write(result)

def persamaan(n):
    print("Contoh penulisan: 3a +2b - 4c - 19d = 2")
    
    kiri_matrix = []  
    kanan_matrix = []  
    variables = set()

    for _ in range(n):
        equation = input("Persamaan ke-{}: ".format(_ + 1))

        equation = equation.replace(" ", "").split("=")
        kiri = equation[0]
        kiri_terms = re.split(r"([+-])", kiri)  
        kiri_coefficients = []
        for term in kiri_terms:
            if term != "+" and term != "-":
                coefficient = term[:-1]  
                if coefficient == "":
                    coefficient = "1"  
                kiri_coefficients.append(float(coefficient))
                variable = term[-1]
                variables.add(variable)
        kiri_matrix.append(kiri_coefficients)
        kanan = float(equation[1])
        kanan_matrix.append(kanan)
        
    kiri_matrix = np.array(kiri_matrix)
    kanan_matrix = np.array(kanan_matrix)
    variables = np.sort(np.array(list(variables)))
    return kiri_matrix, kanan_matrix, variables

def spl_solution(matrix1, matrix2):
    baris, kolom = matrix1.shape
    if baris != kolom:
        return "\nHasil = Tidak ada solusi"
    a = scipy.linalg.det(matrix1)
    if a != 0:
        return "\nHasil = Solusi unik"
    matrix_aug = np.hstack((matrix1, matrix2.reshape(-1, 1)))
    matrix_ref = np.linalg.matrix_rank(matrix_aug)

    if matrix_ref < np.linalg.matrix_rank(matrix1):
        return "\nHasil = Tidak ada solusi"

    elif matrix_ref < kolom:
        return "\nHasil = Solusi tak terbatas"
    else:
        return "\nHasil = Solusi unik"

def spl_variabel(): 
    n = int(input("Jumlah persamaan yang akan dihitung: "))
    matrix1, matrix2, c = persamaan(n)

    solution = spl_solution(matrix1, matrix2)
    print(f"Solusi: {solution}")

    if solution == "\nHasil = Solusi unik" :
        x = scipy.linalg.solve(matrix1, matrix2)
        for index in range(len(c)):
            hasil = "{} = {}".format(c[index], x[index])
            print(hasil)

    elif solution == "\nHasil = Solusi tak terbatas":
        particular_solution = scipy.linalg.lstsq(matrix1[:, :-1], matrix2)[0]
        null_space = scipy.linalg.null_space(matrix1[:, :-1])
        print("Solusi dalam bentuk parameter:")
        for i in range(null_space.shape[1]):
            param = "p" + str(i + 1)
            print(f"x{i + 1} = {particular_solution[i]} + {param} * {null_space[:, i]}")


def hitung_complex(persamaan, variabel):
    matrix1 = np.zeros((persamaan, variabel), dtype=complex)
    matrix2 = np.zeros(persamaan, dtype=complex)
    eqVariable = set()

    print("Masukkan persamaan-persamaan:")
    for i in range(persamaan):
        persamaan = input(f"Persamaan {i+1}: ")
        persamaan = re.sub(r'([a-z])', r'1j*\1', persamaan) 
        koefisien = re.findall(r'[+-]?\d+\.?\d*|\d*\.?\d+[j]', persamaan)
        for j in range(variabel):
            matrix1[i, j] = complex(koefisien[j])
        matrix2[i] = complex(koefisien[-1])
        variables = re.findall(r'[a-z]', persamaan)
        eqVariable.update(variables)

    eqVariable = sorted(list(eqVariable))

    return matrix1, matrix2, eqVariable
    
def spl_complex():
    n = int(input("Masukkan jumlah persamaan: "))
    m = int(input("Masukkan jumlah variabel: "))
    
    matrix1, matrix2, c = hitung_complex(n, m)
    U, s, Vh = scipy.linalg.svd(matrix1)
    s_inv = np.zeros_like(matrix1.T, dtype=complex)
    s_inv[:s.size, :s.size] = np.diag(1 / s)
    x = Vh.T @ s_inv @ U.T @ matrix2

    print("Hasil:")
    index = 0
    while index <= len(c):
        result = str(c[index]) + " = " + str(x[index])
        print(result)
        index += 1  

    with open("readme.txt", "a") as file:
        file.write("Hasil:\n")
        index = 0
        while index <= len(c):
            result = str(c[index]) + " = " + str(x[index]) + "\n"
            file.write(result)
            index += 1

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print("==================")
    print("KALKULATOR MATRIKS")
    print("===================")
    print("Pilih program :")
    print("1. Mencari solusi SPL (Matriks)")
    print("2. Mencari Determinan Matriks")
    print("3. Mencari Inverse Matriks")
    print("4. Mencari Diagonalisasi Matriks")
    print("5. Mencari Faktorisasi LU ")
    print("6. Mencari SVD (Singular Value Decomposition)")
    print("7. Mencari Karakteristik Polinomial, Nilai Eigen dan Vektor Eigen")
    print("8. Hapus arsip dari readme")
    print("0. Keluar dari program")
    selection = int(input("Pilihan Anda: "))

    match selection:
        case 1:
            solve_gauss_jordan()
            input("\nPress any key to continue . . . ")
        case 2:
            determinant()
            input("\nPress any key to continue . . . ")
        case 3: 
            inverse_matrix()
            input("\nPress any key to continue . . . ")
        case 4:
            matriks_diagonal()
            input("\nPress any key to continue . . . ")
        case 5: 
            lu_factorization()
            input("\nPress any key to continue . . . ")
        case 6:
            svd()
            input("\nPress any key to continue . . . ")
        case 7:
            polinom_eigen()
            input("\nPress any key to continue . . . ")
        case 8:
            print("Menghapus arsip dari readme.txt")
            input("\nPress any key to continue . . . ")
            with open("readme.txt", "w") as file :
                pass
        case 0:
            print("\nTerima kasih telah menggunakan program kalkulator matriks!")
            break
        case _:
            print("Pilihan tidak valid")