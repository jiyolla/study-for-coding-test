import requests
import json
from typing import List

BASE_URL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
X_AUTH_TOKEN = '06365e288dc3539162e75243e51853c0'

def reset_sim(problem: int):
    headers = {
        'X-Auth-Token': X_AUTH_TOKEN,
        'Content-Type': 'application/json'
    }
    body = {
        'problem': problem
    }

    return requests.post(url=BASE_URL + '/start', data=json.dumps(body), headers=headers).json()


def get_location(auth_key: str):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    return requests.get(url=BASE_URL + '/locations', headers=headers).json()


def get_trucks(auth_key: str):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    return requests.get(url=BASE_URL + '/trucks', headers=headers).json()


def simulate(auth_key: str, commands: List):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    body = {
        'commands': commands
    }
    return requests.put(url=BASE_URL + '/simulate', data=json.dumps(body), headers=headers).json()


def get_score(auth_key: str):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    return requests.get(url=BASE_URL + '/score', headers=headers).json()


def sim_baseline(problem: int):
    auth_key = reset_sim(problem)['auth_key']
    locations = []
    trucks = get_trucks(auth_key)['trucks']
    commands = [{'truck_id': truck['id'], 'command': [1,3]*5} for truck in trucks]
    print(commands)
    
    for i in range(720):
        print(i)
        locations.append(get_location(auth_key))
        simulate(auth_key, commands)

    print(get_score(auth_key))
    return locations


def solve_0():
    problem = 1
    auth_key = reset_sim(problem)['auth_key']

    # Initialization
    commands = [
        {
            'truck_id': 0, 
            'command': [0]
        },
        {
            'truck_id': 1, 
            'command': [1]*4
        },
        {
            'truck_id': 2, 
            'command': [2]*4
        },
        {
            'truck_id': 3, 
            'command': [1,2]*4
        },
        {
            'truck_id': 4, 
            'command': [1,2]*2
        }
    ]
    simulate(auth_key, commands)

    for i in range(719):
        print(i)
        locations = get_location(auth_key)['locations']
        sum_bikes = sum([location['located_bikes_count'] for location in locations])
        avg = sum_bikes // 25

        below_avg = []
        above_avg = []
        for location in locations:
            if location['located_bikes_count'] < avg:
                below_avg.append(location)
            elif location['located_bikes_count'] > avg + 1:
                above_avg.append(location)
        below_avg.sort(key=lambda item: item['located_bikes_count'])
        for location in below_avg:
            
    
        


def main():
    # locations_1 = sim_baseline(1)
    # locations_2 = sim_baseline(1)
    # for old_location, location in zip(old_locations, locations):
    #     if old_location != location:
    #         print('Ouch!')
    solve_0()
        
if __name__ == '__main__':
    main()






# Simulate
# Score

res = requests.get(url='https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-1.json').json()

def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__, reverse=True)

src_count = [0] * 3600
dst_count = [0] * 3600

def reset():
    src_count = [0] * 3600
    dst_count = [0] * 3600

def count(data):
    for src, dst, _ in data:
        src_count[src] += 1
        dst_count[dst] += 1

i = 1
for time in res:
    count(res[time])
    if int(time) >= 240 * i - 1:
        i += 1
        print({i: src_count[i] for i in argsort(src_count)[:10]})
        print({i: dst_count[i] for i in argsort(dst_count)[:10]})
        reset()




 
