import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Criteria checks
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Assign points
    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    if upper_criteria:
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")
        
    if lower_criteria:
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")
        
    if digit_criteria:
        strength += 1
    else:
        feedback.append("Include at least one number.")
        
    if special_criteria:
        strength += 1
    else:
        feedback.append("Include at least one special character (e.g., !, @, #, $).")

    # Strength assessment
    strength_levels = {
        5: "Very Strong 💪",
        4: "Strong ✅",
        3: "Moderate ⚠️",
        2: "Weak ❌",
        1: "Very Weak 🔓",
        0: "Extremely Weak 🚫"
    }

    return {
        "password": password,
        "score": strength,
        "strength": strength_levels[strength],
        "feedback": feedback
    }

# Example usage
if __name__ == "__main__":
    pwd = input("Enter a password to check its strength: ")
    result = assess_password_strength(pwd)
    
    print(f"\nPassword Strength: {result['strength']}")
    if result["feedback"]:
        print("Suggestions to improve your password:")
        for f in result["feedback"]:
            print(f"- {f}")
