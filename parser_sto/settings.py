from .constants import TITLE_CONSTANTS
from .utils import get_config_setting

TITLE_SETTINGS = {
    constant: get_config_setting(constant, section="title")
    for constant in TITLE_CONSTANTS
}
