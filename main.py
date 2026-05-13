from caesar import *

message = "HELLO WORLD"

shift = 3

encrypted = caesar_encrypt(message, shift)

print("Encrypted Message:", encrypted)

decrypted = caesar_decrypt(encrypted, shift)

print("Decrypted Message:", decrypted)

from affine import *

message = "HELLO"

a = 5
b = 8

encrypted = affine_encrypt(message, a, b)

print("Encrypted Message:", encrypted)

decrypted = affine_decrypt(encrypted, a, b)

print("Decrypted Message:", decrypted)

from playfair import *

message = "HELLO"

key = "SECURITY"

encrypted = playfair_encrypt(message, key)

print("Encrypted Message:", encrypted)

decrypted = playfair_decrypt(encrypted, key)

print("Decrypted Message:", decrypted)

from caesar import *
from affine import *
from playfair import *


print("===============================")
print(" MULTI CIPHER ENCRYPTION SYSTEM")
print("===============================")

print("\nChoose Cipher Technique")
print("1. Caesar Cipher")
print("2. Affine Cipher")
print("3. Playfair Cipher")
print("4. Multi Cipher (All Three)")

choice = input("\nEnter your choice: ")

message = input("Enter Message: ")


# -----------------------------------
# CAESAR CIPHER
# -----------------------------------

if choice == '1':

    shift = int(input("Enter Shift Key: "))

    encrypted = caesar_encrypt(message, shift)

    print("\nEncrypted Message:", encrypted)
    decrypted = caesar_decrypt(encrypted, shift)

    print("Decrypted Message:", decrypted)


# -----------------------------------
# AFFINE CIPHER
# -----------------------------------

elif choice == '2':

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    encrypted = affine_encrypt(message, a, b)

    print("\nEncrypted Message:", encrypted)

    decrypted = affine_decrypt(encrypted, a, b)

    print("Decrypted Message:", decrypted)

# -----------------------------------
# PLAYFAIR CIPHER
# -----------------------------------

elif choice == '3':

    key = input("Enter Playfair Keyword: ")

    encrypted = playfair_encrypt(message, key)

    print("\nEncrypted Message:", encrypted)

    decrypted = playfair_decrypt(encrypted, key)

    print("Decrypted Message:", decrypted)
    print("\n----- MULTI CIPHER DECRYPTION -----")

    final_cipher = playfair_encrypt(affine_encrypt(caesar_encrypt(message, 3), 5, 8), key)
    
    decrypt1 = playfair_decrypt(final_cipher, key)
    print("After Playfair Decryption:", decrypt1)

    decrypt2 = affine_decrypt(decrypt1, a, b)
    print("After Affine Decryption:", decrypt2)

    original = caesar_decrypt(decrypt2, shift)
    print("Original Message:", original)

    # -----------------------------------
# INVALID OPTION
# -----------------------------------

else:
 print("Invalid Choice")


