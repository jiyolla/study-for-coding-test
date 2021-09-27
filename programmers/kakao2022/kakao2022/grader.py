import random

from .api import put_change_grade


# grades[id] = grade for user #{id}.
# grades[0] is not used. Since user id starts from 1.


def change_grade_randomshuffle(auth_key, grades):
    changed_users_id = set(range(len(grades)))
    changed_users_id.remove(0)
    grades = list(range(len(grades)))
    random.shuffle(grades)

    commands = []
    for changed_user_id in changed_users_id:
        commands.append({'id': changed_user_id, 'grade': grades[changed_user_id]})
    put_change_grade(auth_key, commands)


def change_grade_simplelinear(auth_key, grades, game_results):
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
    put_change_grade(auth_key, commands)


def change_grade_discountedlinear(auth_key, grades, game_results):
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
    put_change_grade(auth_key, commands)


def change_grade_simplequadratic(auth_key, grades, game_results):
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
    put_change_grade(auth_key, commands)

def change_grade_preventabusediscountedlinear(auth_key, grades, game_results):
    # Max score is given at 11.
    # Games below 11 mins give base scores.
    BASE_SCORE = 1000
    MIN_TAKEN = 11
    MAX_TAKEN = 40
    changed_users_id = set()
    for game_result in game_results:
        changed_users_id.add(game_result['win'])
        changed_users_id.add(game_result['lose'])
        if game_result['taken'] < 11:
            grades[game_result['win']] += BASE_SCORE
            grades[game_result['lose']] -= BASE_SCORE
        else:
            grades[game_result['win']] += BASE_SCORE*(2 - 1.5*(game_result['taken'] - MIN_TAKEN)/(MAX_TAKEN - MIN_TAKEN))
            grades[game_result['lose']] -= BASE_SCORE*(2 - 1.5*(game_result['taken'] - MIN_TAKEN)/(MAX_TAKEN - MIN_TAKEN))
    
    commands = []
    for changed_user_id in changed_users_id:
        commands.append({'id': changed_user_id, 'grade': grades[changed_user_id]})
    put_change_grade(auth_key, commands)