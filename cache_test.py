import cache_decorator
import json
import requests


# https://jsonplaceholder.typicode.com/todos/2
# https://jsonplaceholder.typicode.com/todos?userId=10&completed=true
# https://jsonplaceholder.typicode.com/users

req_url = "https://jsonplaceholder.typicode.com/todos?userId=10&completed=true"


@cache_decorator.cached
@cache_decorator.invalidate_cached
def get_deals(req_url: str):
    response = requests.get(req_url)
    todos = json.loads(response.text)
    print(f"View values from api {todos}")
    return todos


get_deals(req_url)
