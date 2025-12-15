import pytest
import requests
import logging

from API.CarsClient import CarsClient


@pytest.fixture(scope="class")
def base_url():
    return "http://127.0.0.1:8080"

@pytest.fixture(scope="class")
def session():
    s = requests.Session()
    yield s
    s.close()

@pytest.fixture(scope="class")
def cars_client(base_url, session):
    return CarsClient(base_url, session)

@pytest.fixture(scope="class")
def auth_client(cars_client):
    cars_client.login()
    return cars_client



@pytest.fixture(scope="session", autouse=True)
def file_logger():
    #file logger
    file_error_logger = logging.Logger('file_error_logger')
    file_error_logger.setLevel(logging.ERROR)

    file_error_handler = logging.FileHandler("test_search.log", encoding="utf-8")
    file_error_handler.setLevel(logging.ERROR)
    
    formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
    file_error_handler.setFormatter(formater)
    file_error_logger.addHandler(file_error_handler)

    return file_error_logger


@pytest.fixture(scope="session", autouse=True)
def console_logger():
    console_error_logger = logging.getLogger('console_error_logger')
    console_error_logger.setLevel(logging.ERROR)

    console_error_handler = logging.StreamHandler()
    console_error_handler.setLevel(logging.ERROR)

    formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    console_error_handler.setFormatter(formater)
    console_error_logger.addHandler(console_error_handler)

    return console_error_logger


@pytest.fixture()
def logg_all(info_to_log : str, console_logger, file_logger):
    console_logger.error(info_to_log)
    file_logger.error(info_to_log)