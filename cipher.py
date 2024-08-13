def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust the shift value for decryption
    if mode == 'decrypt':
        shift = -shift

    # Iterate over each character in the text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, leave it unchanged
        else:
            result += char

    return result

def main():
    # Get user input for the operation
    mode = input("Would you like to encrypt or decrypt the message? (enter 'encrypt' or 'decrypt'): ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        return

    # Get the message and shift value from the user
    message = input("Enter the message: ").strip()
    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    # Perform encryption or decryption
    result = caesar_cipher(message, shift, mode)

    # Display the result
    print(f"The {mode}ed message is: {result}")
    
    # Keep the program open until the user presses Enter
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
