from prac_07.guitar import Guitar

FILE_NAME = 'guitars.csv'


def main():
    """Main function of this project"""
    guitars = []
    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)

    show_current_guitar(guitars)
    sorted_guitars = sorted(guitars)
    print("\nAfter Sorted\n")
    show_current_guitar(sorted_guitars)

    add_new_guitars(guitars)

    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def show_current_guitar(guitars):
    """Print current guitar in list"""
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    """Add new guitars to list"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(Guitar(name, year, cost))
        print(f"{guitar} added.")
        name = input("Name: ")


main()
