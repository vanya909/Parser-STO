import os
from parser_sto import DocxWriter

docx_writer = DocxWriter()
filename = 'input data.txt'

if '_MEIPASS2' in os.environ:
    filename = os.path.join(os.environ['_MEIPASS2'], filename)

with open(filename, encoding='utf-8') as ipdata:
    for line in ipdata:
        docx_writer.write_to_doc(line.rstrip('\n'))

docx_writer.save_docx('Отчет.docx')
