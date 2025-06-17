import logging
from typing import Optional

_DEFAULT_LOG_FORMAT = '%(asctime)s [%(levelname)s] %(name)s: %(message)s'


def setup_logging(level: int = logging.INFO, log_format: Optional[str] = None) -> None:
    """
    Set up logging configuration for the SDK.
    Args:
        level: Logging level (default: logging.INFO)
        log_format: Log message format (default: standard format)
    """
    logging.basicConfig(
        level=level,
        format=log_format or _DEFAULT_LOG_FORMAT
    )


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger instance for the SDK.
    Args:
        name: Logger name (default: None for root logger)
    Returns:
        logging.Logger instance
    """
    return logging.getLogger(name or 'owui_sdk') 