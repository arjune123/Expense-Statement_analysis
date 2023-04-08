import os
import PyPDF2

file = input("Enter the full path of the pdf file: ")

if not os.path.isfile(file):
    print("Error: File does not exist. Please check the path again.")

else:
    try:
        reader = PyPDF2.PdfReader(file)
        if reader.is_encrypted:
            print("\nFile is encrypted.\n")
            response = 'y'
            while response=='y':
                password = input("Enter the password to decrypt the pdf file: ")
                if reader.decrypt(password):
                    break
                else:
                    print("Wrong password.")
                    response = input("Try again? y/n: ")

            if reader.decrypt(password):
                print("Successfully decrypted. File opened successfully.\n")
        else:
            print("File opened successfully.")
    except PyPDF2.utils.PdfReadError:
        print("Error: unable to read PDF file")
    except Exception as e:
        print(f"Error: {e}")

for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()