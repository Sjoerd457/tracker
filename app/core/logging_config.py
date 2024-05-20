import logging
import os
from logging.config import dictConfig
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

root = Path('__file__').resolve().parents[2]

# Ensure the 'logs' directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(pathname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "default",
            "filename": "logs/app.log",
            "when": "midnight",
            "interval": 1,
            "backupCount": 5,
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"],
    },
}

def setup_logging():
    dictConfig(logging_config)

if __name__ == "__main__":
    setup_logging()
    logging.info("Test logging")
