from PIL import Image
import pytesseract
import tkinter as tk
from tkinter import filedialog, messagebox
import pyperclip

"""

    * Powered by Tesseract OCR
    * https://opensource.google/projects/tesseract
    * https://github.com/tesseract-ocr/tesseract

    ***** DOWNLOADS *****
    * For windows: https://sourceforge.net/projects/tesseract-ocr-alt/files/
    * For linux:   https://github.com/tesseract-ocr/tesseract/releases

"""


config = {
    "language": "eng",
    "tesseract": r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
}


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

pytesseract.pytesseract.tesseract_cmd = config["tesseract"]

text = pytesseract.image_to_string(Image.open(file_path), lang=config["language"])

yesno = messagebox.askyesno(title="Copy to clipboard?", message=f"Text:\n{text}")

if yesno:
    pyperclip.copy(text)