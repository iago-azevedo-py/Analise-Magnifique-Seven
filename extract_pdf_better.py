import PyPDF2

pdf_path = r"Métodos - Iago Santos Azevedo - Seções 1, 2 e 3 do trabalho final.pdf"

full_text = ""
with open(pdf_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        full_text += page.extract_text()

# Save to text file for better viewing
with open('conteudo_pdf.txt', 'w', encoding='utf-8') as f:
    f.write(full_text)

print("Conteúdo extraído e salvo em conteudo_pdf.txt")
print(f"\nPrimeiros 2000 caracteres:\n")
print(full_text[:2000])
