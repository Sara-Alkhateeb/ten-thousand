
from game_logic import GameLogic
# from ten_thousand.game_logic import GameLogic

dice_roller = GameLogic.roll_dice

def play(roller=GameLogic.roll_dice):
    global dice_roller
    dice_roller = roller

    choice = invite_to_play()
    if choice == "y":
        score = start_game()
        print(f"Thanks for playing. You earned {score} points")
    else:
        decline_game()

def invite_to_play():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")
    return choice

def start_game(max_round=40):
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
                    
            # cheater_repet=False
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
            print(f"You have {unbanked_score} unbanked points and {num_of_dice - len(dice_kept)} dice remaining")

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
                num_of_dice -= len(dice_kept)
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
                    print("**         Zilch!!! Round over        **")        
                    print("****************************************")
                    print(f"You banked 0 points in round {round_num}")
                    print("Total score is 0 points")
                    break
                dice_kept = []

        if choice == "q":
            break

    return total_score

def decline_game():
    print("OK. Maybe another time")

def ask_for_input():
    print("Enter dice to keep, or (q)uit:")
    choice = input("> ")
    return choice

def cheater_function(dice_roll,dice_kept,unpacked_tuple):
    cheater=False
    z=list(dice_roll)
    for x in dice_kept:
                if x not in z:
                    print("Cheater!!! Or Possibly made a typo...")
                    print("*** " + unpacked_tuple + " ***")
                    cheater=True
                    break
                else: 
                    z.remove(x)
    # quit_input=input("> ")
    return cheater                


if __name__=="__main__":
    play()




