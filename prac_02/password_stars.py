MIN_LENGTH = 6


def main():
    """Main function"""
    password = get_password()
    print_password(password)


def get_password():
    """To get password"""
    password = input(f"PW(minimum length:{MIN_LENGTH}): ")
    while len(password) < MIN_LENGTH:
        print("Invalid Password")
        password = input(f"PW(minimum length:{MIN_LENGTH}): ")
    return password


def print_password(password):
    """To print password"""
    print("PW: ", end='')
    for i in range(len(password)):
        print("*", end='')
    print()


main()
