import tkinter as tk

class Kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Sederhana")
        self.ekspresi = ""
        
        # Display outputnyee
        self.layar = tk.Entry(root, width=20, font=('Arial', 20), bd=5, relief=tk.SUNKEN, justify='right')
        self.layar.grid(row=0, column=0, columnspan=4)
        
        # Buttons nya ya gess
        self.tombol = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
            ('+', 4, 0), ('=', 4, 2)
        ]
        
        for (text, row, col) in self.tombol:
            if text == "=":
                tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), 
                          command=self.hitung).grid(row=row, column=col)
            else:
                tk.Button(root, text=text, width=5, height=2, font=('Arial', 20), 
                          command=lambda t=text: self.masukkan_angka(t)).grid(row=row, column=col)
    
    def masukkan_angka(self, angka):# Ini adalah update terbaru untuk kalkulator

        self.ekspresi += angka
        self.layar.delete(0, tk.END)
        self.layar.insert(tk.END, self.ekspresi)
    
    def hitung(self):
        try:
            hasil = eval(self.ekspresi)
            self.layar.delete(0, tk.END)
            self.layar.insert(tk.END, str(hasil))
            self.ekspresi = str(hasil)
        except:
            self.layar.delete(0, tk.END)
            self.layar.insert(tk.END, "Error")
            self.ekspresi = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = Kalkulator(root)
    root.mainloop()
