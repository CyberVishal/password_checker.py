import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength == 4:
        return " Strong Password"
    elif strength == 3:
        return " Medium Strength"
    else:
        return "⚠ Weak Password"

if __name__ == "__main__":
    print(check_password_strength("Hello@123"))
