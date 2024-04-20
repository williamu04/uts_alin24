import re
import numpy as np
import scipy.linalg

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
            if term!= "+" and term!= "-":
                coefficient = term[:-1]
                if coefficient == "":
                    coefficient = "1"
                kiri_coefficients.append(float(coefficient))
                variable = term[-1]
                variables.add(variable)
        kiri_matrix.append(kiri_coefficients)
        kanan = float(equation[1])
        kanan_matrix.append(kanan)

    sistem = (f"Persamaan:\n{equation}\n")
    with open("readme.txt", "a") as file:
        file.write(result)
    kiri_matrix = np.array(kiri_matrix)
    kanan_matrix = np.array(kanan_matrix)
    variables = np.sort(np.array(list(variables)))
    return kiri_matrix, kanan_matrix, variables

def spl_solution(matrix1, matrix2):
    baris, kolom = matrix1.shape
    if baris!= kolom:
        return "\nHasil = Tidak ada solusi"
    a = scipy.linalg.det(matrix1)
    if a!= 0:
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
        particular_solution, residuals, rank, s = np.linalg.lstsq(matrix1, matrix2, rcond=None)
        null_space = scipy.linalg.null_space(matrix1)
        print("Solusi dalam bentuk parameter:")
        for i in range(null_space.shape[1]):
            param = "x" + str(i + 1)
            print(f"x{i + 1} = {particular_solution[i]} + {param} * {null_space[:, i]}")