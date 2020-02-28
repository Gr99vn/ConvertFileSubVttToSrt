import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def getFilePath():
    file_path = filedialog.askopenfilenames()
    return list(file_path)