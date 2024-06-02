print("Loops")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

print()
print("Problem a")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

print()
print("Problem b")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

print()
print("Problem c")
num_of_star = int(input("Number of stars: "))
for i in range(0, num_of_star, 1):
    print("*", end='')
print()

print()
print("Problem d")
for col in range(0, num_of_star, 1):
    for line in range(0, col + 1, 1):
        print("*", end='')
    print()
print()

print("Finished.")