import random
from DataBase import sqldb


# Password Generator Class
class PasswordGenerator:

    @staticmethod
    def __PasswordGenerate__(Char_Length):
        # Alphabets, numbers, and symbols
        data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '`', '~', '!', '@', '#',
                '$', '%', '(', ')', '[', ']', '{', '}', ';']
        random.shuffle(data)
        return print("You password is ", *data[:Char_Length], sep="")

    @staticmethod
    def __StorePassword__():
        try:
            # Taking Input From the User
            Website_Input = input("WebSite Name: ")
            User_value, Password_value = input(
                f"What is the Username and Password for {Website_Input} (Ex. Username(or Email) , Password format): ").split(
                ",")
            # initializing the DataBase module
            DataBase = sqldb(Website_Input, User_value, Password_value)
            DataBase.__addData__()
        except ValueError:
            print("To many values are given")

    @staticmethod
    def __FetchData__():
        Website_Input = input("Website Name: ")
        DataBase = sqldb(Website_Input, None, None)
        DataBase.__FetchData__()

