import logging
from settings.config import Config

config = Config()

class Logger:
    COLORS = {
        'DEBUG':    '\x1b[1;38;5;031m',     # blue color for DEBUG
        'INFO':     '\x1b[1;38;5;082m',     # green color for INFO
        'WARNING':  '\x1b[1;38;5;214m',     # yellow color for WARNING
        'ERROR':    '\x1b[1;38;5;160m',     # red color for ERROR
        'CRITICAL': '\x1b[1;48;5;124m',     # red background for CRITICAL
        'RESET':    '\x1b[0m',              # reset colors
    }

    def __init__(self, name, log_to_console=config.DEBUG_STATE_CONSOLE, log_to_file=config.DEBUG_STATE_FILE, file_name='logging.log'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False  # Disable sending messages to parent loggers

        if not self.logger.handlers:  # Add handlers only if they don't exist yet
            if log_to_console:
                console_handler = logging.StreamHandler()
                formatter = self.ColorFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                console_handler.setFormatter(formatter)
                self.logger.addHandler(console_handler)

            if log_to_file:
                file_handler = logging.FileHandler(file_name, encoding='utf-8')
                file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                file_handler.setFormatter(file_formatter)
                self.logger.addHandler(file_handler)

    class ColorFormatter(logging.Formatter):
        def format(self, record):
            record_color = Logger.COLORS.get(record.levelname, '')
            record_reset = Logger.COLORS.get('RESET', '')

            levelname = record.levelname
            colored_levelname = f"{record_color}{levelname}{record_reset}"

            record.levelname = colored_levelname

            message = super().format(record)

            record.levelname = levelname

            return message.encode('utf-8').decode('ascii', 'ignore')

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
