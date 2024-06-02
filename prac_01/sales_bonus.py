"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_HIGH = 0.15
BONUS_LOW = 0.10

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus_rate = BONUS_HIGH
    else:
        bonus_rate = BONUS_LOW
    bonus = sales * bonus_rate
    print(f"Bonus: ${bonus}")
    sales = float(input("Enter sales: $"))
print("Finished.")
