import numpy as np

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
    B_trans = B.transpose()

    solution = method_gauss_jordan(A, B)

    augmented_matrix = np.hstack((A, B.reshape(-1, 1)))
    temp_matrix = np.linalg.matrix_rank(augmented_matrix)
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

    hasil = (f"Matrix A:\n{A}\nMatrix B:\n{B}\nSolusi:\n{result}\n")
    with open("readme.txt", "a") as file:
        file.write(hasil)