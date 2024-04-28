"""Logging utilities for package."""

import logging
from pathlib import Path


class FuncNameExceptionFilter(logging.Filter):
    """A logging filter that filters by function name and log level."""

    def __init__(self, func_name: str, level: int = logging.ERROR):
        """Initialize the filter.

        :param func_name: The name of the function to filter by.
        :param level: The logging level to filter by.
        """
        # set the function name and log level to private attributes
        self._func_name = func_name
        self._log_level = level

    def filter(self, record):
        """Filter the log record based on function name and log level.

        :param record: The log record to filter.
        :return: True if the record should be logged, False otherwise.
        """
        # Check if the record has the correct function name and log level
        if record.funcName == self._func_name and record.levelno >= self._log_level:
            return True
        else:
            return False


def setup_func_exception_log_handler(
    func_name: str,
    file_path: str | Path = None,
    log_level: int = logging.ERROR,
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
):
    """Setup a logging handler that filters by function name and log level.

    Can setup either a file handler or a stream handler based on file_path. can
    configured to filter by log level and function name and has configurable log formatter.

    :param func_name: The name of the function to filter by.
    :param file_path: The path to the file to write logs to. If None, logs will be written to stderr.
    :param log_level: The logging level to filter by.
    :param log_format: The format of the log messages.
    :return: A logging handler.
    """
    # Setup the handler, if file_path is None, use a stream handler, otherwise use a file handler
    if file_path is None:
        handler = logging.StreamHandler()
    else:
        handler = logging.FileHandler(file_path, mode="w")

    # Set the log level, add the filter, and set the formatter
    handler.setLevel(log_level)
    handler.addFilter(FuncNameExceptionFilter(func_name, log_level))
    handler.setFormatter(logging.Formatter(log_format))

    # Return the handler
    return handler
