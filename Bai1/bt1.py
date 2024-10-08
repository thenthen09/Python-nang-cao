import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

# Hàm tính phương trình bậc 1
def giai_pt_bac_1():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if a == 0:
            if b == 0:
                result.set("Phương trình có vô số nghiệm.")
            else:
                result.set("Phương trình vô nghiệm.")
        else:
            x = -b / a
            result.set(f"Nghiệm của phương trình: x = {x:.2f}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")

# Hàm tính phương trình bậc 2 
def giai_pt_bac_2():
    try:
        a = float(entry_a2.get())
        b = float(entry_b2.get())
        c = float(entry_c2.get())
        if a == 0:
            giai_pt_bac_1()  # Nếu a = 0, gọi lại hàm tính phương trình bậc 1
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                result2.set("Phương trình vô nghiệm.")
            elif delta == 0:
                x = -b / (2*a)
                result2.set(f"Phương trình có nghiệm kép: x = {x:.2f}")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                result2.set(f"Nghiệm x1 = {x1:.2f}, x2 = {x2:.2f}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số.")

# Tạo giao diện chính
win = tk.Tk()
win.title("Giải phương trình bậc 1 và bậc 2")

# Tạo Notebook để chứa các tab
notebook = ttk.Notebook(win)
notebook.pack(padx=10, pady=10, expand=True)

# Tạo tab cho phương trình bậc 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Phương trình bậc 1")

ttk.Label(tab1, text="Phương trình bậc 1: ax + b = 0").grid(row=0, column=0, columnspan=2, pady=10)
ttk.Label(tab1, text="Nhập a:").grid(row=1, column=0, padx=5, pady=5)
entry_a = ttk.Entry(tab1, width=10)
entry_a.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(tab1, text="Nhập b:").grid(row=2, column=0, padx=5, pady=5)
entry_b = ttk.Entry(tab1, width=10)
entry_b.grid(row=2, column=1, padx=5, pady=5)

result = tk.StringVar()
ttk.Label(tab1, textvariable=result).grid(row=4, column=0, columnspan=2, pady=10)

ttk.Button(tab1, text="Giải phương trình bậc 1", command=giai_pt_bac_1).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Tạo tab cho phương trình bậc 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Phương trình bậc 2")

ttk.Label(tab2, text="Phương trình bậc 2: ax^2 + bx + c = 0").grid(row=0, column=0, columnspan=2, pady=10)
ttk.Label(tab2, text="Nhập a:").grid(row=1, column=0, padx=5, pady=5)
entry_a2 = ttk.Entry(tab2, width=10)
entry_a2.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(tab2, text="Nhập b:").grid(row=2, column=0, padx=5, pady=5)
entry_b2 = ttk.Entry(tab2, width=10)
entry_b2.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(tab2, text="Nhập c:").grid(row=3, column=0, padx=5, pady=5)
entry_c2 = ttk.Entry(tab2, width=10)
entry_c2.grid(row=3, column=1, padx=5, pady=5)

result2 = tk.StringVar()
ttk.Label(tab2, textvariable=result2).grid(row=5, column=0, columnspan=2, pady=10)

ttk.Button(tab2, text="Giải phương trình bậc 2", command=giai_pt_bac_2).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

win.mainloop()
