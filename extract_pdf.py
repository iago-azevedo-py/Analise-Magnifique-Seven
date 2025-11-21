import PyPDF2

pdf_path = r"Métodos - Iago Santos Azevedo - Seções 1, 2 e 3 do trabalho final.pdf"

with open(pdf_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)
    
    print(f"Total de páginas: {num_pages}\n")
    print("="*80)
    
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        print(f"\n--- PÁGINA {page_num + 1} ---\n")
        print(text)
        print("\n" + "="*80)
