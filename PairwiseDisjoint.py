def pairwiseDisjoint(listOfSets):
    superSet = set()
    for _set in listOfSets:
        superSet = superSet.union(_set)
    return superSet
