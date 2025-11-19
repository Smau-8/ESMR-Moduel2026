# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 1.
Ceci est le fichier template pour la partie 5 du Prelim 1.
"""

import math
def part_5(turns: int, board: [str]):
    """
    Simulate the Game of platypus

    Parameters:
        turns str: The number of turns in the game
        board [str]: The 16x16 grid representing the board of the Game of platypus with x as the platypus and . the food

    Returns:
        str: Is the platypus surviving ("Yes" or "No")
    """
    final_answer = "No"
    ### You code goes here ###
    ### Votre code va ici ###

    final_answer = "Yes"
    hunger = 0
    foods = []
    board = [list(row) for row in board]
    pl_moved = False
    distance = lambda x,y,xy: math.sqrt((xy[0]-x)**2 + (xy[1]-y)**2)
    for turn in range(turns):
        hunger += 1
        pl_moved = False
        foods = []

        for y, row in enumerate(board):
            for x,el in enumerate(row):
                if el == "x" and pl_moved == False:
                    platypus = (x,y)
                    if x+1 < len(board[1]) and board[y][x+1] == ".":
                        board[y][x], board[y][x +1] = "_","x"
                        hunger,pl_moved = 0, True
                        continue
                    if y+1 < len(board) and board[y+1][x] == ".":
                        board[y][x],board[y+1][x] = "_","x"
                        hunger,pl_moved = 0, True
                        continue
                    if x-1 >= 0 and board[y][x-1] == ".":
                        board[y][x],board[y][x-1] = "_","x"
                        hunger,pl_moved = 0, True
                        continue
                    if y-1 >= 0 and board[y-1][x] == ".":
                        board[y][x],board[y-1][x] = "_","x"
                        hunger,pl_moved = 0, True
                        continue
                if el == ".":
                    foods.append((x,y))

        if pl_moved == False and foods:
            closest = [(float('inf'),(0,0))]
            for food in foods:
                food_distance = (distance(platypus[0],platypus[1],food), (food[0], food[1]))
                if food_distance[0] < closest[0][0]: 
                    closest = [food_distance]
                if food_distance[0] == closest[0][0]:
                    closest.append(food_distance)

            directions = []
            for food in closest:
                if food[1][0] - platypus[0] > 0:
                    directions.append("right")
                elif food[1][0] - platypus[0] < 0:
                    directions.append("left")
                elif food[1][1] - platypus[1] > 0:
                    directions.append("down")
                elif food[1][1] - platypus[1] < 0:
                    directions.append("up")

            if "right" in directions:
                board[platypus[1]][platypus[0]], board[platypus[1]][platypus[0] +1] = "_","x"
            elif "down" in directions:
                board[platypus[1]][platypus[0]], board[platypus[1] +1][platypus[0]] = "_","x"
            elif "left" in directions:
                board[platypus[1]][platypus[0]], board[platypus[1]][platypus[0] -1] = "_","x"
            elif "up" in directions:
                board[platypus[1]][platypus[0]], board[platypus[1] -1][platypus[0]] = "_","x"

        if hunger >= 3:
            return "No"

    
    return final_answer
