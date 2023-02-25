class ParsingError(Exception):
    """Base parsing-related error."""

    message: str = ""


class MissingInputFile(ParsingError):
    """Error when input filed was not found in project directory."""

    message: str = (
        "Заданый входной файл {filename} не найден.\n"
        "Убедитесь, что такой файл существует."
    )

    def __init__(self, filename: str, *args, **kwargs):
        self.message = self.message.format(filename=filename)
        super().__init__(self.message, *args, **kwargs)
