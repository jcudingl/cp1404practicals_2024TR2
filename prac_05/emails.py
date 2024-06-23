"""
Emails
Estimate: 10 minutes
Actual:   15 minutes
"""
email_dictionary = {}
email = input("Email: ")
while email != "":
    name = " ".join(word.capitalize() for word in email.split("@")[0].split("."))
    check = input(f"Is your name {name}? (Y/n)")
    if check == "Y" or check == "":
        email_dictionary[name] = email
    else:
        name = input("Name: ")
        email_dictionary[name] = email
    email = input("Email: ")
for name, email in email_dictionary.items():
    print(f"{name}({email})")
