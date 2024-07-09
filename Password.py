import random
import string

def generate_password(length=8):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")
    
    # Character sets to choose from
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure the password has at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random choices from all sets
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    # Convert the list to a string and return
    return ''.join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length (minimum 8): "))
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)
