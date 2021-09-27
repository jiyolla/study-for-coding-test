# https://programmers.co.kr/learn/courses/30/lessons/64061
# 크레인 인형뽑기 게임

def solution(board, moves):
    board = list(map(list, zip(*board[::-1])))
    for b in board:
        while b[-1] == 0:
            b.pop()

    stack = []
    ret = 0
    for move in moves:
        try:
            stack.append(board[move - 1].pop())
            if stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()
                ret += 2
        except IndexError:
            pass

    return ret

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
