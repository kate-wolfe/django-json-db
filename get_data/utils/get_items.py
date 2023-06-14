from get_data.utils.authorization import authenticate_session
import requests

import environ

env = environ.Env()
environ.Env.read_env()


def get_items():
    session = authenticate_session(requests.Session())
    get_items_url = env("ITEMS_URL")
    get_items_params = {
        "limit": 2000,
        "fields": "id",
        "updatedDate": "2023-06-14",
        "deleted": "false",
        "suppressed": "false",
    }

    result = session.get(get_items_url, params=get_items_params)

    resultJSON = result.json()

    entryList = []

    for i in range(2000):
        entry = resultJSON["entries"][i]["id"]
        entryList.append(entry)

    return entryList
