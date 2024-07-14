HEX_COLOURS = {"absolutezero": "#0048ba",
               "acidgreen": "#b0bf1a",
               "aliceblue": "#f0f8ff",
               "alizarincrimson": "#e32636",
               "amaranth": "#e52b50",
               "amber": "#ffbf00",
               "amethyst": "#9966cc",
               "antiquewhite": "#faebd7",
               "apricot": "#fbceb1",
               "aqua": "#00ffff"}

colour_name = input("Enter Colour Name: ").strip().lower()
while colour_name != "":
    if colour_name in HEX_COLOURS:
        print(f"The code of {colour_name} is {HEX_COLOURS[colour_name]}.")
    else:
        print("Invalid Colour Name")
    colour_name = input("Enter Colour Name: ").strip().lower()
