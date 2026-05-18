import customtkinter as ctk
from tkinter import messagebox, Text, Toplevel
from caesar import *
from affine import *
from playfair import *
import time

# ============================================
# WELCOME PAGE
# ============================================
def show_welcome():
    welcome_window = Toplevel(app)
    welcome_window.title("Welcome - Multi Cipher Encryption System")
    welcome_window.resizable(True, True)
    
    # Set to zoomed (fullscreen)
    try:
        welcome_window.state("zoomed")
    except:
        welcome_window.geometry("1600x900")
    
    # Configure grid
    welcome_window.grid_rowconfigure(0, weight=1)
    welcome_window.grid_columnconfigure(0, weight=1)
    
    # Main background frame
    main_bg = ctk.CTkFrame(welcome_window, fg_color="#0a0e27")
    main_bg.grid(row=0, column=0, sticky="nsew")
    main_bg.grid_rowconfigure(0, weight=1)
    main_bg.grid_columnconfigure(0, weight=1)
    
    # Content container
    content_container = ctk.CTkFrame(main_bg, fg_color="#0a0e27")
    content_container.pack(fill="both", expand=True)
    
    # Left panel - Dark with branding
    left_panel = ctk.CTkFrame(content_container, fg_color="#1a1f3a")
    left_panel.pack(side="left", fill="both", expand=True, padx=0, pady=0)
    
    # Left content with padding
    left_content = ctk.CTkFrame(left_panel, fg_color="#1a1f3a")
    left_content.pack(fill="both", expand=True, padx=60, pady=60)
    
    # Logo/Icon area
    logo_label = ctk.CTkLabel(
        left_content,
        text="🔐",
        font=("Helvetica", 100),
        text_color="#00d9ff"
    )
    logo_label.pack(pady=(0, 30))
    
    # Main title
    title = ctk.CTkLabel(
        left_content,
        text="Multi Cipher",
        font=("Helvetica", 80, "bold"),
        text_color="#00d9ff"
    )
    title.pack(pady=(0, 5))
    
    # Subtitle
    subtitle = ctk.CTkLabel(
        left_content,
        text="Encryption System",
        font=("Helvetica", 36, "bold"),
        text_color="#FFFFFF"
    )
    subtitle.pack(pady=(0, 30))
    
    # Tagline
    tagline = ctk.CTkLabel(
        left_content,
        text="Secure your messages with military-grade encryption",
        font=("Helvetica", 15),
        text_color="#b0b8d4"
    )
    tagline.pack(pady=(0, 40))
    
    # Features list
    features_title = ctk.CTkLabel(
        left_content,
        text="Key Features",
        font=("Helvetica", 20, "bold"),
        text_color="#00d9ff"
    )
    features_title.pack(anchor="w", pady=(20, 15))
    
    features = [
        ("✓ Caesar Cipher", "Classic shift-based encryption"),
        ("✓ Affine Cipher", "Mathematical encryption"),
        ("✓ Playfair Cipher", "Digraph-based encryption"),
        ("✓ Multi Cipher", "Combined triple encryption")
    ]
    
    for feature_name, feature_desc in features:
        feature_frame = ctk.CTkFrame(left_content, fg_color="transparent")
        feature_frame.pack(anchor="w", pady=8)
        
        feature_label = ctk.CTkLabel(
            feature_frame,
            text=feature_name,
            font=("Helvetica", 14, "bold"),
            text_color="#00d9ff"
        )
        feature_label.pack(anchor="w")
        
        feature_desc_label = ctk.CTkLabel(
            feature_frame,
            text=f"  {feature_desc}",
            font=("Helvetica", 12),
            text_color="#8b92b8"
        )
        feature_desc_label.pack(anchor="w", padx=(10, 0))
    
    # Right panel - Modern gradient look
    right_panel = ctk.CTkFrame(content_container, fg_color="#0f1729")
    right_panel.pack(side="right", fill="both", expand=True, padx=0, pady=0)
    
    # Right content
    right_content = ctk.CTkFrame(right_panel, fg_color="#0f1729")
    right_content.pack(fill="both", expand=True, padx=50, pady=60)
    
    # Welcome card
    welcome_card = ctk.CTkFrame(right_content, fg_color="#1a2547", corner_radius=15)
    welcome_card.pack(fill="both", expand=True, pady=20)
    
    welcome_inner = ctk.CTkFrame(welcome_card, fg_color="#1a2547")
    welcome_inner.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Welcome heading
    welcome_heading = ctk.CTkLabel(
        welcome_inner,
        text="Welcome!",
        font=("Helvetica", 48, "bold"),
        text_color="#FFFFFF"
    )
    welcome_heading.pack(pady=(0, 15))
    
    # Welcome message
    welcome_msg = ctk.CTkLabel(
        welcome_inner,
        text="Experience the power of advanced encryption technology. "
             "Choose from multiple cipher algorithms to protect your sensitive data. "
             "Our intuitive interface makes encryption simple and secure.",
        font=("Helvetica", 13),
        text_color="#c7cfe8",
        justify="left",
        wraplength=350
    )
    welcome_msg.pack(pady=15)
    
    # Statistics
    stats_title = ctk.CTkLabel(
        welcome_inner,
        text="Why Choose Us?",
        font=("Helvetica", 16, "bold"),
        text_color="#00d9ff"
    )
    stats_title.pack(anchor="w", pady=(20, 10))
    
    stats_frame = ctk.CTkFrame(welcome_inner, fg_color="#0f1729", corner_radius=10)
    stats_frame.pack(fill="x", pady=10)
    
    stat_items = [
        ("Fast", "Lightning-quick encryption"),
        ("Secure", "Military-grade algorithms"),
        ("Easy", "User-friendly interface")
    ]
    
    for stat_name, stat_desc in stat_items:
        stat_item = ctk.CTkFrame(stats_frame, fg_color="transparent")
        stat_item.pack(anchor="w", padx=15, pady=8)
        
        stat_label = ctk.CTkLabel(
            stat_item,
            text=f"• {stat_name}",
            font=("Helvetica", 13, "bold"),
            text_color="#00d9ff"
        )
        stat_label.pack(anchor="w")
        
        stat_desc_label = ctk.CTkLabel(
            stat_item,
            text=f"  {stat_desc}",
            font=("Helvetica", 11),
            text_color="#8b92b8"
        )
        stat_desc_label.pack(anchor="w")
    
    # Button section
    button_frame = ctk.CTkFrame(welcome_inner, fg_color="transparent")
    button_frame.pack(fill="x", pady=(30, 0))
    
    def on_get_started():
        welcome_window.withdraw()
        app.deiconify()
        try:
            app.state("zoomed")
        except:
            app.geometry("1600x900")
    
    # Get Started button
    get_started_btn = ctk.CTkButton(
        button_frame,
        text="Get Started →",
        command=on_get_started,
        width=280,
        height=60,
        font=("Helvetica", 18, "bold"),
        fg_color="#00d9ff",
        hover_color="#00b8cc",
        text_color="#0a0e27",
        corner_radius=10
    )
    get_started_btn.pack(pady=10)
    
    # Footer note
    footer = ctk.CTkLabel(
        welcome_inner,
        text="Click 'Get Started' to begin encrypting your messages",
        font=("Helvetica", 11),
        text_color="#6b7390"
    )
    footer.pack(pady=(10, 0))

# Set appearance mode
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main window (create but hide it initially)
app = ctk.CTk()
app.title("Multi Cipher Encryption System - Secure Messaging")
app.resizable(True, True)
app.withdraw()  # Hide the main window initially
try:
    app.state("zoomed")
except:
    app.geometry("1600x900")

# Configure grid
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# Main frame with background
main_frame = ctk.CTkFrame(app, fg_color="#0f1419")
main_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
main_frame.grid_rowconfigure(8, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# ============================================
# HEADER WITH BACK BUTTON
# ============================================
header_frame = ctk.CTkFrame(main_frame, fg_color="#1a2138", corner_radius=0)
header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=0, pady=0)

# Back button on top left
back_btn_header = ctk.CTkButton(
    header_frame,
    text="←",
    width=40,
    height=40,
    font=("Helvetica", 20, "bold"),
    fg_color="#00d9ff",
    hover_color="#00b8cc",
    text_color="#0a0e27",
    corner_radius=8
)
back_btn_header.pack(side="left", padx=15, pady=10)

# Header title and content
header_content = ctk.CTkFrame(header_frame, fg_color="transparent")
header_content.pack(side="left", fill="both", expand=True, padx=20, pady=10)

header_label = ctk.CTkLabel(
    header_content,
    text="🔐 Multi Cipher Encryption System",
    font=("Helvetica", 32, "bold"),
    text_color="#00d9ff"
)
header_label.pack(anchor="w")

header_subtext = ctk.CTkLabel(
    header_content,
    text="Advanced Encryption with Multiple Cipher Algorithms",
    font=("Helvetica", 11),
    text_color="#a0a8c0"
)
header_subtext.pack(anchor="w")

# ============================================
# CIPHER SELECTION & KEYS - COMPACT LAYOUT
# ============================================
control_frame = ctk.CTkFrame(main_frame, fg_color="#1a2138", corner_radius=10)
control_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=15, pady=15)

# Row 1: Cipher Selection
cipher_label = ctk.CTkLabel(control_frame, text="Select Cipher:", font=("Helvetica", 13, "bold"), text_color="#00d9ff")
cipher_label.grid(row=0, column=0, padx=15, pady=12, sticky="w")

cipher_choice = ctk.CTkComboBox(
    control_frame,
    values=["Caesar Cipher", "Affine Cipher", "Playfair Cipher", "Multi Cipher"],
    state="readonly",
    width=200,
    font=("Helvetica", 11),
    button_color="#00d9ff",
    dropdown_fg_color="#1a2138"
)
cipher_choice.set("")
cipher_choice.grid(row=0, column=1, padx=10, pady=12, sticky="w")

# Row 1: Keys
key1_label = ctk.CTkLabel(control_frame, text="Key 1:", font=("Helvetica", 13, "bold"), text_color="#00d9ff")
key1_label.grid(row=0, column=2, padx=15, pady=12, sticky="w")

key1_entry = ctk.CTkEntry(control_frame, placeholder_text="Select a cipher first", width=140, font=("Helvetica", 11))
key1_entry.grid(row=0, column=3, padx=10, pady=12, sticky="w")

key2_label = ctk.CTkLabel(control_frame, text="Key 2:", font=("Helvetica", 13, "bold"), text_color="#00d9ff")
key2_label.grid(row=0, column=4, padx=15, pady=12, sticky="w")

key2_entry = ctk.CTkEntry(control_frame, placeholder_text="Select a cipher first", width=140, font=("Helvetica", 11))
key2_entry.grid(row=0, column=5, padx=10, pady=12, sticky="w")

# ============================================
# INPUT TEXT
# ============================================
input_label = ctk.CTkLabel(main_frame, text="📝 Input Message:", font=("Helvetica", 14, "bold"), text_color="#00d9ff")
input_label.grid(row=2, column=0, columnspan=2, sticky="w", pady=(15, 5), padx=15)

input_text = Text(main_frame, height=7, width=100, bg="#0a0e27", fg="#FFFFFF", font=("Courier", 12), insertbackground="#00d9ff", relief="flat", bd=0)
input_text.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5, padx=15, ipady=8)

# Scrollbar for input
input_scrollbar = ctk.CTkScrollbar(main_frame, command=input_text.yview)
input_scrollbar.grid(row=3, column=2, sticky="ns", padx=(0, 15))
input_text.config(yscrollcommand=input_scrollbar.set)

# ============================================
# OUTPUT TEXT
# ============================================
output_label = ctk.CTkLabel(main_frame, text="🔒 Output Message:", font=("Helvetica", 14, "bold"), text_color="#00d9ff")
output_label.grid(row=4, column=0, columnspan=2, sticky="w", pady=(15, 5), padx=15)

output_text = Text(main_frame, height=9, width=100, bg="#0a0e27", fg="#FFFFFF", font=("Courier", 12), insertbackground="#00d9ff", relief="flat", bd=0)
output_text.grid(row=5, column=0, columnspan=2, sticky="ew", pady=5, padx=15, ipady=8)

# Scrollbar for output
output_scrollbar = ctk.CTkScrollbar(main_frame, command=output_text.yview)
output_scrollbar.grid(row=5, column=2, sticky="ns", padx=(0, 15))
output_text.config(yscrollcommand=output_scrollbar.set)

# Configure text tags for styling
output_text.tag_configure("multi_cipher", foreground="#00d9ff")  # Cyan color for Multi Cipher
output_text.tag_configure("multi_cipher_header", foreground="#00ff88", font=("Courier", 12, "bold"))  # Light green for headers

# ============================================
# FUNCTIONS
# ============================================

def update_placeholder_text(*args):
    """Update placeholder text based on selected cipher"""
    cipher = cipher_choice.get()
    
    if cipher == "":
        key1_entry.configure(placeholder_text="Select a cipher first")
        key2_entry.configure(placeholder_text="Select a cipher first")
    elif cipher == "Caesar Cipher":
        key1_entry.configure(placeholder_text="Shift value")
        key2_entry.configure(placeholder_text="(Not used)")
    elif cipher == "Affine Cipher":
        key1_entry.configure(placeholder_text="A value")
        key2_entry.configure(placeholder_text="(affine cipher)")
    elif cipher == "Playfair Cipher":
        key1_entry.configure(placeholder_text="Keyword")
        key2_entry.configure(placeholder_text="(Not used)")
    elif cipher == "Multi Cipher":
        key1_entry.configure(placeholder_text="(Auto)")
        key2_entry.configure(placeholder_text="(Auto)")

# Bind cipher selection to placeholder update
cipher_choice.configure(command=update_placeholder_text)

def encrypt_message():
    cipher = cipher_choice.get()
    message = input_text.get("1.0", "end").strip()
    
    if cipher == "":
        messagebox.showerror("Error", "Please select a cipher type")
        return
    
    if message == "":
        messagebox.showerror("Error", "Please enter message")
        return
    
    output_text.delete("1.0", "end")
    
    try:
        if cipher == "Caesar Cipher":
            shift = int(key1_entry.get())
            encrypted = caesar_encrypt(message, shift)
            output_text.insert("end", "Encrypted Message:\n")
            output_text.insert("end", encrypted)
        
        elif cipher == "Affine Cipher":
            a = int(key1_entry.get())
            b = int(key2_entry.get())
            encrypted = affine_encrypt(message, a, b)
            output_text.insert("end", "Encrypted Message:\n")
            output_text.insert("end", encrypted)
        
        elif cipher == "Playfair Cipher":
            keyword = key1_entry.get()
            encrypted = playfair_encrypt(message, keyword)
            output_text.insert("end", "Encrypted Message:\n")
            output_text.insert("end", encrypted)
        
        elif cipher == "Multi Cipher":
            shift = 3
            a = 5
            b = 8
            keyword = "SECURITY"
            
            step1 = caesar_encrypt(message, shift)
            step2 = affine_encrypt(step1, a, b)
            final_cipher = playfair_encrypt(step2, keyword)
            
            output_text.insert("end", "After Caesar Cipher:\n", "multi_cipher_header")
            output_text.insert("end", step1 + "\n\n", "multi_cipher")
            output_text.insert("end", "After Affine Cipher:\n", "multi_cipher_header")
            output_text.insert("end", step2 + "\n\n", "multi_cipher")
            output_text.insert("end", "Final Encrypted Message:\n", "multi_cipher_header")
            output_text.insert("end", final_cipher, "multi_cipher")
    
    except ValueError:
        messagebox.showerror("Error", "Invalid key format. Please enter valid numbers.")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {str(e)}")


def decrypt_message():
    cipher = cipher_choice.get()
    message = input_text.get("1.0", "end").strip()
    
    if cipher == "":
        messagebox.showerror("Error", "Please select a cipher type")
        return
    
    if message == "":
        messagebox.showerror("Error", "Please enter message")
        return
    
    output_text.delete("1.0", "end")
    
    try:
        if cipher == "Caesar Cipher":
            shift = int(key1_entry.get())
            decrypted = caesar_decrypt(message, shift)
            output_text.insert("end", "Decrypted Message:\n")
            output_text.insert("end", decrypted)
        
        elif cipher == "Affine Cipher":
            a = int(key1_entry.get())
            b = int(key2_entry.get())
            decrypted = affine_decrypt(message, a, b)
            output_text.insert("end", "Decrypted Message:\n")
            output_text.insert("end", decrypted)
        
        elif cipher == "Playfair Cipher":
            keyword = key1_entry.get()
            decrypted = playfair_decrypt(message, keyword)
            output_text.insert("end", "Decrypted Message:\n")
            output_text.insert("end", decrypted)
        
        elif cipher == "Multi Cipher":
            messagebox.showinfo("Info", "Multi Cipher decryption requires manual steps in reverse order.")
    
    except ValueError:
        messagebox.showerror("Error", "Invalid key format. Please enter valid numbers.")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {str(e)}")


def clear_all():
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")
    key1_entry.delete(0, "end")
    key2_entry.delete(0, "end")


def go_back_to_welcome():
    """Hide main window and show welcome window again"""
    try:
        app.withdraw()
        show_welcome()
    except:
        pass


# ============================================
# BUTTONS
# ============================================
button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
button_frame.grid(row=6, column=0, columnspan=2, pady=20)

encrypt_btn = ctk.CTkButton(
    button_frame,
    text="🔐 Encrypt",
    command=encrypt_message,
    width=160,
    height=45,
    font=("Helvetica", 13, "bold"),
    fg_color="#00d9ff",
    hover_color="#00b8cc",
    text_color="#0a0e27",
    corner_radius=8
)
encrypt_btn.pack(side="left", padx=10)

decrypt_btn = ctk.CTkButton(
    button_frame,
    text="🔓 Decrypt",
    command=decrypt_message,
    width=160,
    height=45,
    font=("Helvetica", 13, "bold"),
    fg_color="#ff6b6b",
    hover_color="#ff5252",
    text_color="#FFFFFF",
    corner_radius=8
)
decrypt_btn.pack(side="left", padx=10)

clear_btn = ctk.CTkButton(
    button_frame,
    text="🗑️ Clear",
    command=clear_all,
    width=160,
    height=45,
    font=("Helvetica", 13, "bold"),
    fg_color="#ffa500",
    hover_color="#ff8c00",
    text_color="#FFFFFF",
    corner_radius=8
)
clear_btn.pack(side="left", padx=10)

# Run the app
back_btn_header.configure(command=go_back_to_welcome)
show_welcome()
try:
    app.mainloop()
except Exception as e:
    print(f"Note: {e}")
    pass
