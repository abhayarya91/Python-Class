import re

def is_strong_password(password):
    """
    Check if a password meets basic strength requirements.
    """
    # Minimum length of 8 characters
    if len(password) < 8:
        return False

    # Contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Contains at least one special character
    special_chars_pattern = r"[!@#$%^&*(),.?\":{}|<>]"
    if not re.search(special_chars_pattern, password):
        return False

    return True

# Example usage
password_to_check = "StrongPwd123!"
if is_strong_password(password_to_check):
    print("Password is strong.")
else:
    print("Password is weak. Please choose a stronger one.")
