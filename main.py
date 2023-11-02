import random
import string

def createPassword(length):
    stringOne = string.ascii_letters + string.punctuation + string.digits
    password = random.choices(stringOne, k=length)
    return "".join(password)

def main():
    print(
      '''
      Password Generator v1.0
=====================================================================================================
This little program will create a random password based on the number of characters that you give it
All password contain upper/lower characters, numbers and punctuation
Its suggested to have a minimum of 16 characters!!
===================================================================================================== 
      '''
      )

    user_answer = input('How many characters do you want the password to be?: ')
    try:
        password_length = int(user_answer)
        if type(password_length) == int:
            print(createPassword(password_length))
    except ValueError:
        print("Invalid input. Please enter a valid integer")
        main()

main()