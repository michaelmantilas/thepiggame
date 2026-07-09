
def make_ai_decision(my_score, opponent_score, turn_total):
    #if I stop, what is my probability to win?
    chance_if_hold = get_win_probability(my_score + turn_total, opponent_score, 0)
    #if I roll, what is my chance to win and my chance to lose all points on this turn?
    chance_if_roll = calculate_roll_chance(my_score, opponent_score, turn_total)
    #compares both probabilities, bigger is better
    if chance_if_hold > chance_if_roll:
        return "HOLD"
    else:
        return "ROLL"