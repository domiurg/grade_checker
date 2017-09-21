from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter #process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from cStringIO import StringIO


def pdf_to_text(pdfname):
    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    text = []

    # Extract text
    fp = file(pdfname, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        text.append(sio.getvalue())
    fp.close()

    # Cleanup
    device.close()
    sio.close()
    return text


def main():
    files = ['final.1.pdf', 'final.2.pdf']
    for file in files:
        lines = pdf_to_text(file)

        for line in lines:
            id = []
            grade = []
            curr = line.split('\n')
            if curr[0] == 'ID':
                curr = curr[11:]
            count = 0
            for i in range(0, len(curr) - 1):
                if curr[i] != '':
                    if count == 0:
                        id.append(curr[i])
                    elif count == 3:
                        grade.append(curr[i])
                else:
                    count += 1

            for j in range(0, len(grade) - 1):
                if grade[j] == 'F':
                    print 'Student ' + id[j] + ' Failed course'


if __name__ == '__main__':
    main()
