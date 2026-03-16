import random
import string

Password_Length = int(input("Enter the length of the password: "))
Password_characters = string.ascii_letters + string.digits + string.punctuation

Password = ''.join(random.choice(Password_characters) for i in range(Password_Length))

print("Generated Password: ", Password)