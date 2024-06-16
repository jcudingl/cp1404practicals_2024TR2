import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_IN_A_LINE = 6

numbers = list(range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1))
number_of_quick_pick = int(input("How many quick picks? "))
for line in range(number_of_quick_pick):
    random.shuffle(numbers)
    quick_pick = sorted(numbers[:NUMBER_IN_A_LINE])
    print("".join(f"{number:2} " for number in quick_pick))
