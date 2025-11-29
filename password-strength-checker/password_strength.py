import tkinter as tk
from tkinter import messagebox
import string

def check_password_strength():
    password = entry.get()
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength <= 2:
        result = "Weak Password"
    elif strength == 3:
        result = "Medium Strength Password"
    else:
        result = "Strong Password"

    messagebox.showinfo("Password Strength", result)

# UI PART
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=25, show="*")
entry.pack(pady=5)

button = tk.Button(root, text="Check Strength", command=check_password_strength)
button.pack(pady=10)

root.mainloop()
