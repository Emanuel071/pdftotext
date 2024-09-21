from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
from docx import Document

def convert_pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)

def convert_image_to_text(file):
    text = image_to_string(file)
    return text

def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img(pdf_file)
    balance_sheet_final_text = ''
    for pg, img in enumerate(images):
        
        if pg == 1:
            balance_sheet_final_text += convert_image_to_text(img)

    return balance_sheet_final_text
   
def string_var_to_word_doc(var_string):
    # Create a new Document
    doc = Document()

    # Add a paragraph with the string
    doc.add_paragraph(var_string)

    # Save the document
    # doc.save('tests/Brewster_July_2024_financials.docx')

    print("Document saved successfully.")


##MAIN##
# path_to_pdf = '/Users/eacalder/Documents/Github/pdftotext/tests/output_page_2.pdf'
# path_to_pdf = '/Users/eacalder/Documents/brewster/financials/Brewster_May_Financials_2024.pdf'
# path_to_pdf = '/Users/eacalder/Documents/brewster/financials/Brewster_March_2024_Financials.pdf'
path_to_pdf = '/Users/eacalder/Documents/brewster/financials/Brewster_June_financials_2024.pdf' #the one that is not working 
# path_to_pdf = '/Users/eacalder/Documents/brewster/financials/Brewster_July_2024_financials.pdf'
# path_to_pdf = '/Users/eacalder/Documents/brewster/financials/Brewster_April_2024_Financials.pdf'
# path_to_pdf = '/Users/eacalder/Documents/brewster/financials/Brewster_Feb_2024_financials.pdf'
# path_to_pdf = '/Users/eacalder/Documents/brewster/financials/Brewster_January_2024_Financials.pdf'

text_BS = get_text_from_any_pdf(path_to_pdf)

print(text_BS)
# Split the string by newline character
list_BS = text_BS.split("\n")

# Remove empty items ("" or None)
cleaned_list_BS = [item for item in list_BS if item]    

balance_sheet_dict = {}
print(f"length dict: {len(balance_sheet_dict)}")

if any(char.isdigit() for char in cleaned_list_BS[5]):
    print("here")
    if len(balance_sheet_dict) < 1:
        #ASSETS 
        # NAMING SETUP
        Operating_Checking        = cleaned_list_BS[5].rsplit(' ', 1)
        Reserve                   = cleaned_list_BS[8].rsplit(' ', 1)
        Accounts_Receivable       = cleaned_list_BS[11].rsplit(' ', 1)
        Washers_Dryers            = cleaned_list_BS[14].rsplit(' ', 1)
        Machinery_EQ              = cleaned_list_BS[15].rsplit(' ', 1)
        Loan_Fees                 = cleaned_list_BS[16].rsplit(' ', 1)
        Prepaid_Insurance         = cleaned_list_BS[19].rsplit(' ', 1)


        balance_sheet_dict[Operating_Checking[0]] = Operating_Checking[1]
        balance_sheet_dict[Reserve[0]] = Reserve[1]
        balance_sheet_dict[Accounts_Receivable[0]] = Accounts_Receivable[1]
        balance_sheet_dict[Washers_Dryers[0]] = Washers_Dryers[1]
        balance_sheet_dict[Machinery_EQ[0]] = Machinery_EQ[1]
        balance_sheet_dict[Loan_Fees[0]] = Loan_Fees[1]
        balance_sheet_dict[Prepaid_Insurance[0]] = Prepaid_Insurance[1]

        #LIABILITIES 
        Loan_Payable                 = cleaned_list_BS[24].rsplit(' ', 1)
        Prepaid_Common_Fees          = cleaned_list_BS[25].rsplit(' ', 1)
        Accounts_Payable             = cleaned_list_BS[26].rsplit(' ', 1)
        Insurance_Proceeds           = cleaned_list_BS[27].rsplit(' ', 1)

        balance_sheet_dict[Loan_Payable[0]] = Loan_Payable[1]
        balance_sheet_dict[Prepaid_Common_Fees[0]] = Prepaid_Common_Fees[1]
        balance_sheet_dict[Accounts_Payable[0]] = Accounts_Payable[1]
        balance_sheet_dict[Insurance_Proceeds[0]] = Insurance_Proceeds[1]

        #EQUITY
        Fund_Balance                 = cleaned_list_BS[30].rsplit(' ', 1)
        Reserve_Retained_Earnings    = cleaned_list_BS[31].rsplit(' ', 1)
        Net_Income                   = cleaned_list_BS[32].rsplit(' ', 1)

        balance_sheet_dict[Fund_Balance[0]] = Fund_Balance[1]
        balance_sheet_dict[Reserve_Retained_Earnings[0]] = Reserve_Retained_Earnings[1]
        balance_sheet_dict[Net_Income[0]] = Net_Income[1]

        print(balance_sheet_dict)

else:
    if len(balance_sheet_dict) < 1:
        #ASSETS 
        # NAMING SETUP
        Operating_Checking        = cleaned_list_BS[5]
        Reserve                   = cleaned_list_BS[7]
        Accounts_Receivable       = cleaned_list_BS[10]
        Washers_Dryers            = cleaned_list_BS[14]
        Machinery_EQ              = cleaned_list_BS[15]
        Loan_Fees                 = cleaned_list_BS[16]
        Prepaid_Insurance         = cleaned_list_BS[19]

        #LIABILITIES 
        Loan_Payable                 = cleaned_list_BS[24]
        Prepaid_Common_Fees          = cleaned_list_BS[25]
        Accounts_Payable             = cleaned_list_BS[26]
        Insurance_Proceeds           = cleaned_list_BS[27]

        #EQUITY
        Fund_Balance                 = cleaned_list_BS[30]
        Reserve_Retained_Earnings    = cleaned_list_BS[31]
        Net_Income                   = cleaned_list_BS[32]

        #ASSETS 
    # VALUE SETUP LOOPING
    balance_sheet_dict[Operating_Checking] = cleaned_list_BS[35]
    balance_sheet_dict[Reserve] = cleaned_list_BS[37]
    balance_sheet_dict[Accounts_Receivable] = cleaned_list_BS[39]
    balance_sheet_dict[Washers_Dryers] = cleaned_list_BS[41]
    balance_sheet_dict[Machinery_EQ] = cleaned_list_BS[42]
    balance_sheet_dict[Loan_Fees] = cleaned_list_BS[43]
    balance_sheet_dict[Prepaid_Insurance] = cleaned_list_BS[45]

    #LIABILITIES 
    balance_sheet_dict[Loan_Payable] = cleaned_list_BS[47]
    balance_sheet_dict[Prepaid_Common_Fees] = cleaned_list_BS[48]
    balance_sheet_dict[Accounts_Payable] = cleaned_list_BS[49]
    balance_sheet_dict[Insurance_Proceeds] = cleaned_list_BS[50]

    #EQUITY
    balance_sheet_dict[Fund_Balance] = cleaned_list_BS[52]
    balance_sheet_dict[Reserve_Retained_Earnings] = cleaned_list_BS[53]
    balance_sheet_dict[Net_Income] = cleaned_list_BS[54]

    print(balance_sheet_dict)

# if len(balance_sheet_dict) < 1:
#     #ASSETS 
#     # NAMING SETUP
#     Operating_Checking        = cleaned_list_BS[5]
#     Reserve                   = cleaned_list_BS[7]
#     Accounts_Receivable       = cleaned_list_BS[10]
#     Washers_Dryers            = cleaned_list_BS[14]
#     Machinery_EQ              = cleaned_list_BS[15]
#     Loan_Fees                 = cleaned_list_BS[16]
#     Prepaid_Insurance         = cleaned_list_BS[19]

#     #LIABILITIES 
#     Loan_Payable                 = cleaned_list_BS[24]
#     Prepaid_Common_Fees          = cleaned_list_BS[25]
#     Accounts_Payable             = cleaned_list_BS[26]
#     Insurance_Proceeds           = cleaned_list_BS[27]

#     #EQUITY
#     Fund_Balance                 = cleaned_list_BS[30]
#     Reserve_Retained_Earnings    = cleaned_list_BS[31]
#     Net_Income                   = cleaned_list_BS[32]


'''
# print(list_BS)

# for value,index in enumerate(list_BS):
#     print(f"index: {value}, value: {index} ")

# #ASSETS 
# Operating_Checking        = list_BS[8]
# Operating_Checking_value  = list_BS[48]
# Reserve                   = list_BS[10]
# Reserve_value             = list_BS[51]
# Accounts_Receivable       = list_BS[14]
# Accounts_Receivable_value = list_BS[54]
# Washers_Dryers            = list_BS[18]
# Washers_Dryers_value      = list_BS[57]
# Machinery_EQ              = list_BS[20]
# Machinery_EQ_value        = list_BS[58]
# Loan_Fees                 = list_BS[21]
# Loan_Fees_value           = list_BS[59]
# Prepaid_Insurance         = list_BS[26]
# Prepaid_Insurance_value   = list_BS[63]

# #LIABILITIES 
# Loan_Payable                 = list_BS[33]
# Loan_Payable_value           = list_BS[66]
# Prepaid_Common_Fees                 = list_BS[34]
# Prepaid_Common_Fees_value           = list_BS[67]
# Accounts_Payable                 = list_BS[35]
# Accounts_Payable_value           = list_BS[68]
# Insurance_Proceeds                 = list_BS[36]
# Insurance_Proceeds_value           = list_BS[69]

# #EQUITY
# Fund_Balance                 = list_BS[41]
# Fund_Balance_value           = list_BS[73]
# Reserve_Retained_Earnings                 = list_BS[42]
# Reserve_Retained_Earnings_value           = list_BS[74]
# Net_Income                 = list_BS[43]
# Net_Income_value           = list_BS[75]

balance_sheet_dict = {}

#ASSETS 
balance_sheet_dict[list_BS[8]] = list_BS[48]
balance_sheet_dict[list_BS[10]] = list_BS[51]
balance_sheet_dict[list_BS[14]] = list_BS[54]
balance_sheet_dict[list_BS[18]] = list_BS[57]
balance_sheet_dict[list_BS[20]] = list_BS[58]
balance_sheet_dict[list_BS[21]] = list_BS[59]
balance_sheet_dict[list_BS[26]] = list_BS[63]

#LIABILITIES 
balance_sheet_dict[list_BS[33]] = list_BS[66]
balance_sheet_dict[list_BS[34]] = list_BS[67]
balance_sheet_dict[list_BS[35]] = list_BS[68]
balance_sheet_dict[list_BS[36]] = list_BS[69]

#EQUITY
balance_sheet_dict[list_BS[41]] = list_BS[73]
balance_sheet_dict[list_BS[42]] = list_BS[74]
balance_sheet_dict[list_BS[43]] = list_BS[75]


print(balance_sheet_dict)



string_var_to_word_doc(text_BS)

print("Job successful.")
'''