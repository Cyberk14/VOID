import fitz  # PyMuPDF

def pdf_to_text(pdf_path, output_text_file):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text = ""

    # Iterate through each page
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
        text += "\n\npage ended\n\n"  # Add a newline after each page's text

    # Save the extracted text to a file
    with open(output_text_file, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

    print(f"Text extracted and saved to {output_text_file}")

# Usage


pdf_path = 'D:\\New folder\\VOID\\VOID.pdf'
output_text_file = 'output_text_file.txt'
pdf_to_text(pdf_path, output_text_file)
