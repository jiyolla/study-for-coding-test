# https://programmers.co.kr/learn/courses/30/lessons/81301
# 숫자 문자열과 영단어

def solution(s: str):
    replaces = [
        {
            'new': '0',
            'old': 'zero'
        },
        {
            'new': '1',
            'old': 'one'
        },
        {
            'new': '2',
            'old': 'two'
        },
        {
            'new': '3',
            'old': 'three'
        },
        {
            'new': '4',
            'old': 'four'
        },
        {
            'new': '5',
            'old': 'five'
        },
        {
            'new': '6',
            'old': 'six'
        },
        {
            'new': '7',
            'old': 'seven'
        },
        {
            'new': '8',
            'old': 'eight'
        },
        {
            'new': '9',
            'old': 'nine'
        },
    ]

    for replace in replaces:
        s = s.replace(replace['old'], replace['new'])

    return int(s)

print(solution("one4seveneight"))
