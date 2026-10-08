import customtkinter as ctk
from utils import *
from win11toast import toast
import tkinter.messagebox as mb
from datetime import datetime

FILE_DIR = Path(__file__).parent

root = ctk.CTk()
root.title('RollerAV')
root.geometry('800x800')

FONT_TEXT = ctk.CTkFont('Segoe UI', 23)
FONT_TITLE = ctk.CTkFont('Segoe UI', 32)
FONT_SUBTITLE = ctk.CTkFont('Segoe UI', 26)
FONT_SMALL = ctk.CTkFont('Segoe UI', 18)
PADDING = {'pady': 13, 'padx': 5}
MALICIOUS_HASHES = load_hashes(FILE_DIR / 'hashes.txt')

root.option_add('*Font', FONT_TEXT)

tabview = ctk.CTkTabview(root)
tabview._segmented_button.configure(font=FONT_SUBTITLE)
tabview.pack(fill='both', expand=True, **PADDING)

hometab = tabview.add('Home')

status_label = ctk.CTkLabel(hometab, text='System status: SECURE', font=FONT_TITLE)
status_label.pack(**PADDING)

ctk.CTkButton(hometab, text='Quick Scan', command=lambda: None).pack(**PADDING)

scantab = tabview.add('Scan')

ctk.CTkLabel(scantab, text='Scan Manager', font=FONT_TITLE).pack(**PADDING)

logbox = ctk.CTkTextbox(scantab, state='disabled', width=700, height=400, font=FONT_SMALL)
logbox.pack(**PADDING)

def log(message, level='info'):
    logbox.configure(state='normal')
    logbox.insert('end', f'[{datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")}] [{level.upper()}] {message}\n')
    logbox.configure(state='disabled')

if __name__ == '__main__':
    root.mainloop()