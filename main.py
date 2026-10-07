import customtkinter as ctk
from utils import *
from win11toast import toast
import tkinter.messagebox as mb

root = ctk.CTk()
root.title('RollerAV')
root.geometry('800x800')

FONT_TEXT = ctk.CTkFont('Segoe UI', 17)
FONT_TITLE = ctk.CTkFont('Segoe UI', 26)
FONT_SUBTITLE = ctk.CTkFont('Segoe UI', 18)
FONT_SMALL = ctk.CTkFont('Segoe UI', 12)

root.option_add('*Font', FONT_TEXT)

tabview = ctk.CTkTabview(root)
tabview._segmented_button.configure(font=FONT_SUBTITLE)
tabview.pack(fill='both', expand=True)

hometab = tabview.add('Home')

if __name__ == '__main__':
    root.mainloop()