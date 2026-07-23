#!/usr/bin/env python3
"""
Python GUI Hesap Makinesi
İşlemler: Toplama, Çıkarma, Çarpma, Bölme, Kök, Üs, Mod, Yüzde
"""

import tkinter as tk
from tkinter import ttk
import math


class HesapMakinesi:
    def __init__(self, root):
        self.root = root
        self.root.title("Hesap Makinesi")
        self.root.geometry("400x550")
        self.root.resizable(False, False)

        self.current = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Renk paleti - Yeşil tonları
        self.bg_color = '#2E7D32'  # Koyu yeşil
        self.button_color = '#66BB6A'  # Orta yeşil
        self.button_hover = '#81C784'  # Açık yeşil
        self.display_bg = '#1B5E20'  # Çok koyu yeşil
        self.text_color = 'white'
        self.operator_color = '#43A047'  # İşlem butonu rengi
        self.clear_color = '#C62828'  # Silme butonu rengi

        self.root.configure(bg=self.bg_color)

        # Ana frame
        main_frame = tk.Frame(self.root, bg=self.bg_color, padx=15, pady=15)
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Ekran
        display_frame = tk.Frame(main_frame, bg=self.bg_color)
        display_frame.grid(row=0, column=0, columnspan=4, pady=10, sticky=(tk.W, tk.E))

        self.display = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=('Arial', 28, 'bold'),
            bg=self.display_bg,
            fg=self.text_color,
            relief='flat',
            padx=15,
            pady=15,
            anchor='e',
            width=15
        )
        self.display.grid(row=0, column=0, sticky=(tk.W, tk.E))

        # Butonlar
        buttons = [
            ('√', 1, 0, self.kok, self.button_color),
            ('x²', 1, 1, self.us, self.button_color),
            ('%', 1, 2, self.yuzde, self.button_color),
            ('AC', 1, 3, self.clear, self.clear_color),
            ('7', 2, 0, lambda: self.append('7'), self.button_color),
            ('8', 2, 1, lambda: self.append('8'), self.button_color),
            ('9', 2, 2, lambda: self.append('9'), self.button_color),
            ('/', 2, 3, lambda: self.append('/'), self.operator_color),
            ('4', 3, 0, lambda: self.append('4'), self.button_color),
            ('5', 3, 1, lambda: self.append('5'), self.button_color),
            ('6', 3, 2, lambda: self.append('6'), self.button_color),
            ('*', 3, 3, lambda: self.append('*'), self.operator_color),
            ('1', 4, 0, lambda: self.append('1'), self.button_color),
            ('2', 4, 1, lambda: self.append('2'), self.button_color),
            ('3', 4, 2, lambda: self.append('3'), self.button_color),
            ('-', 4, 3, lambda: self.append('-'), self.operator_color),
            ('0', 5, 0, lambda: self.append('0'), self.button_color),
            (',', 5, 1, lambda: self.append(','), self.button_color),
            ('=', 5, 2, self.calculate, '#2E7D32'),
            ('+', 5, 3, lambda: self.append('+'), self.operator_color),
        ]

        for text, row, col, command, color in buttons:
            btn = tk.Button(
                main_frame,
                text=text,
                command=command,
                width=6,
                height=2,
                font=('Arial', 16, 'bold'),
                bg=color,
                fg=self.text_color,
                activebackground=self.button_hover,
                activeforeground=self.text_color,
                relief='flat',
                cursor='hand2'
            )
            btn.grid(row=row, column=col, padx=3, pady=3)

    def append(self, value):
        if self.result_var.get() == "0" and value not in [',', '/', '*', '-', '+']:
            self.result_var.set(value)
        else:
            self.result_var.set(self.result_var.get() + value)

    def clear(self):
        self.result_var.set("0")

    def delete(self):
        current = self.result_var.get()
        if len(current) > 1:
            self.result_var.set(current[:-1])
        else:
            self.result_var.set("0")

    def calculate(self):
        try:
            expression = self.result_var.get().replace(',', '.')
            result = eval(expression)

            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)

            self.result_var.set(str(result))
        except ZeroDivisionError:
            self.result_var.set("Hata: Sıfıra bölünemez")
        except:
            self.result_var.set("Hata")

    def kok(self):
        try:
            value = float(self.result_var.get().replace(',', '.'))
            result = math.sqrt(value)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.result_var.set(str(result))
        except:
            self.result_var.set("Hata")

    def us(self):
        try:
            value = float(self.result_var.get().replace(',', '.'))
            result = value ** 2
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.result_var.set(str(result))
        except:
            self.result_var.set("Hata")

    def yuzde(self):
        try:
            value = float(self.result_var.get().replace(',', '.'))
            result = value / 100
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.result_var.set(str(result))
        except:
            self.result_var.set("Hata")


if __name__ == "__main__":
    root = tk.Tk()
    app = HesapMakinesi(root)
    root.mainloop()
