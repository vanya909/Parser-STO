from .parser_sto import DocxWriter
from . import utils


@utils.handle_error
def main() -> None:
    """Create document, write data from input file and save it."""
    docx_writer = DocxWriter()
    out = utils.get_full_output_file_name()

    with utils.get_input_file(encoding="utf-8") as ipdata:
        for line in ipdata:
            docx_writer.write_to_doc(line.rstrip("\n"))

    docx_writer.save_docx(out)
    utils.print_success("Успешно")


if __name__ == "__main__":
    main()
