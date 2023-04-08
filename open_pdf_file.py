import os
import PyPDF2

def open_file():

    file = input("Enter the full path of the pdf file: ")

    if not os.path.isfile(file):
        print("Error: File does not exist. Please check the path again.")
        return None, False
    else:
        try:
            reader = PyPDF2.PdfReader(file)
            if reader.is_encrypted:
                print("\nFile is encrypted.\n")
                response = 'y'
                while response=='y':
                    password = input("Enter the password to decrypt the pdf file: ")
                    if reader.decrypt(password):
                        return reader, True
                    else:
                        print("Wrong password.")
                        response = input("Try again? y/n: ")
                return None, False
            else:
                print("File opened successfully.")
                return reader, True
        except PyPDF2.utils.PdfReadError:
            print("Error: unable to read PDF file")
            return None, False
        except Exception as e:
            print(f"Error: {e}")
            return None, False