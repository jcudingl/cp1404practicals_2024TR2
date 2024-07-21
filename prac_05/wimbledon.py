"""
Wimbledon
Estimate: 30 minutes
Actual:   20 minutes
"""


def main():
    filename = "wimbledon.csv"
    data = read_file(filename)
    champions_in_wimbledon = count_champions(data)
    champion_countries = get_countries(data)

    print("Wimbledon Champions: ")
    for champion, count in champions_in_wimbledon.items():
        print(champion, count)

    print(f"\nThese {len(champion_countries)} countries have won Wimbledon:")
    print(",".join(country for country in champion_countries))


def read_file(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            data.append(line.strip().split(","))
        del data[0]
    return data


def count_champions(data):
    champions = {}
    for line in data:
        player_name = line[2]
        if player_name in champions:
            champions[player_name] += 1
        else:
            champions[player_name] = 1
    return champions


def get_countries(data):
    countries = set()
    for line in data:
        countries.add(line[1])
    return sorted(countries)


main()
