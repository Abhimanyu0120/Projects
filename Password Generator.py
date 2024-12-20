
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Password Generator")
try:
    length = int(input("Enter the desired length of the password: "))

    if length < 8:
        print("Password length must be at least 8.")
    else:
        generated_password = generate_password(length)
        print(f"Generated Password: {generated_password}")
except ValueError:
    print("Please enter a valid number.")
