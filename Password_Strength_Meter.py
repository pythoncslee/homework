

def password_strength(pw: str):

    COMMON_PASSWORDS = [
        "password", "123456", "qwerty", "abc123", "letmein",
        "admin", "welcome", "password123", "iloveyou", "monkey"
    ] # a list of common password people like to choose

    length = len(pw)
    is_common = pw.lower() in COMMON_PASSWORDS

    # very simple repetition/predictability check
    #repeated = length >= 6 and (pw == pw[0] * length or pw in ("abcdef", "123456", "qwerty"))

    score = 0 # Initialize the score as 0
    if length >= 8: score += 1 # password with length greater or equal to 8, add 1 score
    if length >= 12: score += 1 # password with length greater or equal to 12, add an additional score
    if any(c.islower() for c in pw): score += 1 # include any lowercase letter, add 1 score
    if any(c.isupper() for c in pw): score += 1 # include any uppercase letter, add 1 score
    if any(c.isdigit() for c in pw): score += 1 # include any numeric value, add 1 score
    if any(not c.isalnum() for c in pw): score += 1 # include any special character other than alphanumeric value, add 1 score
    if is_common: score -= 2 # match wih any common password, minus 2 score

    if score <= 2: label = "very weak" # score less or equal to 2, classify as very weak password
    elif score == 3: label = "weak" # score equal to 3, classify as weak password
    elif score == 4: label = "okay" # score equal to 4, classify as okay password
    elif score == 5: label = "strong" # score equal to 5, classify as strong password
    else: label = "very strong" # score greater than 5, classify as very strong password

    return label

def password_meter():
    password = input("Enter Your Password for accessing its strength: ") # let user to input the password for assessment
    print("Your Password Strength is", password_strength(password))  # compute the score of password and return the strength of password

# Run main if this script is executed
#if __name__ == "__main__":
#    password_meter()