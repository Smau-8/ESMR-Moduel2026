# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 1.
Ceci est le fichier template pour la partie 3 du Prelim 1.
"""

def part_3(sentence: str):
    """
    Find "ornithorynque" in the sentence

    Parameters:
        sentence str: The sentence that may contain contain the letters of "ornithorynque"

    Returns:
        [int]: The position of the letters found
    """
    word = "ornithorynque"
    positions = []
    ### You code goes here ###
    ### Votre code va ici ###

    for capital_chr, lowercase_chr in zip("ornithorynque", "ORNITHORYNQUE"):
        found = False
        for pos, chr in enumerate(sentence):
            if capital_chr == chr and pos not in positions:
                positions.append(pos)
                found = True
                break
            elif lowercase_chr == chr and pos not in positions:
                positions.append(pos)
                found = True
                break
        if found == False:
            positions.append(-1)
    
    
    return positions

