from pdf2image import convert_from_path
from PIL import Image
import pytesseract

def extract_columns(image_path, columns):
    # Open the image
    img = Image.open(image_path)

    # Get the image width and height
    img_width, img_height = img.size

    # Calculate the width of each column
    column_width = img_width // columns

    # Initialize an empty string to store the extracted text
    extracted_text = []

    for i in range(columns):
        # Define the box to crop the image for each column (left, upper, right, lower)
        left = i * column_width
        right = (i + 1) * column_width
        box = (left, 0, right, img_height)
        
        # Crop the image to the current column
        column_img = img.crop(box)
        
        # Use pytesseract to do OCR on the cropped image
        text = pytesseract.image_to_string(column_img)
        extracted_text.append(text.strip())

    # Return the combined text
    return "\n".join(extracted_text)



def extract_text_from_columns(image_path, columns):
    # Open the image
    img = Image.open(image_path)

    # Get the image width and height
    img_width, img_height = img.size

    # Calculate the width of each column
    column_width = img_width // columns

    # Initialize lists to store text from each column
    column_texts = []

    for i in range(columns):
        # Define the box to crop the image for each column (left, upper, right, lower)
        left = i * column_width
        right = (i + 1) * column_width
        box = (left, 0, right, img_height)
        
        # Crop the image to the current column
        column_img = img.crop(box)
        
        # Use pytesseract to do OCR on the cropped image
        text = pytesseract.image_to_string(column_img)
        
        # Split the text into lines and store it
        column_texts.append(text.strip().split("\n"))

    # Combine the text row by row
    combined_text = []
    for row in zip(*column_texts):
        combined_text.append(" ".join(row).strip())

    return "\n".join(combined_text)
# # Example usage
# path_to_pdf = '/Users/eacalder/Documents/Github/pdftotext/tests/output_page_2.pdf'
# images = convert_from_path(path_to_pdf)

# Save the first page as an image
image_path = "tests/page_image.png"
# images[0].save(image_path, "PNG")

# Extract text from the image, assuming 2 columns
columns = 2
# text = extract_columns(image_path, columns)
text = extract_text_from_columns(image_path, columns)

print(text)
