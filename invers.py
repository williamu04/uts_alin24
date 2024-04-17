import numpy as np

def inverse_matrix():
    n = int(input("Masukkan jumlah baris/kolom: "))

    print(f"Masukkan koefisien matriks A (ukuran {n}x{n}):")
    A = []
    for _ in range(n):
        row = [float(x) for x in input().split()]
        A.append(row)
    A = np.array(A)
    inv_A = np.linalg.inv(A)
    # Create an identity matrix as the right side of the augmented matrix
    print("Original Matriks:")
    print(A)
    print("Inverse Matriks:")
    print(inv_A)

    result = (f"Original Matriks:\n{A}\nInverse Matriks:\n{inv_A}\n")
    with open("readme.txt", "a") as file:
        file.write(result)