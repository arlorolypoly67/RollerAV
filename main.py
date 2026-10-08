import customtkinter as ctk
from utils import load_hashes, scan_file
from win11toast import toast
import tkinter.filedialog as fd
from datetime import datetime
from pathlib import Path
from queue import Queue
import threading

log_queue = Queue()
stuff_queue = Queue()

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
    timestamp = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
    log_queue.put((timestamp, level, message))

def set_status(status: str):
    stuff_queue.put(('update_status', status))

def process_log_queue():
    while not log_queue.empty():
        timestamp, level, message = log_queue.get()

        logbox.configure(state='normal')
        logbox.insert(
            'end',
            f'[{timestamp}] [{level.upper()}] {message}\n'
        )
        logbox.configure(state='disabled')
        logbox.see('end')

    root.after(100, process_log_queue)

def process_stuff_queue():
    while not stuff_queue.empty():
        type_, value = stuff_queue.get()

        if type_ == 'update_status':
            status_label.configure(text=f'System status: {value.upper()}')
        elif type_ == 'toast':
            toast(message=value, app_id="RollerAV")

    root.after(100, process_stuff_queue)

def custom_scan_file(fp):
    log('Custom scan started')

    detected, filehash = scan_file(fp, MALICIOUS_HASHES)

    if detected is None and filehash is None:
        log('File not found', 'error')
        return

    if detected:
        message = f'{fp} was detected as malware (SHA256: {filehash})'
        stuff_queue.put(('toast', f'ALERT: {message}'))
        log(message, level='alert')
        set_status('infected')
    else:
        log(f'{fp} was not detected as malware')
        set_status('clean')

def start_custom_scan_file():
    selected = fd.askopenfilename(
        title='Scan a file',
        parent=root
    )

    if not selected:
        log('Custom scan cancelled')
        return

    threading.Thread(
        target=custom_scan_file,
        args=(Path(selected).resolve(),),
        daemon=True
    ).start()

ctk.CTkButton(scantab, text='Scan File', command=start_custom_scan_file).pack(**PADDING)

if __name__ == '__main__':
    process_log_queue()
    process_stuff_queue()

    root.mainloop()