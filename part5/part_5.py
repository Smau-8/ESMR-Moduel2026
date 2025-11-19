# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 1.
Ceci est le fichier template pour la partie 5 du Prelim 1.
"""

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

    board = [list(row) for row in board]
    foods = []
    hunger = 0
    nb_turn = 0
    
    while hunger < 3 and nb_turn < turns:
        for y,row in enumerate(board):
            for x,el in enumerate(row):
                if el == "x":
                    if board[y][x+1] == ".":
                        hunger = 0
                        board[y][x+1] = "x"
                        board[y][x] = "_"
                        continue
                    if board[y+1][x] == ".":
                        hunger = 0
                        board[y+1][x] = "x"
                        board[y][x] = "_"
                        continue
                    if board[y][x-1] == ".":
                        hunger = 0
                        board[y][x-1] = "x"
                        board[y][x] = "_"
                        continue
                    if board[y][x-1] == ".":
                        hunger = 0
                        board[y-1][x] = "x"
                        board[y][x] = "_"
                        continue
                if el == ".":
                    foods.append((x,y))
                


    print(board)
    return final_answer

print(part_5( turns = 11, 
        board = [
            "____x.________._",
            "_______.________",
            "_________..___._",
            "_.__._____.____.",
            "_________.__.___",
            ".____________._.",
            "_.__________.___",
            "__.______..__.__",
            "____._______.___",
            ".__.___.________",
            "______._________",
            "____..._____.___",
            "__..___.._______",
            "_______________.",
            "________._._____",
            "____.._______.__",
        ]))
