import random

value_dictionary = {}
def get_prob(my_score,opponent_score,turn_total):
    if my_score + turn_total >= 100:
        return 1.0
    if opponent_score >= 100:
        return 0.0
    return value_dictionary[(my_score,opponent_score,turn_total)]

def make_ai_decision(my_score, opponent_score, turn_total):
    #if I stop, what is my probability to win?
    chance_of_hold = 1 - get_prob(opponent_score, my_score + turn_total, 0)
    #if I roll, what is my chance to win and my chance to lose all points on this turn?
    roll_scenarios = []
    roll_scenarios.append(1 - get_prob(opponent_score, my_score, 0))
    for g in range(2, 7):
        roll_scenarios.append(get_prob(my_score, opponent_score, turn_total + g))
        chance_of_roll = roll_scenarios[0] + roll_scenarios[1] + roll_scenarios[2] + roll_scenarios[3] + roll_scenarios[4] + \
             roll_scenarios[5]
    chance_of_roll = chance_of_roll / 6
    #compares both probabilities
    if chance_of_hold > chance_of_roll:
        return "Hold"
    else:
        return "Roll"

#this adds all the possible combinations of my score, opponent score, and the amount on that turn. these are the keys for the dictionary, stored as a tuple
#the keys are the probability that you will win if you take this certain action
for my_score in range(100):
    for opponent_score in range(100):
        for turn_total in range(100):
            current_state = (my_score, opponent_score, turn_total)
            value_dictionary[current_state] = 0.5

while True:
    for i in range(99,-1,-1):
        for j in range(99,-1,-1):
            for k in range(99,-1,-1):
                my_score = i
                opponent_score = j
                turn_total = k
                my_score += turn_total
                p_hold = 1 - get_prob(opponent_score,my_score,0)
                value_dictionary[opponent_score,my_score,0] = p_hold

turn = 2
turn_total = 0
opponent_score = 0
my_score = 0
while True:
    if my_score >= 100:
        print(f"You win! \nIt took you {turn / 2 - 1} turns.\nThe AI was on {opponent_score} when you reached {my_score}.\nWell done.")
        break
    elif opponent_score >= 100:
        print(f"You lose! \nIt took the AI {turn / 2 - 1} turns.\nYou were on {my_score} when the AI reached {opponent_score}.\nBetter luck next time.")
        break
    if turn % 2 == 0:
        print("")
        choice = input(f"Your score is {my_score}, your opponent's score is {opponent_score}. \nYour turn total is {turn_total}\nWould you like to roll or hold?\n -roll\n -hold\n >").lower()
        if choice == "roll":
            dice_roll = random.randint(1,6)
            if dice_roll == 1:
                turn_total = 0
                turn += 1
                print(f"You decided to roll. Unfortunately, you got a 1. \nYour turn ends with {my_score} points banked.")
            else:
                print(f"You decided to roll. Thankfully, you got a {dice_roll}. \nYour turn keeps going.")
                turn_total += dice_roll
        elif choice == "hold":
            my_score += turn_total
            print(f"You decided to hold. You have banked {turn_total} points bringing your final score for this turn to {my_score}")
            turn_total = 0
            turn += 1
    else:
        print("")
        print("It is the AI's turn now.")
        if make_ai_decision(opponent_score,my_score,turn_total) == "Roll":
            dice_roll = random.randint(1,6)
            if dice_roll == 1:
                turn_total = 0
                turn += 1
                print(f"The AI decided to roll. They got a 1. \nTheir turn ends with {opponent_score} points banked.")
            else:
                turn_total += dice_roll
                print(f"The AI decided to roll. They got a {dice_roll}.\nTheir turn keeps going.")
                print(f"They have a turn total of {turn_total} and they have {opponent_score} points banked.")
        elif make_ai_decision(opponent_score, my_score, turn_total) == "Hold":
            opponent_score += turn_total
            print(f"The AI decided to hold. They banked {turn_total} points bringing their final score for this turn to {opponent_score}")
            turn_total = 0
            turn += 1







