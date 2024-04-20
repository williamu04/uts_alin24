import os
from svd import svd
from eigen import polinom_eigen
from diagonal import matriks_diagonal
from invers import inverse_matrix
from det import determinant
from lu import lu_factorization
from spl import solve_gauss_jordan
from homogen import spl_variabel
from spl_complex import spl_complex

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("==================")
        print("KALKULATOR MATRIKS")
        print("===================")
        print("Pilih program :")
        print("1. Mencari Solusi SPL (Matriks)")
        print("2. Mencari Solusi Sistem Homogen")
        print("3. Mencari Solusi SPL Kompleks")
        print("4. Mencari Determinan Matriks")
        print("5. Mencari Inverse Matriks")
        print("6. Mencari Diagonalisasi Matriks")
        print("7. Mencari Faktorisasi LU ")
        print("8. Mencari SVD (Singular Value Decomposition)")
        print("9. Mencari Karakteristik Polinomial, Nilai Eigen dan Vektor Eigen")
        print("10. Hapus arsip dari readme")
        print("0. Keluar dari program")
        selection = int(input("Pilihan Anda: "))

        match selection:
            case 1:
                solve_gauss_jordan()
                input("\nPress any key to continue . . . ")
            case 2:
                spl_variabel()
                input("\nPress any key to continue . . . ")
            case 3:
                spl_complex()
                input("\nPress any key to continue . . . ")
            case 4:
                determinant()
                input("\nPress any key to continue . . . ")
            case 5: 
                inverse_matrix()
                input("\nPress any key to continue . . . ")
            case 6:
                matriks_diagonal()
                input("\nPress any key to continue . . . ")
            case 7: 
                lu_factorization()
                input("\nPress any key to continue . . . ")
            case 8:
                svd()
                input("\nPress any key to continue . . . ")
            case 9:
                polinom_eigen()
                input("\nPress any key to continue . . . ")
            case 10:
                print("Menghapus arsip dari readme.txt")
                input("\nPress any key to continue . . . ")
                with open("readme.txt", "w") as file :
                    pass
            case 0:
                print("\nTerima kasih telah menggunakan program kalkulator matriks!")
                break
            case _:
                print("Pilihan tidak valid")

menu()