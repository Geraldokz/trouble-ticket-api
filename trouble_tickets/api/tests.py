from django.test import TestCase
import json
import requests


def create_event():
    data = {
        "impact": {
            "priority": 1,
            "affected_services_count": 2
        },
        "start_date": "2021-05-24T11:25:00+07:00",
        "finish_date": "2021-05-24T12:30:00+07:00",
        "description": "Описание 6-го события"
    }

    url = 'http://0.0.0.0:8000/api/v1/events/create-event'
    response = requests.post(url, json=data).text
    response_parsed = json.loads(response)
    return json.dumps(response_parsed, indent=4)


def update_event(event_id):
    data = {
        "id": event_id,
        "impact": {
            "priority": "2",
            "affected_services_count": 1
        },
        "start_date": "2021-05-22T01:00:00+07:00",
        "finish_date": None,
        "description": "Описание 4-го события обновленное"
    }
    url = f'http://0.0.0.0:8000/api/v1/events/{event_id}'
    response = requests.patch(url, json=data).text
    response_parsed = json.loads(response)
    return json.dumps(response_parsed, indent=4)


def delete_event(event_id):
    url = f'http://0.0.0.0:8000/api/v1/events/{event_id}'
    response = requests.delete(url).text
    response_parsed = json.loads(response)
    return json.dumps(response_parsed, indent=4)


def get_event_data(event_id):
    url = f'http://0.0.0.0:8000/api/v1/events/{event_id}'
    response = requests.get(url).text
    response_parsed = json.loads(response)
    return json.dumps(response_parsed, indent=4)


def get_all_events_data():
    url = f'http://0.0.0.0:8000/api/v1/events/'
    response = requests.get(url).text
    response_parsed = json.loads(response)
    return json.dumps(response_parsed, indent=4)


if __name__ == '__main__':
    print(create_event())

