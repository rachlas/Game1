import random
# This is a game. The goal is getting a combined score of 50(or above)
# you roll a dice, you can end your own turn te keep the points
# when you roll a 1 your turn ends, and 0 points will be given


#this makes a dice with 6 faces, uses the random function to give a random number
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

#a while loop to ask for number of players, needs to be a digit, then makes a Intiger of the string given by the user
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

#sets the score needed to win the game
#makes a list-item for every player 
max_score = 50
player_scores = [0 for _ in range(players)]

#sets the game to stop when a score equal to or higher then 50 is achieved
while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started!\n")
        current_score = 0
    
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break 

            value = roll()
            if value== 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])
