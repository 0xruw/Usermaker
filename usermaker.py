import os
import random
import string

def display_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(r"""
    
,---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
| ~ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | [ | ] | <-    |
|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----| 
| ->| | " | , | . | P | Y | F | G | C | R | L | / | = |  \  | 
|-----',--',--',--',--',--',--',--',--',--',--',--',--'-----| 
| Caps | A | O | E | U | I | D | H | T | N | S | - |  Enter | 
|------'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'--------| 
|        | ; | Q | J | K | X | B | M | W | V | Z |          | 
|------,-',--'--,'---'---'---'---'---'---'---'---',--,------| 
| ctrl |  | alt |                          | alt  |  | ctrl | 
'------'  '-----'--------------------------'------'  '------'
    
          by : 0xruw

    """)

def generate_usernames():
    try:
        # Request user input for number of usernames and their length
        num_users = int(input("Enter the number of usernames to generate: "))
        username_length = int(input("Enter the length of each username: "))

        # Validate input
        if num_users <= 0 or username_length <= 2:  # Ensure usernames have at least 3 characters
            print("Please enter positive numbers and username length >= 3.")
            return

        # Allowed characters (lowercase letters, digits, '.', '_')
        allowed_chars = string.ascii_lowercase + string.digits + "._"

        # Generate and save usernames to list.txt
        with open("list.txt", "w") as file:
            for i in range(num_users):
                # Generate username that doesn't start or end with '.' or '_'
                while True:
                    username = ''.join(random.choices(allowed_chars, k=username_length))
                    if username[0] not in "._" and username[-1] not in "._":
                        break

                # Write to file
                file.write(username + "\n")

                # Clear screen and print progress every 1000 usernames
                if (i + 1) % 1000 == 0 or (i + 1) == num_users:
                    os.system("cls" if os.name == "nt" else "clear")
                    percentage = ((i + 1) / num_users) * 100
                    print(r"""
    
,---,---,---,---,---,---,---,---,---,---,---,---,---,-------,
| ~ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 | [ | ] | <-    |
|---'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-----| 
| ->| | " | , | . | P | Y | F | G | C | R | L | / | = |  \  | 
|-----',--',--',--',--',--',--',--',--',--',--',--',--'-----| 
| Caps | A | O | E | U | I | D | H | T | N | S | - |  Enter | 
|------'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'-,-'--------| 
|        | ; | Q | J | K | X | B | M | W | V | Z |          | 
|------,-',--'--,'---'---'---'---'---'---'---'---',--,------| 
| ctrl |  | alt |                          | alt  |  | ctrl | 
'------'  '-----'--------------------------'------'  '------'
            Insta : 0xruw
    """)
                    print(f"usernames generated ({int(percentage)}%)...")

        print(f"Successfully saved {num_users} usernames to list.txt!")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def main():
    display_banner()
    generate_usernames()

# Run the program
if __name__ == "__main__":
    main()
