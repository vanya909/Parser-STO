import logging
import os

from .parser_sto import DocxWriter
from .utils import (
    get_input_file_name,
    get_out_directory_name,
    get_output_file_name,
    get_project_directory_name,
    print_error,
    print_success,
)


def main():
    docx_writer = DocxWriter()
    input_filename = (
        f"{get_project_directory_name()}/"
        f"{get_input_file_name()}"
    )

    output_directory = get_out_directory_name()
    # Append slash only if directory is not empty
    output_directory += "/" if output_directory else ""
    full_out_directory = f"{get_project_directory_name()}/{output_directory}"

    if output_directory and not os.path.isdir(full_out_directory):
        os.mkdir(full_out_directory)

    output_filename = (
        f"{full_out_directory}/"
        f"{get_output_file_name()}"
    )

    with open(input_filename, encoding="utf-8") as ipdata:
        for line in ipdata:
            docx_writer.write_to_doc(line.rstrip("\n"))

    docx_writer.save_docx(output_filename)
    print_success("Successfull!")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.CRITICAL,
        filename="parser_sto.log",
        format="%(asctime)s %(levelname)s:%(message)s",
    )
    try:
        main()
    except Exception as e:
        print_error("Some error ocured")
        logging.critical(e)
