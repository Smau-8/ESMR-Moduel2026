# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 1.
Ceci est le fichier template pour la partie 4 du Prelim 1.
"""

def part_4(positions):
    """
    Find the closest preys to the platypus

    Parameters:
        positions [(int, int, int)]: The position of the platypus and all the preys

    Returns:
        [int]: The ascending order of the preys' distance to the platypus
    """
    order = []
    ### You code goes here ###
    ### Votre code va ici ###
    platypus = positions[0]
    distance = lambda x,y,z: math.sqrt((platypus[0]-x)**2 + (platypus[1]-y)**2 + (platypus[2]-z)**2)
    preys_distance = []
    
    for prey, coordinates in enumerate(positions[1:]):
        preys_distance.append((prey + 1, distance(coordinates[0],coordinates[1],coordinates[2])))
    
    preys_distance.sort(key = lambda x: x[1])

    order = [i for i,_ in preys_distance]
    

    return order
