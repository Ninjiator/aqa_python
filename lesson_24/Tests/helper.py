import logging

def assert_with_log(condition: bool, msg: str, logger: logging.Logger):
    if not condition:
        logger.error(msg)
    assert condition, msg