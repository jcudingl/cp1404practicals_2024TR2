FILE_NAME_Q1 = "name.txt"
FILE_NAME_Q3 = "numbers.txt"

# Question 1
print("Python File Question 1")
user_name = input("Name: ")
out_file = open(FILE_NAME_Q1, "w")
print(user_name, file=out_file)
out_file.close()
print()

# Question 2
print("Python File Question 2")
in_file = open(FILE_NAME_Q1, "r")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()
print()

# Question 3
print("Python File Question 3")
with open(FILE_NAME_Q3, 'r') as file:
    result = 0
    for i in range(2):
        result += int(file.readline().strip())
    print(f"The total of first two numbers is {result}")
print()

# Question 4
print("Python File Question 4")
with open(FILE_NAME_Q3, 'r') as file:
    result = 0
    for line in file:
        result += int(line)
    print(f"The total of numbers is {result}")