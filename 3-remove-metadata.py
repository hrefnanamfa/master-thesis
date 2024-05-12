import os
from PyPDF2 import PdfReader, PdfWriter

def remove_metadata(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as file:
        # Create a PdfReader object
        pdf_reader = PdfReader(file)

        # Create a PdfWriter object
        pdf_writer = PdfWriter()

        # Copy all pages from the original file to the writer
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Remove metadata
        pdf_writer.add_metadata({})

        # Create a new PDF file in write-binary mode
        with open(pdf_path, 'wb') as output_file:
            # Write the modified content to the new file
            pdf_writer.write(output_file)

if __name__ == "__main__":
    # Specify the directory containing the PDF files
    directory = "C:/Directory/Anonymous Data"

    # Loop through all PDF files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory, filename)

            # Remove metadata and overwrite the original file
            remove_metadata(file_path)

            print(f"Metadata removed for {file_path}")
