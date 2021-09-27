# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축

def solution(s):
    ret = len(s)
    for stride_len in range(1, len(s)//2 + 1):
        current_combo = 1
        count = 0
        for i in range(stride_len, len(s), stride_len):
            if s[i:i + stride_len] == s[i - stride_len:i]:
                current_combo += 1
            else:
                count += stride_len + (0 if current_combo == 1 else len(str(current_combo)))
                current_combo = 1
        
        count += len(s[i:i + stride_len]) + (0 if current_combo == 1 else len(str(current_combo)))
        if count < ret:
            ret = count
                
    return ret

print(solution("abcabcdede"))
