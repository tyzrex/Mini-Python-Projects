import secrets
import string
from pyfiglet import Figlet
from simple_term_menu import TerminalMenu

f = Figlet(font='slant')
options = ["yes", "no"]


def print_title():
    print(f.renderText('Password Generator'))


def get_user_options():
    print("Do you want to use default settings? ")
    settings = TerminalMenu(options).show()
    if (settings == 1):
        print("Choose password length: ")
        length = int(input("\nEnter password length: "))
        print("Choose password type: ")
        password_type_options = ["alphanumeric", "letters", "digits"]
        password_type = TerminalMenu(password_type_options).show()
        password_type_choice = password_type_options[password_type]
        print(f"\nYou have selected {password_type_choice} password type!")
        return length, password_type_choice

    else:
        print("\nDefault settings: 10 characters, alphanumeric password")
        return 10, "alphanumeric"


def generate_password(length, password_type):
    print("\nGenerating password...")
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    password = ''.join(secrets.choice(letters + digits + special_characters) if password_type == "alphanumeric" else 
                       secrets.choice(letters) if password_type == "letters" else 
                       secrets.choice(digits) for i in range(length))
    
    print("\nYour generated password is: ")
    print(password, end="")
        
        
if __name__ == "__main__":
    print_title()
    length, password_type = get_user_options()
    generate_password(length, password_type)

