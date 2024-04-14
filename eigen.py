import numpy as np

def char_poly_eigen():
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

    # Compute the characteristic polynomial
    char_poly = np.poly(matrix)

    # Compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    # Compute the characteristic polynomial, eigenvalues, and eigenvectors
    char_poly, eigenvalues, eigenvectors = char_poly_eigen(matrix)

    # Print the results
    print("Characteristic polynomial: \n", char_poly)
    print("Eigenvalues: \n", eigenvalues)
    print("Eigenvectors: \n", eigenvectors)

char_poly_eigen()