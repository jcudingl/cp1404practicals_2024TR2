from guitar import Guitar

guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_2 = Guitar("Another Guitar", 2013, 10000)
print(f"{guitar_1.name} get_age() - Except {2024-1922}. Got {guitar_1.get_age()}")
print(f"{guitar_2.name} get_age() - Except {2024-2013}. Got {guitar_2.get_age()}")
print(f"{guitar_1.name} is_vantage() - Except {2024-1922 >= 50}. Got {guitar_1.is_vintage()}")
print(f"{guitar_2.name} is_vantage() - Except {2024-2013 >= 50}. Got {guitar_2.is_vintage()}")
