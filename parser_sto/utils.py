import configparser
import os

from rich import print as rprint
from rich.panel import Panel

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


def beautify_string(string: str) -> str:
    """Strip quotes."""
    return string.strip("'").strip('"')


def print_success(text: str):
    """Print success message."""
    rprint(Panel(text, style="green bold"))


def print_error(text: str):
    """Print error message."""
    rprint(Panel(text, style="red bold"))
