from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from caesar import *
from affine import *
from playfair import *

# --------------------------------------
# MAIN WINDOW
# --------------------------------------

window = Tk()

window.title("Multi Cipher Encryption System")
window.geometry("800x650")
window.config(bg="#1e1e1e")


# --------------------------------------
# FUNCTIONS
# --------------------------------------


def encrypt_message():

    cipher = cipher_choice.get()

    message = input_text.get("1.0", END).strip()

    if message == "":
        messagebox.showerror("Error", "Please enter message")
        return

    output_text.delete("1.0", END)
     # ----------------------------------
    # CAESAR CIPHER
    # ----------------------------------

    if cipher == "Caesar Cipher":

        shift = int(key1_entry.get())

        encrypted = caesar_encrypt(message, shift)

        output_text.insert(END, "Encrypted Message:\n")
        output_text.insert(END, encrypted)
        # ----------------------------------
    # AFFINE CIPHER
    # ----------------------------------

    elif cipher == "Affine Cipher":

        a = int(key1_entry.get())
        b = int(key2_entry.get())

        encrypted = affine_encrypt(message, a, b)

        output_text.insert(END, "Encrypted Message:\n")
        output_text.insert(END, encrypted)


    # ----------------------------------
    # PLAYFAIR CIPHER
    # ----------------------------------

    elif cipher == "Playfair Cipher":

        keyword = key1_entry.get()
        encrypted = playfair_encrypt(message, keyword)

        output_text.insert(END, "Encrypted Message:\n")
        output_text.insert(END, encrypted)
 # ----------------------------------
    # MULTI CIPHER
    # ----------------------------------

    elif cipher == "Multi Cipher":

        shift = 3
        a = 5
        b = 8
        keyword = "SECURITY"

        step1 = caesar_encrypt(message, shift)
        step2 = affine_encrypt(step1, a, b)
        final_cipher = playfair_encrypt(step2, keyword)

        output_text.insert(END, "After Caesar Cipher:\n")
        output_text.insert(END, step1 + "\n\n")

        output_text.insert(END, "After Affine Cipher:\n")
        output_text.insert(END, step2 + "\n\n")

        output_text.insert(END, "Final Encrypted Message:\n")
        output_text.insert(END, final_cipher)
        # --------------------------------------
# DECRYPT FUNCTION
# --------------------------------------


def decrypt_message():

    cipher = cipher_choice.get()

    message = input_text.get("1.0", END).strip()

    if message == "":
        messagebox.showerror("Error", "Please enter message")
        return

    output_text.delete("1.0", END)

# ----------------------------------
    # CAESAR DECRYPT
    # ----------------------------------

    if cipher == "Caesar Cipher":

        shift = int(key1_entry.get())

        decrypted = caesar_decrypt(message, shift)

        output_text.insert(END, "Decrypted Message:\n")
        output_text.insert(END, decrypted)

         # ----------------------------------
    # PLAYFAIR DECRYPT
    # ----------------------------------

    elif cipher == "Playfair Cipher":

        keyword = key1_entry.get()

        decrypted = playfair_decrypt(message, keyword)

        output_text.insert(END, "Decrypted Message:\n")
        output_text.insert(END, decrypted)


    # ----------------------------------
    # AFFINE DECRYPT
    # ----------------------------------

    elif cipher == "Affine Cipher":

        a = int(key1_entry.get())
        b = int(key2_entry.get())

        decrypted = affine_decrypt(message, a, b)

        output_text.insert(END, "Decrypted Message:\n")
        output_text.insert(END, decrypted)

    # ----------------------------------
    # MULTI CIPHER DECRYPT
    # ----------------------------------

    elif cipher == "Multi Cipher":

        shift = 3
        a = 5
        b = 8
        keyword = "SECURITY"

        step1 = playfair_decrypt(message, keyword)
        step2 = affine_decrypt(step1, a, b)
        original = caesar_decrypt(step2, shift)

        output_text.insert(END, "After Playfair Decryption:\n")
        output_text.insert(END, step1 + "\n\n")

        output_text.insert(END, "After Affine Decryption:\n")
        output_text.insert(END, step2 + "\n\n")

        output_text.insert(END, "Original Message:\n")
        output_text.insert(END, original)

        # --------------------------------------
# CLEAR FUNCTION
# --------------------------------------


def clear_all():

    input_text.delete("1.0", END)
    output_text.delete("1.0", END)

    key1_entry.delete(0, END)
    key2_entry.delete(0, END)


# --------------------------------------
# TITLE
# --------------------------------------


heading = Label(
    window,
    text="MULTI CIPHER ENCRYPTION SYSTEM",
    font=("Arial", 22, "bold"),
        bg="#1e1e1e",
    fg="white"
)

heading.pack(pady=20)


# --------------------------------------
# CIPHER SELECTION
# --------------------------------------


cipher_label = Label(
    window,
    text="Select Cipher:",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
)

cipher_label.pack()


cipher_choice = ttk.Combobox(
    window,
    values=[
        "Caesar Cipher",
        "Affine Cipher",
        "Playfair Cipher",
        "Multi Cipher"
    ],
    font=("Arial", 12),
    width=30
)

cipher_choice.pack(pady=10)
cipher_choice.current(0)

# --------------------------------------
# INPUT MESSAGE
# --------------------------------------


input_label = Label(
    window,
    text="Enter Message:",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
)

input_label.pack()


input_text = Text(
    window,
    height=5,
    width=70,
    font=("Arial", 12)
)
input_text.pack(pady=10)


# --------------------------------------
# KEYS
# --------------------------------------


key1_label = Label(
    window,
    text="Key 1 / Shift / Keyword:",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

key1_label.pack()


key1_entry = Entry(
    window,
    width=30,
    font=("Arial", 12)
)
key1_entry.pack(pady=5)


key2_label = Label(
    window,
    text="Key 2 (Affine b value):",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

key2_label.pack()


key2_entry = Entry(
    window,
    width=30,
    font=("Arial", 12)
)

key2_entry.pack(pady=5)

# --------------------------------------
# BUTTONS
# --------------------------------------

button_frame = Frame(window, bg="#1e1e1e")
button_frame.pack(pady=20)

encrypt_button = Button(
    button_frame,
    text="Encrypt",
    font=("Arial", 12, "bold"),
    width=15,
    command=encrypt_message
)

encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = Button(
    button_frame,
    text="Decrypt",
    font=("Arial", 12, "bold"),
    width=15,
    command=decrypt_message
)

decrypt_button.grid(row=0, column=1, padx=10)

clear_button = Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    width=15,
    command=clear_all
)

clear_button.grid(row=0, column=2, padx=10)


# --------------------------------------
# OUTPUT
# --------------------------------------


output_label = Label(
    window,
    text="Output:",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
)

output_label.pack()


output_text = Text(
     window,
    height=10,
    width=70,
    font=("Arial", 12)
)

output_text.pack(pady=10)
# --------------------------------------
# RUN WINDOW
# --------------------------------------


window.mainloop()

