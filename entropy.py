from math import log2

def calculate_password_entropy(password, character_set_size):
    password_length = len(password)
    return password_length * log2(character_set_size)

if __name__ == "__main__":
    # Example usage:
    password = "password"
    character_set_size = 72  # Example: upper and lower case letters, digits, and common special characters
    entropy = calculate_password_entropy(password, character_set_size)
    print(f"Entropy of the password '{password}' using a character set size of {character_set_size}: {entropy} bits")
