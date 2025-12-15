import pytest


class TestCars:


    @pytest.mark.parametrize('limit_value', [5, 25, 1, 0, 12])
    def test_limits(self, auth_client, limit_value):
        cars_response = auth_client.get_cars(limit=limit_value)

        assert cars_response.status_code == 200
        cars = cars_response.json()
        assert len(cars) == limit_value


    @pytest.mark.parametrize('sort_param', ['price', 'brand', 'year', "engine_volume"])
    def test_sorting(self, auth_client, sort_param):
        cars_response = auth_client.get_cars(sort_by = sort_param)

        assert cars_response.status_code == 200

        cars = cars_response.json()

        cars_sorted_by_param = [c[sort_param] for c in cars]

        assert cars_sorted_by_param == sorted(cars_sorted_by_param)

    @pytest.mark.parametrize('limit_value, sort_param', [
        (5, 'brand'),
        (25, 'price'),
        (7, 'year'),
        (0, "engine_volume")
    ])
    def test_sorting_with_limits(self, auth_client, sort_param, limit_value):
        cars_response = auth_client.get_cars(sort_by = sort_param, limit= limit_value)
        assert cars_response.status_code == 200

        cars = cars_response.json()

        assert len(cars) == limit_value

        cars_sorted_by_param = [c[sort_param] for c in cars]

        assert cars_sorted_by_param == sorted(cars_sorted_by_param)

