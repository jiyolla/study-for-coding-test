import random

from .api import put_change_grade


# grades[id] = grade for user #{id}.
# grades[0] is not used. Since user id starts from 1.


def change_grade_randomshuffle(grades):
    changed_users_id = set(range(len(grades)))
    changed_users_id.remove(0)
    grades = list(range(len(grades)))
    random.shuffle(grades)

    commands = []
    for changed_user_id in changed_users_id:
        commands.append({'id': changed_user_id, 'grade': grades[changed_user_id]})
    put_change_grade(commands)


def change_grade_simplelinear(grades, game_results):
    MAX_TAKEN = 40
    changed_users_id = set()
    for game_result in game_results:
        changed_users_id.add(game_result['win'])
        changed_users_id.add(game_result['lose'])
        grades[game_result['win']] += MAX_TAKEN - game_result['taken']
        grades[game_result['lose']] -= MAX_TAKEN - game_result['taken']
    
    commands = []
    for changed_user_id in changed_users_id:
        commands.append({'id': changed_user_id, 'grade': grades[changed_user_id]})
    put_change_grade(commands)


def change_grade_discountedlinear(grades, game_results):
    BASE_SCORE = 100
    MIN_TAKEN = 3
    MAX_TAKEN = 40
    changed_users_id = set()
    for game_result in game_results:
        changed_users_id.add(game_result['win'])
        changed_users_id.add(game_result['lose'])
        grades[game_result['win']] += BASE_SCORE * (2 - 1.6*(game_result['taken'] - MIN_TAKEN)/(MAX_TAKEN - MIN_TAKEN))
        grades[game_result['lose']] -= BASE_SCORE * (2 - 1.6*(game_result['taken'] - MIN_TAKEN)/(MAX_TAKEN - MIN_TAKEN))
    
    commands = []
    for changed_user_id in changed_users_id:
        commands.append({'id': changed_user_id, 'grade': grades[changed_user_id]})
    put_change_grade(commands)


def change_grade_simplequadratic(grades, game_results):
    MAX_TAKEN = 40
    changed_users_id = set()
    for game_result in game_results:
        changed_users_id.add(game_result['win'])
        changed_users_id.add(game_result['lose'])
        grades[game_result['win']] += (MAX_TAKEN - game_result['taken'])**2
        grades[game_result['lose']] -= (MAX_TAKEN - game_result['taken'])**2
    
    commands = []
    for changed_user_id in changed_users_id:
        commands.append({'id': changed_user_id, 'grade': grades[changed_user_id]})
    put_change_grade(commands)


def change_grade_preventabusediscountedlinear(grades, game_results, suspicion_marks):
    BASE_SCORE = 4000
    MIN_TAKEN = 3
    MAX_TAKEN = 40
    changed_users_id = set()
    for game_result in game_results:
        winner = game_result['win']
        loser = game_result['lose']
        game_time = game_result['taken']

        changed_users_id.add(winner)
        changed_users_id.add(loser)

        if game_time < 11:
            expected_game_time = 40 - abs(grades[winner] - grades[loser])/99000*35
            tolerance = 5 + 5
            if game_time < expected_game_time - tolerance:
                suspicion_marks[loser] += 1

            if suspicion_marks[loser] > 2:
                continue
        expected_win_rate = grades[winner]/(grades[winner] + grades[loser])
        win_rate_modifier = expected_win_rate # (expected_win_rate - 0.3)*2 + 0.2
        grades[winner] += win_rate_modifier*BASE_SCORE*(3 - 2.5*(game_time - MIN_TAKEN)/(MAX_TAKEN - MIN_TAKEN))
        grades[loser] -= win_rate_modifier*BASE_SCORE*(3 - 2.5*(game_time - MIN_TAKEN)/(MAX_TAKEN - MIN_TAKEN))
    
    commands = []
    for changed_user_id in changed_users_id:
        commands.append({'id': changed_user_id, 'grade': grades[changed_user_id]})
    put_change_grade(commands)
