import logging
import os
from time import sleep
from parser_sto import DocxWriter

def main():
    docx_writer = DocxWriter()
    filename = 'input data.txt'

    if '_MEIPASS2' in os.environ:
        filename = os.path.join(os.environ['_MEIPASS2'], filename)

    with open(filename, encoding='utf-8') as ipdata:
        for line in ipdata:
            docx_writer.write_to_doc(line.rstrip('\n'))

    docx_writer.save_docx('Отчет.docx')
    print('Successfull! This window will automatically close in 3 seconds...')
    sleep(3)

if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL,
                        filename='parser_sto.log',
                        format='%(asctime)s %(levelname)s:%(message)s')
    try:
        main()
    except Exception as e:
        logging.critical(e)
