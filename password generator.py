import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Password length must be greater than 0.")
            continue
        password = generate_password(password_length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number for password length.")    
    another_password = input("Generate another password? (yes/no): ").lower()
    if another_password != "yes":
        break
