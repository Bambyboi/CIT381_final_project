import random
#indicate the points for each player
count_user_winner = 0
count_computer_winner = 0

while True:
    #user player
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    #computer player
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    #determine either player one or two wins
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        #---------------------------------------
        count_user_winner += 0
        count_computer_winner += 0
        #---------------------------------------
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            #-------------------------------------------
            count_user_winner += 1
            count_computer_winner += 0
            #-------------------------------------------
        else:
            print("Paper covers rock! You lose.")
            #-------------------------------------------
            count_computer_winner += 1
            count_user_winner += 0
            #-------------------------------------------
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            #-----------------------------------(--------
            count_user_winner += 1
            count_computer_winner += 0
            #-------------------------------------------
        else:
            print("Scissors cuts paper! You lose.")
            #-------------------------------------------
            count_computer_winner += 1
            count_user_winner += 0
            #-------------------------------------------
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            #-------------------------------------------
            count_user_winner += 1
            count_computer_winner += 0
            #-------------------------------------------
        else:
            print("Rock smashes scissors! You lose.")
            #-------------------------------------------
            count_computer_winner += 1
            count_user_winner += 0
            #-------------------------------------------
    #--------------------------------------------------------------------------------------------------
    print(f'count_user_winner: {count_user_winner}\ncount_computer_winner: {count_computer_winner}')
    #--------------------------------------------------------------------------------------------------