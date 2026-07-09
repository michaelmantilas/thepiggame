value_dictionary = {}
#this adds all the possible combinations of my score, opponent score, and the amount on that turn. these are the keys for the dictionary, sotred as a tuple
#the keys are the probability that you will win if you take this certain action
#another comment to test the commit process
for my_score in range(100):
    for opponent_score in range(100):
        for turn_total in range(100):
            current_state = (my_score, opponent_score, turn_total)
            value_dictionary[current_state] = 0.5