import docx
from docx.document import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Mm, Pt

from .utils import get_project_directory_name, get_screenshots_directory_name


class DocxWriter:
    """Class to write data to `docx` document."""

    def __init__(self):
        """Init document."""

        # Mapping defines which format method will be used according to format
        # symbol found on the line
        self.FORMAT_MAPPING = {
            "\\*": self.switch_keep_with_next,
            "\\!": self.add_bold_run,
            "&": self.add_image,
            "": self.add_run,
        }

        self.doc: Document = docx.Document()
        self.picture_count = 0
        self.keep_with_next = False

        normal_style = self.doc.styles["Normal"]
        self.init_font(normal_style.font)
        self.init_format(normal_style.paragraph_format)
        self.init_a4(self.doc.sections[0])

    def init_a4(self, section):
        """Init A4 document."""
        section.page_height = Mm(297)
        section.page_width = Mm(210)

    def init_font(self, font):
        """Init font of the document."""
        font.name = "Times New Roman"
        font.size = Pt(14)

    def init_format(self, paragraph_format):
        """Init format of the document."""
        paragraph_format.first_line_indent = Cm(1.25)
        paragraph_format.space_after = 0

    def write_to_doc(self, text: str):
        """Write text to document."""
        format_symbol = self.parse_format_symbols(text)
        format_method = self.FORMAT_MAPPING[format_symbol]
        clean_text = text.strip(format_symbol).strip()

        format_method(clean_text)

    def get_text_paragraph(
        self,
        align_center: bool = False,
    ):
        """Return prepared text paragraph."""
        par = self.doc.add_paragraph()
        par.paragraph_format.keep_with_next = self.keep_with_next

        if align_center:
            par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

        return par

    def add_run(self, text: str):
        """Add paragraph with plain text."""
        par = self.get_text_paragraph()
        run = par.add_run(text)
        return run

    def add_bold_run(self, text: str):
        """Add paragraph with bold text."""
        run = self.add_run(text)
        run.bold = True

    def add_image(self, text: str = ""):
        """Add image to paragraph."""
        par = self.get_text_paragraph(align_center=True)
        par.paragraph_format.first_line_indent = 0
        run = par.add_run()

        self.picture_count += 1
        run.add_picture(self.picture_path)

        picture_description = f" – {text}" if len(text) else ""
        image_text = par.add_run(f"\n{self.picture_name}{picture_description}")

        font = image_text.font
        font.size = Pt(12)

    def switch_keep_with_next(self, *args):
        """Switch `self.keep_with_next`."""
        self.keep_with_next = not self.keep_with_next

    def parse_format_symbols(self, text: str) -> str:
        """Return format symbol from given text.

        If format symbols are not presented in the string, then return just
        empty string.

        """
        for symbol in self.FORMAT_MAPPING:
            if text.startswith(symbol):
                return symbol
        return ""

    @property
    def picture_name(self) -> str:
        """Standard name of picture."""
        return f"Рисунок {self.picture_count}"

    @property
    def picture_path(self) -> str:
        """Path to picture."""
        return (
            f"{get_project_directory_name()}/"
            f"{get_screenshots_directory_name()}/"
            f"{self.picture_count}.png"
        )

    def save_docx(self, name: str):
        """Save `docx` file."""
        self.doc.save(name)
