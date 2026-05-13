def mod_inverse(a, m):

    for x in range(1, m):

        if (a * x) % m == 1:
            return x

    return None


def affine_encrypt(text, a, b):

    result = ""

    for char in text.upper():

        if char.isalpha():

            x = ord(char) - ord('A')

            encrypted = (a * x + b) % 26

            result += chr(encrypted + ord('A'))

        else:
            result += char

    return result


def affine_decrypt(text, a, b):

    result = ""

    a_inverse = mod_inverse(a, 26)

    if a_inverse is None:
        return "Invalid Key"

    for char in text.upper():

        if char.isalpha():

            y = ord(char) - ord('A')

            decrypted = (a_inverse * (y - b)) % 26

            result += chr(decrypted + ord('A'))

        else:
            result += char

    return result

def affine_encrypt(text, a, b):

    result = ""

    for char in text:

        # LETTERS
        if char.isalpha():

            x = ord(char.upper()) - ord('A')

            encrypted = (a * x + b) % 26

            result += chr(encrypted + ord('A'))

        # DIGITS
        elif char.isdigit():

            x = ord(char) - ord('0')

            encrypted = (a * x + b) % 10

            result += str(encrypted)

        else:
            result += char

    return result

def affine_decrypt(text, a, b):

    result = ""

    a_inverse = mod_inverse(a, 26)

    if a_inverse is None:
        return "Invalid Key"

    for char in text:

        # LETTERS
        if char.isalpha():

            y = ord(char.upper()) - ord('A')

            decrypted = (a_inverse * (y - b)) % 26

            result += chr(decrypted + ord('A'))

        # DIGITS
        elif char.isdigit():

            y = ord(char) - ord('0')

            # inverse for mod 10
            digit_inverse = None

            for i in range(10):
                if (a * i) % 10 == 1:
                    digit_inverse = i
                    break

            if digit_inverse is not None:
                decrypted = (digit_inverse * (y - b)) % 10
                result += str(decrypted)

        else:
            result += char

    return result