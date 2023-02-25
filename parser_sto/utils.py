import configparser
import os
from contextlib import contextmanager

from rich import print as rprint
from rich.panel import Panel

from .exceptions import MissingInputFile, ParsingError
from .log_utils import log_error

SETTINGS_FILE = "parsersettings.ini"

config = configparser.ConfigParser()
config.read(SETTINGS_FILE)
main_config = config["main"]


def get_project_directory_name() -> str:
    """Return root directory of project."""
    return os.path.dirname(os.path.realpath(__file__))


def get_input_file_name() -> str:
    """Return name of the input file."""
    return beautify_string(main_config["InputFileName"])


def get_output_file_name() -> str:
    """Return name of the output file."""
    return beautify_string(main_config["OutputFileName"])


def get_screenshots_directory_name() -> str:
    """Return name of the screenshots folder from config file."""
    return beautify_string(main_config["ScreenshotsDirectoryName"])


def get_out_directory_name() -> str:
    """Return name out folder."""
    return beautify_string(main_config["OutputDirectoryName"])


@contextmanager
def get_input_file(*args, **kwargs):
    """Context manager to get and open input file or raise error.

    Raises:
        MissingInputFile: If input file with provided name was not found.

    """
    input_filename = (
        f"{get_project_directory_name()}/"
        f"{get_input_file_name()}"
    )

    if not os.path.isfile(input_filename):
        raise MissingInputFile(input_filename)

    with open(input_filename, **kwargs) as ipdata:
        yield ipdata


def get_full_output_file_name():
    """Return output file name."""
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


def handle_error(func):
    """Decorator to handle occurred error."""

    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as error:
            message = "Some unknown error occurred"
            if isinstance(error, ParsingError):
                message = error.message
            print_error(message)
            log_error(error)

    return inner
