from pdf2image import convert_from_path
import easyocr

# Path to the PDF file
pdf_path = 'image_based_balance_sheet.pdf'

# Convert PDF to list of images (one per page)
images = convert_from_path(pdf_path, dpi=300)  # Set DPI to improve quality


# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # 'en' stands for English, add more languages if needed

# Iterate over each image and perform OCR
for i, image in enumerate(images):
    # Convert PIL image to numpy array
    ocr_results = reader.readtext(image, detail=0)  # detail=0 returns the text only

    # Print or save the results
    print(f"Text from page {i + 1}:\n")
    for result in ocr_results:
        print(result)
