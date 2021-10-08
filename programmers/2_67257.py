# https://programmers.co.kr/learn/courses/30/lessons/67257
# [카카오 인턴] 수식 최대화

from itertools import permutations


def eval_with_precedence(tokens, precedence):
    for opr in precedence:
        new_tokens = []
        for i in range(len(tokens)):
            if tokens[i] == opr:
                tokens[i + 1] = eval(f'{new_tokens.pop(-1)}{opr}{tokens[i + 1]}')
            else:
                new_tokens.append(tokens[i])
        tokens = new_tokens
    return new_tokens[0]
            

def solution(expression):
    tokens = ['']
    for c in expression:
        if c in '+-*':
            tokens.append(c)
            tokens.append('')
        else:
            tokens[-1] += c
    
    return max(abs(eval_with_precedence(tokens[:], precedence)) for precedence in permutations('+-*'))

print(solution("100-200*300-500+20"))
