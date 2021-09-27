# https://programmers.co.kr/learn/courses/30/lessons/42888
# 오픈채팅방

def solution(record):
    uid_name_dict = {}
    for cmd, uid, *name in map(str.split, reversed(record)):
        if cmd in {'Enter', 'Change'} and uid not in uid_name_dict:
            uid_name_dict[uid] = name[0]

    ret = []
    for cmd, uid, *name in map(str.split, record):
        if cmd == 'Enter':
            ret.append(f'{uid_name_dict[uid]}님이 들어왔습니다.')
        elif cmd == 'Leave':
            ret.append(f'{uid_name_dict[uid]}님이 나갔습니다.')
    
    return ret

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
