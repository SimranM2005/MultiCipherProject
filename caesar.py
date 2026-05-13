def caesar_encrypt(text, shift):
    result = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            encrypted_char = chr(
                (ord(char) - start + shift) % 26 + start
            )

            result += encrypted_char

        else:
            result += char

    return result


def caesar_decrypt(text, shift):

    return caesar_encrypt(text, -shift)

def caesar_encrypt(text, shift):

    result = ""

    for char in text:

        # UPPERCASE LETTERS
        if char.isupper():

            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        # LOWERCASE LETTERS
        elif char.islower():

            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        # NUMBERS
        elif char.isdigit():

            result += chr((ord(char) - ord('0') + shift) % 10 + ord('0'))

        else:
            result += char

    return result


def caesar_decrypt(text, shift):

    return caesar_encrypt(text, -shift)