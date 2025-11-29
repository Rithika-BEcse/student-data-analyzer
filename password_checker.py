import re

def check_password_strength(password):
    strength = 0

    # Conditions
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1

    # Decision
    if strength == 5:
        return "Very Strong Password 💪"
    elif strength == 4:
        return "Strong Password 👍"
    elif strength == 3:
        return "Moderate Password 🙂"
    else:
        return "Weak Password ❌"

# Demo
user_password = input("Enter your password: ")
print(check_password_strength(user_password))
