from loguru import logger

from src.config.logging_config import (
    configure_logging
)

configure_logging()

logger.info(
    "Logger initialized successfully"
)