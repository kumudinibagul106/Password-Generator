import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    length_score = min(len(password) / 20.0, 1.0)
    upper_case = any(char.isupper() for char in password)
    lower_case = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = any(char in string.punctuation for char in password)

    complexity = upper_case + lower_case + digit + special_char
    complexity_score = min(complexity / 3, 1.0)

    strength = length_score * complexity_score
    return strength

if __name__ == "__main__":
    # Generate a random password of length 16
    password = generate_password(length=16)
    print("Password:", password)

    # Calculate the strength of the generated password
    strength = password_strength(password)
    print("Strength:", strength)
