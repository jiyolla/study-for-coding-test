import json

import requests
from ratelimit import limits, sleep_and_retry

from .config import BASE_URL, X_AUTH_TOEKN


# Max 10 calls per second.
@sleep_and_retry
@limits(calls=10, period=1)
def check_limit():
    ...


def reset_sim(problem: int):
    check_limit()

    headers = {
        'X-Auth-Token': X_AUTH_TOKEN,
        'Content-Type': 'application/json'
    }
    body = {
        'problem': problem
    }

    return requests.post(url=BASE_URL + '/start', data=json.dumps(body), headers=headers).json()


def get_waiting_line(auth_key: str):
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    return requests.get(url=BASE_URL + '/waiting_line', headers=headers).json()


def get_game_result(auth_key: str):
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    return requests.get(url=BASE_URL + '/game_result', headers=headers).json()


def get_user_info(auth_key: str):
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    return requests.get(url=BASE_URL + '/user_info', headers=headers).json()


def put_match(auth_key: str, pairs):
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    body = {
        'pairs': pairs
    }
    return requests.put(url=BASE_URL + '/match', data=json.dumps(body), headers=headers).json()


def put_change_grade(auth_key: str, commands):
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    body = {
        'commands': commands
    }
    return requests.put(url=BASE_URL + '/change_grade', data=json.dumps(body), headers=headers).json()


def get_score(auth_key: str):
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    return requests.get(url=BASE_URL + '/score', headers=headers).json()
