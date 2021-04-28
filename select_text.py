# IMPORTANT! select_text.py is just a test!


from pynput.keyboard import Key
from PIL import ImageGrab
import pytesseract
import pyperclip
from pynput import mouse, keyboard

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
    "key": Key.scroll_lock,
}

pytesseract.pytesseract.tesseract_cmd = config["tesseract"]

while(True):
    pos1 = None
    pos2 = None

    # get first mouse position
    def on_click1(x, y, button, pressed):
        # some globals
        global pos1
        pos1 = (x, y)
        # if not released
        if not pressed:
            return False

    # get second mouse position
    def on_click2(x, y, button, pressed):
        # some globals
        global pos2
        pos2 = (x, y)
        # if not released
        if not pressed:
            return False

    def process():
        # mouse positions
        global pos1
        global pos2

        # start listening
        with mouse.Listener(on_click=on_click1) as listener:
            listener.join()

        # start listening
        with mouse.Listener(on_click=on_click2) as listener:
            listener.join()

        # writing indent ints from tuples
        pos1_  = pos1[0]
        pos1__ = pos1[1]
        pos2_  = pos2[0]
        pos2__ = pos2[1]

        # if user throw first pos as second (to prevent app crash)
        if pos1_ > pos2_ and pos1__ > pos2__:
            # processing positions
            pos1_p  = pos2_
            pos1__p = pos2__
            pos2_p  = pos1_
            pos2__p = pos1__

            # writing positions
            pos1_ = pos1_p
            pos1__ = pos1__p
            pos2_ = pos2_p
            pos2__ = pos2__p

        image = ImageGrab.grab(all_screens=True, bbox=(pos1_, pos1__, pos2_, pos2__))

        text = pytesseract.image_to_string(image, lang=config["language"])

        pyperclip.copy(text)
        print(f"Copied!\nOutput:\n{text}")

    def on_press(key):
        if key == config["key"]:
            process()

        return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
