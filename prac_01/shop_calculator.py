BONUS = 0.10


total_price = 0
num_of_item = int(input("Number of items: "))
for i in range(0, num_of_item, 1):
    price = float(input("Price of item: "))
    while price < 0:
        print("Invalid number of items!")
        price = float(input("Price of item: "))
    total_price += price
if total_price >= 100:
    total_price = total_price * (1 - BONUS)
print(f"Total price for {num_of_item} items is ${total_price:.2f} ")