def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) + shift - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift - 97) % 26 + 97)
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message
def decrypt(encrypted_message, shift):
    return encrypt(encrypted_message, -shift)
if __name__ == "__main__":
    while True:
        user_choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
        user_message = input("Enter your message: ")
        user_shift = int(input("Enter shift value: "))
        if user_choice == "E":
            encrypted = encrypt(user_message, user_shift)
            print(f"Encrypted message: {encrypted}")
        elif user_choice == "D":
            decrypted = decrypt(user_message, user_shift)
            print(f"Decrypted message: {decrypted}")
        else:
            print("Invalid option. Please choose E or D.")
        another = input("Do you want to try again? (Y/N): ").upper()
        if another != 'Y':
            break