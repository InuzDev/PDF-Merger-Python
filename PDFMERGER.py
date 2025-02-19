import PyPDF2
from PyPDF2 import PdfMerger

def delete_first_two_pages(input_pdf_path, output_pdf_path):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_pdf_file:
        reader = PyPDF2.PdfReader(input_pdf_file)
        writer = PyPDF2.PdfWriter()

        # Add pages to the writer, skipping the first two pages
        for page_num in range(2, len(reader.pages)):
            page = reader.pages[page_num]
            writer.add_page(page)

        # Write the output PDF file
        with open(output_pdf_path, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)

def merge_pdfs(input_paths, output_path):
    merger = PdfMerger()
    for path in input_paths:
        merger.append(path)
    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    # Example usage of delete_first_two_pages
    input_pdf_path = 'PDF_FILE1.pdf'  # Replace with your input PDF file path
    output_pdf_path = 'FIX_PDF_FILE1.pdf'  # Replace with your desired output PDF file path
    delete_first_two_pages(input_pdf_path, output_pdf_path)
    
    # Example usage of merge_pdfs
    merge_pdfs(["PDF_FILE.pdf", "FIX_PDF_FILE1.pdf"], "ConverterPDF.pdf")