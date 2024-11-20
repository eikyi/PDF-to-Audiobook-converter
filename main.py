# importing required classes
from pypdf import PdfReader

path = input("Input path to PDF file: ")
# creating a pdf reader object
reader = PdfReader(path)

# printing number of pages in pdf file
print(len(reader.pages))

# creating a page object
page = reader.pages[0]

# extracting text from page
print(page.extract_text())