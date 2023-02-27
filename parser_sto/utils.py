import configparser
import os
from contextlib import contextmanager

from rich import print as rprint
from rich.panel import Panel

from .constants import (
    INPUT_FILE_NAME,
    OUTPUT_DIRECTORY_NAME,
    OUTPUT_FILE_NAME,
    SETTINGS_FILE,
)
from .exceptions import (
    MissingConfigSection,
    MissingConfigSetting,
    MissingInputFile,
    ParsingError,
)
from .log_utils import log_error

config = configparser.ConfigParser()
config.read(SETTINGS_FILE)
main_config = config["main"]


def handle_error(func):
    """Decorator to handle occurred error."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            message = "Some unknown error occurred"
            if isinstance(error, ParsingError):
                message = str(error)
            print_error(message)
            log_error(error)
            raise SystemExit()

    return inner


@handle_error
def get_config_setting(setting: str, section: str = "main") -> str:
    """Return setting from config.

    Raises:
        MissingConfigSection: If `section` was not found in config `ini` file.
        MissingConfigSetting: If `setting` was not found in config `ini` file.

    """
    if section not in config:
        raise MissingConfigSection(section=section)

    section_config = config[section]
    if setting not in section_config:
        raise MissingConfigSetting(setting=setting, section=section)

    return beautify_string(section_config[setting])


def get_project_directory_name() -> str:
    """Return root directory of project."""
    return os.path.dirname(os.path.realpath(__file__))


@contextmanager
def get_input_file(*args, **kwargs):
    """Context manager to get and open input file or raise error.

    Raises:
        MissingInputFile: If input file with provided name was not found.

    """
    input_filename = (
        f"{get_project_directory_name()}/"
        f"{get_config_setting(INPUT_FILE_NAME)}"
    )

    if not os.path.isfile(input_filename):
        raise MissingInputFile(filename=input_filename)

    with open(input_filename, **kwargs) as ipdata:
        yield ipdata


def get_full_output_file_name():
    """Return output file name."""
    output_directory = get_config_setting(OUTPUT_DIRECTORY_NAME)
    # Append slash only if directory is not empty
    output_directory += "/" if output_directory else ""
    full_out_directory = f"{get_project_directory_name()}/{output_directory}"

    if output_directory and not os.path.isdir(full_out_directory):
        os.mkdir(full_out_directory)

    output_filename = (
        f"{full_out_directory}/"
        f"{get_config_setting(OUTPUT_FILE_NAME)}"
    )

    return output_filename


def beautify_string(string: str) -> str:
    """Strip quotes."""
    return string.strip("'").strip('"')


def print_success(text: str):
    """Print success message."""
    rprint(Panel(text, style="green bold"))


def print_error(text: str):
    """Print error message."""
    rprint(Panel(text, style="red bold"))
