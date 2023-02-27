class ParsingError(Exception):
    """Base parsing-related error."""

    message: str = ""

    def __init__(self, *args, **kwargs):
        self.message = self.message.format(**kwargs)
        super().__init__(self.message, *args)


class MissingInputFile(ParsingError):
    """Error when input filed was not found in project directory."""

    message: str = (
        "Заданый входной файл {filename} не найден.\n"
        "Убедитесь, что такой файл существует."
    )

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class MissingConfigSection(ParsingError):
    """Error when certain config section is not presented in `ini` file."""

    message: str = (
        "Секция `{section}` не была найдена в `ini` файле.\n"
        "Убедитесь, что такая секция присутствует."
    )

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class MissingConfigSetting(ParsingError):
    """Error when certain config setting is not presented in `ini` file."""

    message: str = (
        "`{setting}` не был найден в `ini` файле в секции `{section}`.\n"
        "Убедитесь, что в секции `{section}` есть поле `{setting}`."
    )

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
