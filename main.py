#Password Generator 
import random 

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '-', '+']

print("Welcome to the password generator program ")
u_letters = int(input("How many letters would you put in your password? \n"))
u_symbols = int(input("How many symbols would you put in your password? \n"))
u_numbers = int(input("How many numbers would you put in your password? \n"))

password = []

for char in range(1, u_letters +1):
    password += random.choice(letters)

for char in range(1, u_symbols +1):
    password += random.choice(symbols)

for char in range(1, u_numbers +1):
    password += random.choice(numbers)

random.shuffle(password)

password_string = ""
for char in password:
    password_string += char 

print(f"your password is {password_string}")