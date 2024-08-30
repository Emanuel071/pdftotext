from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
from docx import Document

def convert_pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)

def convert_image_to_text(file):
    text = image_to_string(file)
    print(text)
    return text

def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img(pdf_file)
    final_text = ''
    for pg, img in enumerate(images):
        final_text += convert_image_to_text(img)
    return final_text
   
def string_var_to_word_doc(var_string):
    # Create a new Document
    doc = Document()

    # Add a paragraph with the string
    doc.add_paragraph(var_string)

    # Save the document
    # doc.save('tests/Brewster_July_2024_financials.docx')

    print("Document saved successfully.")


##MAIN##
path_to_pdf = '/Users/eacalder/Documents/Github/pdftotext/tests/output_page_2.pdf'
# path_to_pdf = '/Users/eacalder/Documents/brewster/financials/Brewster_July_2024_financials.pdf'

stinrg_variable = get_text_from_any_pdf(path_to_pdf)
# print(stinrg_variable)

string_var_to_word_doc(stinrg_variable)

print("Job successful.")