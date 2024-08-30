from PyPDF2 import PdfReader, PdfWriter

def extract_page(input_pdf_path, output_pdf_path, page_number):
    # Open the input PDF file
    with open(input_pdf_path, "rb") as input_pdf_file:
        # Create a PDF reader object
        pdf_reader = PdfReader(input_pdf_file)
        
        # Create a PDF writer object
        pdf_writer = PdfWriter()
        
        # Add the specified page to the writer object (page_number - 1 because it's zero-indexed)
        pdf_writer.add_page(pdf_reader.pages[page_number - 1])
        
        # Write the new PDF with the single page
        with open(output_pdf_path, "wb") as output_pdf_file:
            pdf_writer.write(output_pdf_file)

# Example usage
path_to_pdf = '/Users/eacalder/Documents/brewster/financials/Brewster_July_2024_financials.pdf'
output_pdf = "tests/output_page_2.pdf"  # Path to save the output PDF file
page_number = 2  # Page to extract

extract_page(path_to_pdf, output_pdf, page_number)

print(f"Page {page_number} has been saved to {output_pdf}.")
