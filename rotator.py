import PyPDF2


def rotate_pdf_page(pdf_in, page_number, angle):
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        if pagenum==int(page_number)-1:
            print(1111)
            page.rotateClockwise(int(angle))
        pdf_writer.addPage(page)  
    return pdf_writer