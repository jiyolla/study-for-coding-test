from tqdm import trange

from .api import reset_sim, get_waiting_line, get_game_result, get_user_info, put_match, put_change_grade, get_score
from .grader import change_grade_preventabusediscountedlinear, change_grade_randomshuffle, change_grade_simplelinear, change_grade_discountedlinear, change_grade_simplequadratic


# ========== Type #1 Solver ==================================================
# Matching is indenpendant of grading, and more specifically only in FCFS way.
# Batch grading on the last turn

def alpha_solve(problem, matching_policy, grading_policy):
    auth_key = reset_sim(problem)['auth_key']
    
    users = get_user_info(auth_key)['user_info']
    grades = [0] * (len(users) + 1)
    game_results = []

    # Matching
    # Hardcoded to First Come Firt Served
    assert matching_policy == 'fcfs'
    for _ in trange(595):
        waiting_line = get_waiting_line(auth_key)['waiting_line']
        waiting_line.sort(key=lambda item: item['from'])
        game_results.extend(get_game_result(auth_key)['game_result'])
        pairs = []
        for i in range(len(waiting_line)//2):
            pairs.append([waiting_line[i]['id'], waiting_line[i + 1]['id']])
        put_match(auth_key, pairs)
    
    # Batch Grading
    if grading_policy == 'randomshuffle':
        change_grade_randomshuffle(auth_key, grades)
    elif grading_policy == 'simplelinear':
        change_grade_simplelinear(auth_key, grades, game_results)
    elif grading_policy == 'simplequadratic':
        change_grade_simplequadratic(auth_key, grades, game_results)
    elif grading_policy == 'discountedlinear':
        change_grade_discountedlinear(auth_key, grades, game_results)

    # End simulation and return score
    print(put_match(auth_key, []))
    return get_score(auth_key)


# ========== Type #2 Solver ==================================================
# Matching is dependant on grading, and thus grading happens on the fly

def beta_solve(problem, matching_policy, grading_policy):
    auth_key = reset_sim(problem)['auth_key']
    
    MAX_GRADE_DIFF = 100
    users = get_user_info(auth_key)['user_info']
    grades = [0] * (len(users) + 1)

    for _ in trange(595):
        waiting_line = get_waiting_line(auth_key)['waiting_line']
        waiting_line.sort(key=lambda item: item['from'])
        
        change_grade_simplelinear(auth_key, grades, get_game_result(auth_key)['game_result'])

        pairs = []
        for i in range(len(waiting_line)):
            for j in range(i + 1, len(waiting_line)):
                if abs(grades[waiting_line[i]['id']] - grades[waiting_line[j]['id']]) < MAX_GRADE_DIFF:
                    pairs.append([waiting_line[i]['id'], waiting_line[j]['id']])
                    waiting_line.pop(j)
                    break
        print(put_match(auth_key, pairs))

    # End simulation and return score
    print(put_match(auth_key, []))
    return get_score(auth_key)


# problem #1:
# {'status': 'finished', 'efficiency_score': '55.2227', 'accuracy_score1': '64.4444', 'accuracy_score2': '59.3047', 'score': '192.6771'}
# problem #2:
# 
def solve_limitmaxdiff_simplelinear(problem: int):
    auth_key = reset_sim(problem)['auth_key']
    
    MAX_GRADE_DIFF = 100
    users = get_user_info(auth_key)['user_info']
    grades = [0] * (len(users) + 1)
    for _ in trange(595):
        waiting_line = get_waiting_line(auth_key)['waiting_line']
        waiting_line.sort(key=lambda item: item['from'])
        
        change_grade_simplelinear(auth_key, grades, get_game_result(auth_key)['game_result'])

        pairs = []
        for i in range(len(waiting_line)):
            for j in range(i + 1, len(waiting_line)):
                if abs(grades[waiting_line[i]['id']] - grades[waiting_line[j]['id']]) < MAX_GRADE_DIFF:
                    pairs.append([waiting_line[i]['id'], waiting_line[j]['id']])
                    waiting_line.pop(j)
                    break
        put_match(auth_key, pairs)

    # End simulation and return score
    print(put_match(auth_key, []))
    return get_score(auth_key)


# problem #1:
# {'status': 'finished', 'efficiency_score': '98.084', 'accuracy_score1': '56.6667', 'accuracy_score2': '57.8218', 'score': '215.8534'}
# problem #2:
# 
def solve_limitmaxdiff_discountedlinear(problem: int):
    auth_key = reset_sim(problem)['auth_key']
    
    MAX_GRADE_DIFF = 600
    users = get_user_info(auth_key)['user_info']
    grades = [0] * (len(users) + 1)
    for _ in trange(595):
        waiting_line = get_waiting_line(auth_key)['waiting_line']
        waiting_line.sort(key=lambda item: item['from'])
        
        change_grade_discountedlinear(auth_key, grades, get_game_result(auth_key)['game_result'])

        pairs = []
        for i in range(len(waiting_line)):
            for j in range(i + 1, len(waiting_line)):
                if abs(grades[waiting_line[i]['id']] - grades[waiting_line[j]['id']]) < MAX_GRADE_DIFF:
                    pairs.append([waiting_line[i]['id'], waiting_line[j]['id']])
                    waiting_line.pop(j)
                    break
        put_match(auth_key, pairs)

    # End simulation and return score
    print(put_match(auth_key, []))
    return get_score(auth_key)


# problem #1:
# 
# problem #2:
# 
def solve_limitmaxdiff_preventabusediscountedlinear(problem: int):
    auth_key = reset_sim(problem)['auth_key']
    
    users = get_user_info(auth_key)['user_info']
    grades = [40000] * (len(users) + 1)
    game_records = [[] for _ in range(len(users) + 1)]
    for _ in trange(595):
        waiting_line = get_waiting_line(auth_key)['waiting_line']
        waiting_line.sort(key=lambda item: item['from'])
        
        game_results = get_game_result(auth_key)['game_result']
        for game_result in game_results:
            game_records[game_result['win']].append(1)
            game_records[game_result['lose']].append(0)
        change_grade_preventabusediscountedlinear(auth_key, grades, game_results)

        pairs = []
        is_waiting = [True] * len(waiting_line)
        for i in range(len(waiting_line)):
            for j in range(i + 1, len(waiting_line)):
                # Lock max biased win rate by estimation at 60%
                if (
                    max(grades[waiting_line[i]['id']], grades[waiting_line[j]['id']])
                    / (grades[waiting_line[i]['id']] + grades[waiting_line[j]['id']])
                    < 0.6
                    and is_waiting[i]
                    and is_waiting[j]
                ):
                    pairs.append([waiting_line[i]['id'], waiting_line[j]['id']])
                    is_waiting[i] = False
                    is_waiting[j] = False
                    break

        put_match(auth_key, pairs)

    # End simulation and return score
    print(put_match(auth_key, []))
    print(get_score(auth_key))
    breakpoint()
    return get_score(auth_key)