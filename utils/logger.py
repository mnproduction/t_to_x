import logging
from settings.config import DEBUG_STATE_CONSOLE, DEBUG_STATE_FILE

class ColorFormatter(logging.Formatter):
    COLORS = {
        'DEBUG':    '\x1b[1;38;5;031m',     # blue color for DEBUG
        'INFO':     '\x1b[1;38;5;082m',     # green color for INFO
        'WARNING':  '\x1b[1;38;5;214m',     # yellow color for WARNING
        'ERROR':    '\x1b[1;38;5;160m',     # red color for ERROR
        'CRITICAL': '\x1b[1;48;5;124m',     # red background for CRITICAL
        'RESET':    '\x1b[0m',              # reset colors
    }


    def format(self, record):
        record_color = self.COLORS.get(record.levelname, '')
        record_reset = self.COLORS.get('RESET', '')

        levelname = record.levelname
        colored_levelname = f"{record_color}{levelname}{record_reset}"

        record.levelname = colored_levelname

        message = super().format(record)

        record.levelname = levelname

        return message.encode('utf-8').decode('ascii', 'ignore')

    def testcase():
        # Creating logger object
        logger = logging.getLogger(__name__)

        # Creating handler for output to console
        console_handler = logging.StreamHandler()

        # Creating formatter with color format
        formatter = ColorFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Attaching handler to logger
        logger.addHandler(console_handler)

        # Setting logging level
        logger.setLevel(logging.DEBUG)

        # Setting formatter for handler
        console_handler.setFormatter(formatter)

        # Writing log messages
        logger.debug('Debug message')
        logger.info('Info message')
        logger.warning('Warning message')
        logger.error('Error message')
        logger.critical('Critical message')
        
def setup_logger(name, log_to_console=DEBUG_STATE_CONSOLE, log_to_file=DEBUG_STATE_FILE, file_name='logging.log'):
    '''
    Function to set up logger
    :param log_to_console: logging to console
    :param log_to_file: logging to file
    :param file_name: file name for log
    :return: logger object
    '''
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False  # Disable sending messages to parent loggers

    if not logger.handlers:  # Add handlers only if they don't exist yet
        if log_to_console:
            console_handler = logging.StreamHandler()
            formatter = ColorFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        if log_to_file:
            file_handler = logging.FileHandler(file_name, encoding='utf-8')
            file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

    return logger
