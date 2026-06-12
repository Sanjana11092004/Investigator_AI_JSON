from pathlib import Path

from watchdog.events import (
    FileSystemEventHandler
)

from watchdog.observers import Observer

from loguru import logger

from src.config.settings import settings

from src.ingestion.ingestion_service import (
    IngestionService
)


class IncomingFileHandler(
    FileSystemEventHandler
):

    def __init__(self):

        self.ingestion_service = (
            IngestionService()
        )

    def on_created(
        self,
        event
    ):

        if event.is_directory:
            return

        try:

            result = (
                self.ingestion_service
                .process_file(
                    event.src_path
                )
            )

            logger.info(result)

        except Exception as e:

            logger.error(str(e))


def start_watcher():

    settings.INCOMING_DIR.mkdir(
        exist_ok=True
    )

    observer = Observer()

    observer.schedule(
        IncomingFileHandler(),
        str(settings.INCOMING_DIR),
        recursive=False
    )

    observer.start()

    logger.info(
        "Watching incoming folder..."
    )

    try:

        import time

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()


if __name__ == "__main__":

    start_watcher()