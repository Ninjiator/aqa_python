from requests.auth import HTTPBasicAuth

class CarsClient:
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session

    def login(self):
        auth_request = self.session.post(
            f"{self.base_url}/auth",
            auth=HTTPBasicAuth('test_user', 'test_pass'))

        auth_request.raise_for_status()

        token = auth_request.json()["access_token"]
        self.session.headers.update({
            "Authorization": f"Bearer {token}"})

    def get_cars(self, sort_by=None, limit=None):
        params = {}

        if sort_by is not None:
            params["sort_by"] = sort_by
        if limit is not None:
            params["limit"] = limit

        return self.session.get(
            f"{self.base_url}/cars",
            params=params
        )
