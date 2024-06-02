"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Fix this!
MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Main function"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            status = determine_status(score)
            print(status)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


def get_valid_score():
    """Get a valid score input"""
    score = input("Enter score: ")
    while float(score) < 0 or float(score) > 100:
        print("Invalid score")
        score = input("Enter score: ")
    return score


def determine_status(score):
    """Determine status based on score"""
    if float(score) >= 90:
        return "Excellent"
    elif float(score) >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Show stars as many as score length"""
    for i in range(len(score)):
        print("*", end='')
    print()


main()
