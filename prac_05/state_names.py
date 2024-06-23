"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

for code in CODE_TO_NAME:
    print(f"{code:3} is {CODE_TO_NAME[code]}")

state_code = input("Enter short state: ").upper()
try:
    print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
except KeyError:
    print("Invalid short state")
