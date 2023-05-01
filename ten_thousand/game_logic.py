import random
from collections import Counter

class GameLogic:

    def __init__():
        pass

    """
    the below function will take an argument of num_dice and will return a tuple of random numbers between 1-6 and the length of the tuple is the same as the taken argument
    """
    def roll_dice(num_dice):
      values = [random.randint(1, 6) for _ in range(num_dice)]
      return  (values)
    
    """
    the function below takes argument of a tuple and works as :
    The input to calculate_score function is a tuple of integers that represents a dice roll.
    The output from calculate_score is an integer representing the roll’s score according to rules of the game.
    link to the rules :
    https://en.wikipedia.org/wiki/Dice_10000
    """
    def calculate_score(roll):
      unbanked_points = 0
      count_result = Counter(roll)

      ############################ ones
      scores = {3: 1000, 4: 2000, 5: 4000, 6: 8000}
      unbanked_points += scores.get(count_result[1], 0)

      if count_result[1]<3:
            unbanked_points+=100*count_result[1]
      ############################ five
      points_dict = {3: 500, 4: 1000, 5: 2000, 6: 4000}
      unbanked_points += points_dict.get(count_result[5], 0)

      if count_result[5]<3:
            unbanked_points+=50*count_result[5]
      #################### three of a kind 
      if count_result[2]==3:
            unbanked_points+=200
      if count_result[3]==3:
            unbanked_points+=300 
      if count_result[4]==3:
            unbanked_points+=400
      if count_result[6]==3:
            unbanked_points+=600
            ###################### four of a kind 
      if count_result[6]==4:
            unbanked_points+=1200
      if count_result[4]==4:
            unbanked_points+=800
      if count_result[3]==4:
            unbanked_points+=600 
      if count_result[2]==4:
            unbanked_points+=400
            ###################### five of a kind 
      if count_result[6]==5:
            unbanked_points+=2400
      if count_result[4]==5:
            unbanked_points+=1600
      if count_result[3]==5:
            unbanked_points+=1200 
      if count_result[2]==5:
            unbanked_points+=800                                   
            ###################### six of a kind 
      if count_result[6]==6:
            unbanked_points+=4800
      if count_result[4]==6:
            unbanked_points+=3200
      if count_result[3]==6:
            unbanked_points+=2400 
      if count_result[2]==6:
            unbanked_points+=1600      
      

      ###################### straight
      if count_result[1]==1 and count_result[2]==1 and  count_result[3]==1 and count_result[4]==1 and count_result[5]==1 and count_result[6]==1:
            unbanked_points=2000 
      ########################## three pairs
      if len(count_result)==3 and len(set(count_result.values()))==1 and list(set(count_result.values()))[0]==2:
            unbanked_points=1500
      ############################# two pairs 
      if len(count_result)==2 and len(set(count_result.values()))==1 and list(set(count_result.values()))[0]==3:
            unbanked_points=unbanked_points*2           
                                                                                                                  
      return unbanked_points     

@staticmethod
def validate_keepers(dice_roll,dice_kept):
        cheater=True
        z=list(dice_roll)
        for x in dice_kept:
            if x not in z:
                cheater=False
            else: 
                z.remove(x)
        return cheater 
   
@staticmethod
def get_scorers(test_input):
        main_score = GameLogic.calculate_score(test_input)
        # print(main_score)
        scorers = []
        input_list = list(test_input)
        # print(range(len(input_list)))
        for i,val in enumerate(input_list):
            input_list.pop(i)
            element_score = GameLogic.calculate_score(tuple(input_list))
            # print()
            if element_score != main_score:
                # print("x")
                scorers.append(val)
                input_list.insert(i,val)
            else:
                input_list.insert(i,val)   
        scorers_tuple = tuple(scorers) 
        # print(scorers_tuple)       
        return scorers_tuple 
    



