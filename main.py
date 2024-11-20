# importing required classes
from pypdf import PdfReader
from converter import Converter

path = input("Input path to PDF file: ")
# creating a pdf reader object
reader = PdfReader(path)

# printing number of pages in pdf file
print(len(reader.pages))

# creating a page object
pages = reader.pages

#initialize the voice converter
converter = Converter()
#convert to audio
converter.search(pages)
