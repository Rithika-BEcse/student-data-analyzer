import tkinter as tk
from password_strength import check_password_strength

def check_strength():
    pwd = entry.get()
    result = check_password_strength(pwd)
    output_label.config(text=result)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=30, show="*")
entry.pack()

btn = tk.Button(root, text="Check Strength", command=check_strength)
btn.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack(pady=20)

root.mainloop()
