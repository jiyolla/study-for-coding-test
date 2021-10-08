def is_valid_point(place, r, c):
    max_r, max_c = len(place) - 1, len(place[0]) - 1
    
    if r > 0 and place[r - 1][c] == 'P':
        return False
    if c > 0 and place[r][c - 1] == 'P':
        return False
    
    if r > 0 and c > 0 and place[r - 1][c - 1] == 'P':
        return place[r - 1][c] == 'X' and place[r][c - 1] == 'X'
    if r > 0 and c < max_c and place[r - 1][c + 1] == 'P':
        return place[r - 1][c] == 'X' and place[r][c + 1] == 'X'
    
    if r > 1 and place[r - 2][c] == 'P':
        return place[r - 1][c] == 'X'
    if c > 1 and place[r][c - 2] == 'P':
        return place[r][c - 1] == 'X'
    
    return True
    

def is_valid_place(place):
    for r in range(len(place)):
        for c in range(len(place[0])):
            if place[r][c] == 'P':
                if not is_valid_point(place, r, c):
                    return 0
    return 1

def solution(places):
    ret = []
    for place in places:
        ret.append(is_valid_place(place))
                        
    return ret