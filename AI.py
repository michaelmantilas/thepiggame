def make_ai_decision(my_score, opponent_score, turn_total):
    #if I stop, what is my probability to win?
    chance_if_hold = get_prob(my_score + turn_total, opponent_score, 0)
    #if I roll, what is my chance to win and my chance to lose all points on this turn?
    chance_if_roll = get_prob(my_score, opponent_score, turn_total)
    #compares both probabilities, bigger is better
    if chance_if_hold > chance_if_roll:
        return "Hold"
    else:
        return "Roll"
#a test

value_dictionary = {}


def get_prob(my_score, opponent_score, turn_total):
    if my_score + turn_total >= 100:
        return 1.0
    if opponent_score >= 100:
        return 0.0
    return value_dictionary[(my_score, opponent_score, turn_total)]


# this adds all the possible combinations of my score, opponent score, and the amount on that turn. these are the keys for the dictionary, stored as a tuple
# the keys are the probability that you will win if you take this certain action
for my_score in range(100):
    for opponent_score in range(1
    print(make_ai_decision(67,89,22))