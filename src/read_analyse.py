import PyPDF2
import open_pdf_file

def read_data():
	for i in range(len(reader.pages)):
	    page = reader.pages[i]
	    text = page.extract_text()
	    print(text)

reader, ack = open_pdf_file.open_file()
if ack:
	read_data()