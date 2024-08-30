
import pdfplumber
import csv
import re

path_to_pdf = '/Users/eacalder/Documents/Github/pdftotext/tests/output_page_2.pdf'


with pdfplumber.open(path_to_pdf) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
    
    
    balance_sheet_text = text
    print(balance_sheet_text)    
    

        # # Try to locate the balance sheet section in the text
        # if "Balance Sheet" in text:
        #     balance_sheet_text = text
        #     break

# You can adjust the parsing logic based on your specific balance sheet format
# This is a basic approach and might need customization based on your PDF
lines = balance_sheet_text.split("\n")
print(lines)

# Prepare for CSV data
data = []

for line in lines:
    # Example regex to find lines that might contain numbers (simple assumption)
    if re.search(r'\d', line):
        # Split the line on whitespace and commas for CSV friendly formatting
        data.append([item.strip() for item in re.split(r'\s{2,}|\t|,', line)])
print(data)
