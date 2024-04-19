import re
import numpy as np
import scipy.linalg

def hitung_complex(persamaan, variabel):
    matrix1 = np.zeros((persamaan, variabel), dtype=complex)
    matrix2 = np.zeros(persamaan, dtype=complex)
    eqVariable = set()

    print("Masukkan persamaan-persamaan: ")
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

def write_result_to_file(c, x):
    with open("readme.txt", "a") as file:
        file.write("Hasil:\n")
        index = 0
        while index <= len(c):
            result = str(c[index]) + " = " + str(x[index]) + "\n"
            file.write(result)
            index += 1

def spl_complex():
    n = int(input("Masukkan jumlah persamaan: "))
    m = int(input("Masukkan jumlah variabel: "))

    matrix1, matrix2, c = hitung_complex(n, m)
    U, s, Vh = scipy.linalg.svd(matrix1)
    s_inv = np.zeros_like(matrix1.T, dtype=complex)
    s_inv[:s.size, :s.size] = np.diag(1 / s)
    x = Vh.T @ s_inv @ U.T @ matrix2

    print("Hasil: ")
    index = 0
    while index <= len(c):
        result = str(c[index]) + " = " + str(x[index])
        print(result)
        index += 1

    write_result_to_file(c, x)