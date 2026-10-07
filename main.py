import customtkinter as ctk
from utils import *
from win11toast import toast
import tkinter.messagebox as mb

root = ctk.CTk()
root.title('RollerAV')
root.geometry('800x800')

FONT_TEXT = ctk.CTkFont('Segoe UI', 23)
FONT_TITLE = ctk.CTkFont('Segoe UI', 32)
FONT_SUBTITLE = ctk.CTkFont('Segoe UI', 26)
FONT_SMALL = ctk.CTkFont('Segoe UI', 18)
PADDING = {'pady': 13, 'padx': 5}

root.option_add('*Font', FONT_TEXT)

tabview = ctk.CTkTabview(root)
tabview._segmented_button.configure(font=FONT_SUBTITLE)
tabview.pack(fill='both', expand=True, **PADDING)

hometab = tabview.add('Home')

status_label = ctk.CTkLabel(hometab, text='System status: SECURE', font=FONT_TITLE)
status_label.pack(**PADDING)

ctk.CTkButton(hometab, text='Quick Scan', command=lambda: None).pack(**PADDING)

if __name__ == '__main__':
    root.mainloop()