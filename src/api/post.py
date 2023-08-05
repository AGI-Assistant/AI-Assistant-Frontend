import requests as rq


def user_message(contents: str, session_key: str, api_key: str = None) -> rq.models.Response:
    return rq.post(
        url="Link to API".format(),
        json={"message": contents},
        headers={"Content-Type": "application/json", 'Session': session_key, 'API-Key': api_key})
