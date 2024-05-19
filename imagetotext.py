from PIL import Image
from pytesseract import pytesseract
import enum

class OS(enum.Enum):
    Mac = 0 
    Windows = 1

class Language(enum.Enum):
    ENG = 'eng'

class ImageReader:

    def __init__(self, os: OS):
        if os == OS.Mac:
            # tessarct is already installed via brew
            print('running on :mac\n')

        if os == OS.Windows:
            windows_path = r'C:'
    def extract_text(self, image:str, lang:str) -> str:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img, lang=lang)
        return extracted_text
    
if __name__ == '__main__':
    ir = ImageReader(OS.Mac)
    text = ir.extract_text('tests/white-fang.pdf', lang='eng')
    print(text)