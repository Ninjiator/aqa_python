import pytest

from Tests.helper import assert_with_log


class TestCars:
    @pytest.mark.parametrize('limit_value', [5, 25, 1, 0, 12])
    def test_limits(self, auth_client, limit_value, test_logger):
        cars_response = auth_client.get_cars(limit=limit_value)

        status_code_msg = f"Expected status code is 200 but actual is {cars_response.status_code}"
        assert_with_log(cars_response.status_code == 200, status_code_msg, test_logger)

        cars = cars_response.json()

        len_of_cars_msg = f"Expected len with {limit_value} is {limit_value}, but actual is {len(cars)}"
        assert_with_log(len(cars) == limit_value, len_of_cars_msg, test_logger)


    @pytest.mark.parametrize('sort_param', ['price', 'brand', 'year', "engine_volume"])
    def test_sorting(self, auth_client, sort_param, test_logger):
        cars_response = auth_client.get_cars(sort_by = sort_param)

        status_code_msg = f"Expected status code is 200 but actual is {cars_response.status_code}"
        assert_with_log(cars_response.status_code == 200, status_code_msg, test_logger)

        cars = cars_response.json()

        cars_sorted_by_param = [c[sort_param] for c in cars]
        cars_sorted_msg = f"Sorting result is not equal to expected"
        assert_with_log(cars_sorted_by_param == sorted(cars_sorted_by_param), cars_sorted_msg, test_logger)

    @pytest.mark.parametrize('limit_value, sort_param', [
        (5, 'brand'),
        (25, 'price'),
        (7, 'year'),
        (0, "engine_volume")
    ])
    def test_sorting_with_limits(self, auth_client, sort_param, limit_value, test_logger):
        cars_response = auth_client.get_cars(sort_by = sort_param, limit= limit_value)

        status_code_msg = f"Expected status code is 200 but actual is {cars_response.status_code}"
        assert_with_log(cars_response.status_code == 200, status_code_msg, test_logger)

        cars = cars_response.json()

        len_of_cars_msg = f"Expected len with {limit_value} is {limit_value}, but actual is {len(cars)}"
        assert_with_log(len(cars) == limit_value, len_of_cars_msg, test_logger)

        cars_sorted_by_param = [c[sort_param] for c in cars]

        cars_sorted_msg = f"Sorting result is not equal to expected"
        assert_with_log(cars_sorted_by_param == sorted(cars_sorted_by_param), cars_sorted_msg, test_logger)

