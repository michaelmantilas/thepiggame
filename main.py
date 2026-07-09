
value_dictionary = {}
#this adds all the possible combinations of my score, opponent score, and the amount on that turn. these are the keys for the dictionary, sotred as a tuple
#the keys are the probability that you will win if you take this certain action
for my_score in range(100):
    for opponent_score in range(100):
        for turn_total in range(100):
            current_state = (my_score, opponent_score, turn_total)
            value_dictionary[current_state] = 0.5
def get_prob(my_score,opponent_score,turn_total):
    if my_score + turn_total >= 100:
        return 1.0
    if opponent_score >= 100:
        return 0.0
    return value_dictionary[(my_score,opponent_score,turn_total)]





for i in range(100):
    for j in range(100):
        for k in range(100):
            my_score = i
            opponent_score = j
            turn_total = k
            my_score += turn_total
            p_hold = 1 - get_prob(opponent_score,my_score,0)
            my_score = i
            roll_scenarios = []
            roll_scenarios.append(1 - get_prob(opponent_score,my_score,0))
            for g in range(2,7):
                 roll_scenarios.append(get_prob(my_score, opponent_score, turn_total + g))
            p_roll = roll_scenarios[0] + roll_scenarios[1] + roll_scenarios[2] + roll_scenarios[3] + roll_scenarios[4] + roll_scenarios[5]
            p_roll = p_roll / 6
            if p_roll > p_hold:
                value_dictionary[(i,j,k)] = p_roll
            else:
                value_dictionary[(i,j,k)] = p_hold
#testing dictionary
print(value_dictionary)
