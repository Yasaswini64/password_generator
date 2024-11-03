import random
import string
def generate_password(length, use_digits=True, use_uppercase=True, use_lowercase=True, use_special=True):
    character_pool = ''
    if use_digits:
        character_pool += string.digits  # Adds numbers 0-9
    if use_uppercase:
        character_pool += string.ascii_uppercase  # Adds A-Z
    if use_lowercase:
        character_pool += string.ascii_lowercase  # Adds a-z
    if use_special:
        character_pool += string.punctuation  # Adds special characters like @, #, etc.
    
    if not character_pool:
        return "Please select at least one character type."

    # Generate the password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password
if __name__ == "__main__":
    length = int(input("Enter the desired password length (minimum 8): "))
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    if length < 8:
        print("Password length should be at least 8 characters.")
    else:
        password = generate_password(length, use_digits, use_uppercase, use_lowercase, use_special)
        print("Generated Password:", password)
