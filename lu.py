import numpy as np
from scipy.linalg import lu

def lu_factorization():
    # Prompt the user to enter the number of rows and columns
    n_rows = int(input("Enter the number of rows: "))
    n_cols = int(input("Enter the number of columns: "))

    # Initialize the matrix as a list of lists
    matrix = []
    for i in range(n_rows):
        row = list(map(float, input(f"Enter row {i+1}: ").split()))
        if len(row)!= n_cols:
            raise ValueError("Invalid number of elements in row")
        matrix.append(row)

    # Convert the matrix to a NumPy array
    matrix = np.array(matrix)

    # Compute the LU factorization
    L, U = lu(matrix, permute_l=True)

    # Print the results
    # print("P = \n", P)
    print("L = \n", L)
    print("U = \n", U)