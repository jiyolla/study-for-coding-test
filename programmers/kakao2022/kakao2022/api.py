import json

import requests
from ratelimit import limits, sleep_and_retry

from .config import BASE_URL, X_AUTH_TOKEN


auth_key = 'Call reset_sim() to make this value valid'


# Max 10 calls per second.
@sleep_and_retry
@limits(calls=10, period=1)
def check_limit():
    pass


def reset_sim(problem: int):
    check_limit()

    headers = {
        'X-Auth-Token': X_AUTH_TOKEN,
        'Content-Type': 'application/json'
    }
    body = {
        'problem': problem
    }

    global auth_key
    auth_key = requests.post(url=BASE_URL + '/start', data=json.dumps(body), headers=headers).json()['auth_key']


def get_waiting_line():
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    return requests.get(url=BASE_URL + '/waiting_line', headers=headers).json()


def get_game_result():
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    return requests.get(url=BASE_URL + '/game_result', headers=headers).json()


def get_user_info():
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    return requests.get(url=BASE_URL + '/user_info', headers=headers).json()


def put_match(pairs):
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    body = {
        'pairs': pairs
    }
    return requests.put(url=BASE_URL + '/match', data=json.dumps(body), headers=headers).json()


def put_change_grade(commands):
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    body = {
        'commands': commands
    }
    return requests.put(url=BASE_URL + '/change_grade', data=json.dumps(body), headers=headers).json()


def get_score():
    check_limit()

    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    return requests.get(url=BASE_URL + '/score', headers=headers).json()
