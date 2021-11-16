from parser_sto import DocxWriter


docx_writer = DocxWriter()

with open('input data.txt', encoding='utf-8') as ipdata:
    for line in ipdata:
        docx_writer.write_to_doc(line.rstrip('\n'))

docx_writer.save_docx('Отчет.docx')
