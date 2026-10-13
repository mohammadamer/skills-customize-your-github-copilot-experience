import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_BASE_URL = "http://127.0.0.1:8000"


def request_api(method, path, payload=None):
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    request = Request(
        f"{API_BASE_URL}{path}",
        data=data,
        headers=headers,
        method=method,
    )

    try:
        with urlopen(request) as response:
            if response.status == 204:
                return None
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        print(f"API returned HTTP {error.code}: {error.reason}")
        return None
    except URLError as error:
        print(f"Could not connect to the API: {error.reason}")
        return None


def list_items():
    # Send GET /items and return the list of items.
    pass


def get_item(item_id):
    # Send GET /items/{item_id} and return the matching item.
    pass


def create_item(name, description):
    # Send POST /items with name and description as a JSON payload.
    pass


def update_item(item_id, name, description):
    # Send PUT /items/{item_id} with the updated name and description.
    pass


def delete_item(item_id):
    # Send DELETE /items/{item_id} and report whether it succeeded.
    pass


def main():
    # Add calls here to test each client function against the running API.
    print("Items:", list_items())


if __name__ == "__main__":
    main()