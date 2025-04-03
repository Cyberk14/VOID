# this file will be used to see/spot the info the internet and the files the user  will have complied inform of .pdf files and images.
import fitz

def see(data: str, image=None):
    if data and image is True:
        return data, image
    
    elif image is None:
        return data

def read_pdf(pdf_path: str, output_text_file: str):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text = ""

    # Iterate through each page
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
        text += "page ended \n"  # Add a newline after each page's text

    # Save the extracted text to a file
    with open(output_text_file, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

    print(f"Text extracted and saved to {output_text_file}")

    return text
