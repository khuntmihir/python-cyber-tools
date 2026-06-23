import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password

try:
    length = int(input("Enter password length: "))

    if length < 8:
        print("Password length should be at least 8 characters.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number.")
