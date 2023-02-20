# --------------------------------------------------------
'''
function which calculates new state of the bet
depends on new data about events
'''
# --------------------------------------------------------


def check_state(score: str, state: str, market: str):
    score_list = score.split('-')
    if state == 'created':
        return 'None'
    elif state == 'active':
        if market == 'team_1':
            if score_list[0] > score_list[1]:
                return 'winning'
            else:
                return 'losing'
        if market == 'draw':
            if score_list[0] == score_list[1]:
                return 'winning'
            else:
                return 'losing'
        if market == 'team_2':
            if score_list[0] < score_list[1]:
                return 'winning'
            else:
                return 'losing'
    else:
        if market == 'team_1':
            if score_list[0] > score_list[1]:
                return 'win'
            else:
                return 'lose'
        if market == 'draw':
            if score_list[0] == score_list[1]:
                return 'win'
            else:
                return 'lose'
        if market == 'team_2':
            if score_list[0] < score_list[1]:
                return 'win'
            else:
                return 'lose'
