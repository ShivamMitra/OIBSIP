import random
import string

# Function to generate a random password
def generate_password(length, use_letters, use_numbers, use_symbols):
    # Define the character sets
    letters = string.ascii_letters if use_letters else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Combine the character sets
    characters = letters + numbers + symbols
    
    # Ensure there's at least one character type
    if not characters:
        print("Please select at least one character type (letters, numbers, symbols).")
        return None
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user for password length
    length = int(input("Enter the desired password length: "))
    
    # Ask the user if they want to include letters, numbers, and symbols
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    # Generate the password
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    
    if password:
        print(f"Your generated password is: {password}")
    else:
        print("Password generation failed.")

if __name__ == "__main__":
    main()