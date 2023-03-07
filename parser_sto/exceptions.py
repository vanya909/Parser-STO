class ParsingError(Exception):
    """Base parsing-related error."""

    message: str = ""

    def __init__(self, **kwargs: str) -> None:
        """Format message."""
        self.message = self.message.format(**kwargs)
        super().__init__(self.message)


class MissingInputFile(ParsingError):
    """Error when input filed was not found in project directory."""

    message: str = (
        "Заданый входной файл {filename} не найден.\n"
        "Убедитесь, что такой файл существует."
    )


class MissingImageName(ParsingError):
    """Error when image name was not provided."""

    message: str = (
        "Отсутствует имя изображения для {image}.\n"
        "Для вставки изображения необходимо указать его имя в треугольных "
        "скобках сразу после амперсанда. Например:\n"
        "&<picture1.png> Полезный рисунок.\n"
        "или\n"
        "&<picture1> Полезный рисунок."
    )


class MissingImage(ParsingError):
    """Error when image with provided name was not found."""

    message: str = (
        "Изображение с именем {imagename} не найдено.\n"
        "Убедитесь, что в папке {picturesfolder} есть изображение "
        "с именем {imagename}"
    )


class MissingConfigSection(ParsingError):
    """Error when certain config section is not presented in `ini` file."""

    message: str = (
        "Секция `{section}` не была найдена в `ini` файле.\n"
        "Убедитесь, что такая секция присутствует."
    )


class MissingConfigSetting(ParsingError):
    """Error when certain config setting is not presented in `ini` file."""

    message: str = (
        "`{setting}` не был найден в `ini` файле в секции `{section}`.\n"
        "Убедитесь, что в секции `{section}` есть поле `{setting}`."
    )
