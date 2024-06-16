numbers = [3, 1, 4, 1, 5, 9, 2]

numbers[0]
# My answer: 3
# Result in Python Console: 3
# Correct
numbers[-1]
# My answer: 2
# Result in Python Console: 2
# Correct
numbers[3]
# My answer: 1
# Result in Python Console: 1
# Correct
numbers[:-1]
# My answer: [2, 9, 5, 1, 4, 1, 3]
# Result in Python Console: [3, 1, 4, 1, 5, 9]
# Wrong
numbers[3:4]
# My answer: [1]
# Result in Python Console: [1]
# Correct
5 in numbers
# My answer: True
# Result in Python Console: True
# Correct
7 in numbers
# My answer: False
# Result in Python Console: False
# Correct
"3" in numbers
# My answer: False
# Result in Python Console: False
# Correct
numbers + [6, 5, 3]
# My answer: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Result in Python Console: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Correct

# Q1
numbers[0] = "ten"
# Q2
numbers[-1] = 1
# Q3
print(numbers[2:])
# Q4
print(9 in numbers)
