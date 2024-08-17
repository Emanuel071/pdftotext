from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
from docx import Document
import cv2

def convert_pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)

def convert_image_to_text(file):
    text = image_to_string(file)
    return text

def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img(pdf_file)
    final_text = ''
    for pg, img in enumerate(images):
        print(f"page {pg} and image {img}")
        if pg == 1:
            final_text += convert_image_to_text(img)
    return final_text
   
def string_var_to_word_doc(var_string):
    # Create a new Document
    doc = Document()

    # Add a paragraph with the string
    doc.add_paragraph(var_string)

    # Save the document
    doc.save('tests/Brewster_July_2024_financials_balancesheet.docx')

    print("Document saved successfully.")


##MAIN##
# path_to_pdf = '/Users/eacalder/Documents/Github/pdftotext/tests/white-fang.pdf'
path_to_pdf = '/Users/eacalder/Documents/brewster/financials/Brewster_July_2024_financials.pdf'


# Load image (already black and white)
img = cv2.imread(path_to_pdf, cv2.IMREAD_UNCHANGED)

# Optional: Deskewing if needed
coords = cv2.findNonZero(img)
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle
(h, w) = img.shape[:2]
M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
deskewed = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


# # Deskewing
# coords = cv2.findNonZero(binary)
# angle = cv2.minAreaRect(coords)[-1]
# if angle < -45:
#     angle = -(90 + angle)
# else:
#     angle = -angle
# (h, w) = binary.shape[:2]
# M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
# deskewed = cv2.warpAffine(binary, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)



# stinrg_variable = get_text_from_any_pdf(path_to_pdf)
# print(stinrg_variable)

# string_var_to_word_doc(stinrg_variable)

# print("Job successful.")