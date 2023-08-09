"""
This package holds all APIs needed to run the frontend chat interface.
"""
import requests as rq


def send_message(contents: str, conversation_id: str, api_key: str = None) -> rq.models.Response:
    return rq.post(
        url="Link to API".format(),
        json={'conversationID': conversation_id,
              'message': contents},
        headers={"Content-Type": "application/json", 'API-Key': api_key})
