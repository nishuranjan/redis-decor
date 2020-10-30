import cache_decorator
import json
import requests


# To Do :: cached static data
# https://admin.dev.placeexchange.com/api/v3/orgs/880940e1-5c71-4f1f-82eb-eab9ec8bb23a/deals/Ar_testDeal
# https://admin.dev.placeexchange.com/api/v3/deals/7f4c8e61-2a9b-4dd5-9ec7-ef82c1ad24e9

org_url = "https://admin.dev.placeexchange.com/api/v3/"
request = org_url+"deals/7f4c8e61-2a9b-4dd5-9ec7-ef82c1ad24e9"
jsonData = """
{
    "allowed_pct": "null",
    "at": 3,
    "bidfloor": "0.25",
    "bidfloorcur": "USD",
    "created_by": "null",
    "ext": "null",
    "guaranteed": False,
    "id": "7f4c8e61-2a9b-4dd5-9ec7-ef82c1ad24e9",
    "name": "Ar_testDeal",
    "notes": "",
    "owned_by": "880940e1-5c71-4f1f-82eb-eab9ec8bb23a",
    "status": "paid",
    "token": "",
    "ts": 1571489598,
    "wadomain": [],
    "wbuyer": [],
    "wseat": []
}
"""
# https://jsonplaceholder.typicode.com/todos/2
# https://jsonplaceholder.typicode.com/todos?userId=10&completed=true
# https://jsonplaceholder.typicode.com/users

req_url = "https://jsonplaceholder.typicode.com/todos?userId=10&completed=true"
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""


@cache_decorator.cached
def get_deals(req_url: str):
    response = requests.get(req_url)
    todos = json.loads(response.text)
    print(f"View values from api {todos}")
    return todos


get_deals(req_url)
