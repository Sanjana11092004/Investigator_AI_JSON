from pathlib import Path

from loguru import logger

from src.config.settings import settings


def configure_logging() -> None:

    settings.LOG_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    logger.remove()

    logger.add(
        settings.LOG_DIR / "application.log",
        rotation="10 MB",
        retention="30 days",
        level="INFO",
        enqueue=True
    )

    logger.add(
        sink=lambda msg: print(msg, end=""),
        level="INFO"
    )