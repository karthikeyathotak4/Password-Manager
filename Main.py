from PasswordGenerator import PasswordGenerator
import os

print("Welcome to PassGru\n".center(os.get_terminal_size().columns))
User_In = int(input("[1] Sava a new password\n[2] Generate a new password: "))

if User_In == 1:
    pass

elif User_In == 2:
    Char = int(input("How many letter do you want in you Password(Ex. 15): "))
    PasswordGenerator.__PasswordGenerate__(Char)
else:
    print("Sorry Worry input")