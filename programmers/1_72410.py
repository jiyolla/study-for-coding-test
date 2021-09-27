# https://programmers.co.kr/learn/courses/30/lessons/72410
# 신규 아이디 추천

import re


def solution(new_id: str):
    # Step 1
    new_id = new_id.lower()

    # Step 2
    new_id = re.sub('[^a-z0-9_.-]', '', new_id)
    
    # Step 3
    new_id = re.sub('\.\.+', '.', new_id)

    # Step 4
    new_id = new_id.strip('.')

    # Step 5
    new_id = 'a' if not new_id else new_id

    # Step 6
    new_id = new_id[:15].strip('.')
    
    # Step 7
    new_id = new_id + new_id[-1]*(3 - len(new_id))

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
