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


@pytest.fixture(scope="session")
def test_logger():
    logger = logging.getLogger("tests")
    logger.setLevel(logging.ERROR)
    logger.propagate = False

    # щоб не додавати хендлери повторно (дублікати)
    if logger.handlers:
        return logger

    fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # file
    fh = logging.FileHandler("test_search.log", encoding="utf-8", mode="a")
    fh.setLevel(logging.ERROR)
    fh.setFormatter(fmt)

    # console
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger