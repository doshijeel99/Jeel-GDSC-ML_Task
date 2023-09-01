import random
def generate_password(length, special):
    if special == 'y':
        l = int(input("Enter how many special characters: "))
        special_chars = random.choices('!@#$%^&*().,<>?/:;[]-_+=', k=l)
        password_chars = random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz', k=length - l)
        password = ''.join(password_chars + special_chars)
    else:
        password = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz', k=length))
    print("Password:", password)
length = int(input("Enter length: "))
special = input("Do you want special characters? (y/n)").lower()
generate_password(length, special)