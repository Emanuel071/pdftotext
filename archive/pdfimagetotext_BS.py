from pdf2image import convert_from_path
import cv2
import pytesseract
import os

# Step 1: Convert PDF pages to images
def convert_pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i + 1}.png')
        image_path = image_path[1:]
        print("image saved")
        print(image_path)
        # image.save(image_path, 'PNG')
        
        # image_paths.append(image_path)
    return image_paths

# Step 2: Process each image (already black and white)
def process_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

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

    # OCR
    text = pytesseract.image_to_string(deskewed)
    return text

# Step 3: Run the entire process
pdf_path = '/Users/eacalder/Documents/brewster/financials/Brewster_July_2024_financials.pdf'
output_folder = 'path/to/output/images'

# Convert PDF to images
image_paths = convert_pdf_to_images(pdf_path, output_folder)

# Extract text from each image
for image_path in image_paths:
    extracted_text = process_image(image_path)
    print(f'Text from {os.path.basename(image_path)}:')
    print(extracted_text)
