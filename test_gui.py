import tkinter as tk

def tampilkan_teks():
    label.config(text="Halo Dunia!")

root = tk.Tk()
root.title("Aplikasi GUI Sederhana")

label = tk.Label(root, text="")
label.pack()

tombol = tk.Button(root, text="Klik Saya", command=tampilkan_teks)
tombol.pack()

root.mainloop()
