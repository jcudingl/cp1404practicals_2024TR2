from guitar import Guitar
guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]
name = input("Name: ")
if name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{guitars[-1]} added.")
    name = input("Name: ")
print("\n... snip ...\nThese are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    # do something with i (the index) and guitar (the element)
