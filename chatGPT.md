## query :
create a function named roll_dice The input to roll_dice is an integer between 1 and 6. The output of roll_dice is a tuple with random values between 1 and 6. The length of tuple must match the argument given to roll_dice method.

## Code:
    import random

    def roll_dice(num_dice):
    return tuple(random.randint(1, 6) for _ in range(num_dice))

## query :
creat an equation to find the score according these rules :

        ####################### One
        if count_result[1]==3:
            unbanked_points+=1000
        if count_result[1]==4:
            unbanked_points+=2000
        if count_result[1]==5:
            unbanked_points+=4000
        if count_result[1]==6:
            unbanked_points+=8000 
        ####################### fives
        if count_result[5]==3:
            unbanked_points+=500
        if count_result[5]==4:
            unbanked_points+=1000                    
        if count_result[5]==5:
            unbanked_points+=2000
        if count_result[5]==6:
            unbanked_points+=4000

## Code:
      ####################### One
      scores = {3: 1000, 4: 2000, 5: 4000, 6: 8000}
      unbanked_points += scores.get(count_result[1], 0)
      ####################### fives
      points_dict = {3: 500, 4: 1000, 5: 2000, 6: 4000}
      unbanked_points += points_dict.get(count_result[5], 0)