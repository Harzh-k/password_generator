import random
import string

# Character sets
letters = string.ascii_lowercase     # 'abcdefghijklmnopqrstuvwxyz'
u_letters = string.ascii_uppercase   # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = string.digits              # '0123456789'
symbols = "!@#$%&"

# User input
letters_count = int(input("How many letters you want? : "))
numbers_count = int(input("How many numbers you want? : "))
symbols_count = int(input("How many symbols you want? : "))

# Build password list with one uppercase letter
password = [random.choice(u_letters)]

# Remaining lowercase letters
for i in range(letters_count - 1):
    password.append(random.choice(letters))

# Numbers
for j in range(numbers_count):
    password.append(random.choice(numbers))

# Symbols
for k in range(symbols_count):
    password.append(random.choice(symbols))

# Shuffle and join into string
random.shuffle(password)
main_password = "".join(password)

print("Your password is:", main_password)
