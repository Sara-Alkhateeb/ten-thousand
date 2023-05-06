from ten_thousand.game_logic import GameLogic

dice_roller = GameLogic.roll_dice

def play(roller=GameLogic.roll_dice,num_rounds=10):
    """
    A function to start the Ten Thousand game. Prompts the user whether to play the game or not.
    If the user chooses to play, it starts the game by calling the start_game function.

    Parameters:
    roller (function): The function that is used to roll the dice in the game. Default is GameLogic.roll_dice.

    Returns:
    None
    """
    global dice_roller
    dice_roller = roller

    choice = invite_to_play()

    if choice == "y":
        score = start_game(num_rounds)
        print(f"Thanks for playing. You earned {score} points")
    else:
        decline_game()

def invite_to_play():
    """
    A function to invite the user to play the Ten Thousand game.

    Parameters:
    None

    Returns:
    choice (str): The user's choice, 'y' or 'n'.
    """
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")
    return choice

def start_game(max_round):
    """
    A function to start the Ten Thousand game.

    Parameters:
    max_round (int): The maximum number of rounds to play. Default is 40.

    Returns:
    total_score (int): The total score earned by the player in the game.
    """
    round_num = 0
    total_score = 0
    choice=""

    while round_num < max_round:
        if choice=="q":
            break
        round_num += 1
        print(f"Starting round {round_num}")
        num_of_dice = 6
        print(f"Rolling {num_of_dice} dice...")
        dice_roll = dice_roller(num_of_dice)
        unpacked_tuple = ' '.join([str(x) for x in dice_roll])
        print("*** " + unpacked_tuple + " ***")

        round_score = 0
        unbanked_score = 0
        dice_kept = []
        while True:
            choice=ask_for_input()
            if choice == "q":
                break

            dice_kept = [int(x) for x in choice]
            
            cheater=cheater_function(dice_roll,dice_kept,unpacked_tuple)
            hot_check = GameLogic.get_scorers(dice_kept)

            if len(hot_check) == 6 and not cheater:

                choice = hot_dice_fun(dice_kept, unbanked_score)

            while cheater:
                choice=ask_for_input()
                if choice == "q":
                    break
                elif choice!="q":
                    dice_kept = [int(x) for x in choice]
                    cheater= cheater_function(dice_roll,dice_kept,unpacked_tuple)
                
                
            if choice=="q":
                break
            round_score = GameLogic.calculate_score(dice_kept)
            unbanked_score += round_score
            if len(dice_kept)!=6:
                num_of_dice-=len(dice_kept)
                print(f"You have {unbanked_score} unbanked points and {num_of_dice} dice remaining")

                print("(r)oll again, (b)ank your points or (q)uit:")
                choice = input("> ")
            if choice == "b":
                total_score += unbanked_score
                print(f"You banked {unbanked_score} points in round {round_num}")
                print(f"Total score is {total_score} points")
                unbanked_score = 0
                break
            elif choice == "q":
                break
            elif choice == "r":
                # num_of_dice -= len(dice_kept)
                if num_of_dice == 0:
                    break
                dice_roll = dice_roller(num_of_dice)
                unpacked_tuple = ' '.join([str(x) for x in dice_roll])
                print(f"Rolling {num_of_dice} dice...")
                print("*** " + unpacked_tuple + " ***")
                remaning_dices_score= GameLogic.calculate_score(dice_roll)
                if remaning_dices_score == 0:

                    unbanked_score = 0
                    print("****************************************")
                    print("**        Zilch!!! Round over         **")        
                    print("****************************************")
                    print(f"You banked 0 points in round {round_num}")
                    print("Total score is 0 points")
                    break
                dice_kept = []

        if choice == "q":
            break

    return total_score

def decline_game():
    """
    A function to display a message when the user declines to play the Ten Thousand game.

    Parameters:
    None

    Returns:
    None
    """
    print("OK. Maybe another time")

def ask_for_input():
    """
    A function to prompt the user to enter the dice they want to keep, or quit the game.

    Parameters:
    None

    Returns:
    choice (str): The user's input.
    """
    print("Enter dice to keep, or (q)uit:")
    choice = input("> ")    
    x = choice.replace(" ","")
    return x

def cheater_function(dice_roll,dice_kept,unpacked_tuple):
    """
    A function to check if the user is cheating by keeping dice that were not rolled.

    Parameters:
    dice_roll (tuple): A tuple of the dice that were rolled.
    dice_kept (list): A list of the dice that the user wants to keep.
    unpacked_tuple (str): A string representation of the dice that were rolled.

    Returns:
    cheater (bool): True if the user is cheating, False otherwise.
    """
    cheater=False
    z=list(dice_roll)
    for x in dice_kept:
                if x not in z:
                    print("Cheater!!! Or possibly made a typo...")
                    print("*** " + unpacked_tuple + " ***")
                    cheater=True
                    break
                else: 
                    z.remove(x)
    # quit_input=input("> ")
    return cheater                

def hot_dice_fun(dice_kept, unbanked_score):
    """
    A function to handle the case where the user rolls and keeps all six dice, also known as hot dice.

    Parameters:
    dice_kept (list): A list of the dice that the user wants to keep.
    unbanked_score (int): The score that the user has accumulated in the current round.

    Returns:
    choice (str): The user's choice, to roll again, bank their points, or quit the game.
    """
    round_score = GameLogic.calculate_score(dice_kept)
    unbanked_score += round_score
    num_of_dice = 6
    print(f"You have {unbanked_score} unbanked points and {num_of_dice} dice remaining")

    print("(r)oll again, (b)ank your points or (q)uit:")
    choice = input("> ")
    return choice
if __name__=="__main__":
    play()




