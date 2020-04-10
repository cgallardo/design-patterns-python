import abc
from enum import Enum


class LogLevel(Enum):
    NONE = 1
    INFO = 2
    DEBUG = 3
    WARNING = 4
    ERROR = 5
    FUNCTIONAL_MESSAGE = 6
    FUNCTIONAL_ERROR = 7
    ALL = 8


class Logger(metaclass=abc.ABCMeta):
    def __init__(self, levels) -> None:
        self._next = None
        self.log_levels = []

        for level in levels:
            self.log_levels.append(level)

    def set_next(self, next_logger):
        self._next = next_logger
        return self._next

    def message(self, msg: str, severity: LogLevel) -> None:
        if LogLevel.ALL in self.log_levels or severity in self.log_levels:
            self.write_message(msg)

        if self._next is not None:
            self._next.message(msg, severity)

    @abc.abstractmethod
    def write_message(self, msg: str) -> None:
        raise NotImplementedError("You should implement this method.")


class ConsoleLogger(Logger):
    def write_message(self, msg: str) -> None:
        print("Writing to console:", msg)


class EmailLogger(Logger):
    def write_message(self, msg: str) -> None:
        print("Sending via email: {}".format(msg))


class FileLogger(Logger):
    def write_message(self, msg: str) -> None:
        print("Writing to log file: {}".format(msg))


def main():
    logger = ConsoleLogger([LogLevel.ALL])
    email_logger = logger.set_next(
        EmailLogger([LogLevel.FUNCTIONAL_MESSAGE, LogLevel.FUNCTIONAL_ERROR])
    )
    email_logger.set_next(
        FileLogger([LogLevel.WARNING, LogLevel.ERROR])
    )

    logger.message("Entering function ProcessOrder().", LogLevel.DEBUG)
    logger.message("Order record retrieved.", LogLevel.INFO)
    logger.message("Customer Address details missing in Branch DataBase.", LogLevel.WARNING)
    logger.message("Customer Address details missing in Organization DataBase.", LogLevel.ERROR)
    logger.message("Unable to Process Order ORD1 Dated D1 for customer C1.", LogLevel.FUNCTIONAL_ERROR)
    logger.message("OrderDispatched.", LogLevel.FUNCTIONAL_MESSAGE)


if __name__ == "__main__":
    main()
