from .parser_sto import DocxWriter
from .utils import (
    get_full_output_file_name,
    get_input_file,
    handle_error,
    print_success,
)


@handle_error
def main():
    """Create document, write data from input file and save it."""
    docx_writer = DocxWriter()
    out = get_full_output_file_name()

    with get_input_file(encoding="utf-8") as ipdata:
        for line in ipdata:
            docx_writer.write_to_doc(line.rstrip("\n"))

    docx_writer.save_docx(out)
    print_success("Успешно")


if __name__ == "__main__":
    main()
