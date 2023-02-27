import re
from dataclasses import dataclass


class ParsingError(Exception):
    """Base parsing-related error."""

    message: str = ""

    def get_message_placeholders(self) -> list[str]:
        """Return all placeholders from the message."""
        return re.findall(r"{(\w+)}", self.message)

    def __str__(self) -> str:
        """Return formatted message.

        Using hacky way to format message by those attributes of class which
        presented in message as placeholders.

        """
        placeholders = {
            attr: getattr(self, attr)
            for attr in dir(self)
            if attr in self.get_message_placeholders()
        }
        message = self.message.format(**placeholders)
        return message


@dataclass
class MissingInputFile(ParsingError):
    """Error when input filed was not found in project directory."""

    filename: str

    message: str = (
        "Заданый входной файл {filename} не найден.\n"
        "Убедитесь, что такой файл существует."
    )


@dataclass
class MissingConfigSection(ParsingError):
    """Error when certain config section is not presented in `ini` file."""

    section: str

    message: str = (
        "Секция `{section}` не была найдена в `ini` файле.\n"
        "Убедитесь, что такая секция присутствует."
    )


@dataclass
class MissingConfigSetting(ParsingError):
    """Error when certain config setting is not presented in `ini` file."""

    setting: str
    section: str

    message: str = (
        "`{setting}` не был найден в `ini` файле в секции `{section}`.\n"
        "Убедитесь, что в секции `{section}` есть поле `{setting}`."
    )
