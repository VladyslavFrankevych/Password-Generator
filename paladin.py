import random
import string
import argparse
import colorama

colorama.init(autoreset=True)

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    # Generate a random password using the string module
    choices = ""
    if include_uppercase:
        choices += string.ascii_uppercase
    if include_lowercase:
        choices += string.ascii_lowercase
    if include_numbers:
        choices += string.digits
    if include_symbols:
        choices += string.punctuation
    return ''.join(random.choices(choices, k=length))


def main():
    # Set up the CLI interface
    print(f"""{colorama.Fore.MAGENTA}
   ______     _           _ _       
   | ___ \   | |         | (_)      
   | |_/ /_ _| | __ _  __| |_ _ __  
   |  __/ _` | |/ _` |/ _` | | '_ \ 
   | | | (_| | | (_| | (_| | | | | |
   \_|  \__,_|_|\__,_|\__,_|_|_| |_|
    """)
    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument("-l", "--length", type=int, default=8, help="The password length (default: 8) 🔢")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters in the password 🔠")
    parser.add_argument("-lc", "--lowercase", action="store_true", help="Include lowercase letters in the password 🔡")
    parser.add_argument("-n", "--numbers", action="store_true", help="Include numbers in the password 🔢")
    parser.add_argument("-s", "--symbols", action="store_true", help="Include symbols in the password 🔣")
    args = parser.parse_args()

    # Generate and print the password
    password = generate_password(args.length, args.uppercase, args.lowercase, args.numbers, args.symbols)
    print("Generated password:", password)


if __name__ == "__main__":
    main()
