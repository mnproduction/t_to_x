# run: pytest tests/test_logger.py

import pytest
import logging
import os
from utils.logger import Logger  # Assuming your Logger class is in logger.py

@pytest.fixture(autouse=True)
def reset_logging():
    """Fixture to reset logging configuration before each test"""
    logging.shutdown()
    logging.getLogger().handlers = []
    yield
    logging.shutdown()
    logging.getLogger().handlers = []

def test_console_handler_added():
    """Tests adding a console handler"""
    logger = Logger(name='test_logger', log_to_console=True, log_to_file=False)
    handlers = logger.logger.handlers
    assert len(handlers) == 1
    assert isinstance(handlers[0], logging.StreamHandler)

def test_file_handler_added(tmp_path):
    """Tests adding a file handler"""
    test_log_file = tmp_path / "test.log"
    logger = Logger(name='test_logger', log_to_console=False, log_to_file=True, file_name=str(test_log_file))
    handlers = logger.logger.handlers
    assert len(handlers) == 1
    assert isinstance(handlers[0], logging.FileHandler)
    assert handlers[0].baseFilename == str(test_log_file)

def test_both_handlers_added(tmp_path):
    """Tests adding both handlers"""
    test_log_file = tmp_path / "test.log"
    logger = Logger(name='test_logger', log_to_console=True, log_to_file=True, file_name=str(test_log_file))
    handlers = logger.logger.handlers
    assert len(handlers) == 2
    handler_types = [type(h) for h in handlers]
    assert logging.StreamHandler in handler_types
    assert logging.FileHandler in handler_types

def test_no_handlers_added():
    """Tests when no handlers are added"""
    logger = Logger(name='test_logger', log_to_console=False, log_to_file=False)
    handlers = logger.logger.handlers
    assert len(handlers) == 0

def test_propagate_false():
    """Tests that the propagate property is set to False"""
    logger = Logger(name='test_logger')
    assert logger.logger.propagate is False

def test_logging_methods(caplog):
    """Tests logging methods for correct behavior"""
    logger = Logger(name='test_logger', log_to_console=True, log_to_file=False)
    with caplog.at_level(logging.DEBUG, logger='test_logger'):
        logger.debug('Debug message')
        logger.info('Info message')
        logger.warning('Warning message')
        logger.error('Error message')
        logger.critical('Critical message')

    assert len(caplog.records) == 5
    expected_messages = [
        ('test_logger', logging.DEBUG, 'Debug message'),
        ('test_logger', logging.INFO, 'Info message'),
        ('test_logger', logging.WARNING, 'Warning message'),
        ('test_logger', logging.ERROR, 'Error message'),
        ('test_logger', logging.CRITICAL, 'Critical message'),
    ]

    for record, expected in zip(caplog.records, expected_messages):
        assert record.name == expected[0]
        assert record.levelno == expected[1]
        assert record.getMessage() == expected[2]

def test_color_formatting():
    """Tests color formatting in console output"""
    logger = Logger(name='test_logger', log_to_console=True, log_to_file=False)
    import io
    stream = io.StringIO()
    for handler in logger.logger.handlers:
        if isinstance(handler, logging.StreamHandler):
            handler.stream = stream

    logger.info('Test message')
    output = stream.getvalue()
    color_code = Logger.COLORS['INFO']
    reset_code = Logger.COLORS['RESET']
    assert color_code in output
    assert 'Test message' in output
    assert reset_code in output

def test_file_logging(tmp_path):
    """Tests logging to a file without color formatting"""
    test_log_file = tmp_path / "test.log"
    logger = Logger(name='test_logger', log_to_console=False, log_to_file=True, file_name=str(test_log_file))
    logger.info('File test message')

    with open(test_log_file, 'r', encoding='utf-8') as file:
        content = file.read()
        assert 'File test message' in content
        # Check that color codes are not present
        for code in Logger.COLORS.values():
            assert code not in content

def test_logger_level():
    """Tests the logger level"""
    logger = Logger(name='test_logger')
    assert logger.logger.level == logging.DEBUG

def test_handler_single_instance():
    """Tests that handlers are not added multiple times"""
    logger1 = Logger(name='test_logger', log_to_console=True, log_to_file=False)
    handlers_before = len(logger1.logger.handlers)
    logger2 = Logger(name='test_logger', log_to_console=True, log_to_file=False)
    handlers_after = len(logger2.logger.handlers)
    assert handlers_before == handlers_after

