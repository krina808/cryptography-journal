
def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine shift direction for encryption or decryption
            shift_amount = shift if encrypt else -shift
            # Convert character using ASCII values, maintain case
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

def get_valid_shift():
    while True:
        try:
            shift_value = int(input("Enter shift value (1-25): "))
            if 1 <= shift_value <= 25:
                return shift_value
            else:
                print("Invalid input. Please enter a number between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Example usage
plain_text = input("Enter your message: ")
shift_value = get_valid_shift()

# Encrypt and Decrypt
cipher_text = caesar_cipher(plain_text, shift_value)
print("\nEncrypted Message:", cipher_text)
print("Decrypted Message:", caesar_cipher(cipher_text, shift_value, encrypt=False))

