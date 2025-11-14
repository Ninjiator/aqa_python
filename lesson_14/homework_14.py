"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import pytest


LOG_FILE = 'login_system.log'

logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format = '%(asctime)s - %(levelname)s - %(message)s',
        force=True
    )

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера

    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


@pytest.mark.parametrize("username, status, expected_level", [

    ("admin", "expired", "WARNING"),
    ("president", "success", "INFO"),
    ("Mario", "failed", "ERROR")
])

def test_log_event(username: str, status: str, expected_level: str):
    log_event(username, status)
    with open("login_system.log", "r") as log_file:
        log = log_file.readlines()
        assert expected_level in log[-1]
