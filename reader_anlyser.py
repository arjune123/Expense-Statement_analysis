import PyPDF2

file = input("Enter the full path of the pdf file: ")

reader = PyPDF2.PdfReader(file)
"""
To do:
error handling if the pdf file does not open.

"""

for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()