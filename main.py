from PyPDF2 import PdfMerger

PDF_FILE = ["PDF_file/Python Notes.pdf", "PDF_file/python_revision_notes.pdf"]

merge = PdfMerger()

for new_pdf in PDF_FILE:
    merge.append(new_pdf)

merge.write("merge_pdf_file.pdf")
merge.close()