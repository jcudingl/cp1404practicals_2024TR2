"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Fix this!


def main():
    score = float(input("Enter score: "))
    status = determine_status(score)
    print(status)


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
