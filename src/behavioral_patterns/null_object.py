import abc


class Logger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def log(self, message: str):
        pass


class ConsoleLogger(Logger):
    def log(self, message: str):
        print(message)


class FileLogger(Logger):
    def log(self, message: str):
        f = open("log.txt", "w+")
        f.write(message + "\n")
        f.close()


class NullLogger(Logger):
    def log(self, message: str):
        pass


class LoggerFactory:
    @staticmethod
    def get_logger(logger_type: str) -> Logger:
        if "console" == logger_type:
            return ConsoleLogger()
        elif "file" == logger_type:
            return FileLogger()

        return NullLogger()


def main():
    logger = LoggerFactory.get_logger("console")
    logger.log("This message is logger in the console")

    logger = LoggerFactory.get_logger("another-thing")
    logger.log("You won't see this message anywhere")


if __name__ == "__main__":
    main()
