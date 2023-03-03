import logging

BASE_LOGGING_CONFIG = {
    "filename": "parser_sto.log",
    "format": "%(asctime)s %(levelname)s:%(message)s",
}

LOGGING_CONFIG_ON_ERROR = {
    "level": logging.CRITICAL,
    **BASE_LOGGING_CONFIG,
}


def log_error(error: Exception) -> None:
    """Log critical error message."""
    logging.basicConfig(**LOGGING_CONFIG_ON_ERROR)
    logging.critical(error)
