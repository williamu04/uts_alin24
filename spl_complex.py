import re
import numpy as np

def spl_complex():
    n = int(input("Masukkan jumlah baris: "))
    m = int(input("Masukkan jumlah kolom: "))

    print(f"Masukkan koefisien matriks A (ukuran {n}x{m}):")
    A = []
    for _ in range(n):
        row = list(map(complex, input().split()))
        A.append(row)
    A = np.array(A)

    print(f"Masukkan vektor b (ukuran {n}):")
    b = list(map(complex, input().split()))
    b = np.array(b)

    # Solve the system of linear equations
    solusi = np.linalg.solve(A, b)

    # Print the solution
    print("The solution of the linear equations is:")
    for i, s in enumerate(solusi):
        i+=1
        print(f"x{i} = {s}")
        result = (f"\nx{i}: {s}\n")
        with open("readme.txt", "a") as file:
            file.write(result)