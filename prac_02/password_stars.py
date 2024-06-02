MIN_LENGTH = 6


def main():
    password = get_password()
    print_password(password)


def print_password(password):
    print("PW: ", end='')
    for i in range(len(password)):
        print("*", end='')
    print()


def get_password():
    password = input(f"PW(minimum length:{MIN_LENGTH}): ")
    while len(password) < MIN_LENGTH:
        print("Invalid Password")
        password = input(f"PW(minimum length:{MIN_LENGTH}): ")
    return password


main()
