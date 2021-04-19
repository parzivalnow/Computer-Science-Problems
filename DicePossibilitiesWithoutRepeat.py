import math
def numberOfPermutationsOfDiceWithoutRepeat(number, amountTaken, times):
    ans = math.factorial(number)/math.factorial(number-amountTaken)
    number -= amountTaken
    for i in range(times-1):
        if number <= 0:
            return ans
        ans *= math.factorial(number)/math.factorial(number-amountTaken)
        number -= amountTaken
    return ans
