# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 1.
Ceci est le fichier template pour la partie 1 du Prelim 1.
"""

# just a small helper to visualize the tail
def print_tail(tail: [str]):
    for line in tail:
        print(line)

def part_1(size: int):
    """
    Draw the platypus tail

    Parameters:
        size int: Size of the tail

    Returns:
        [String]: The platypus tail drawn
    """
    tail = []
    ### YOUR CODE GOES HERE ###

    for nb_row in range(size + 1):
        tail.append("|" + "_." * (2 *size - 1) + "_|")
    
    for nb_row in range(1, size + 1):
        tail.append(" " *nb_row + "\\" + "_." * (2 *size -1 -nb_row) + "_/" + " " *nb_row)

    return tail
