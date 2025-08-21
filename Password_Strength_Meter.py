

def password_strength(pw: str):

    COMMON_PASSWORDS = [
        "password", "123456", "qwerty", "abc123", "letmein",
        "admin", "welcome", "password123", "iloveyou", "monkey"
    ]

    length = len(pw)
    is_common = pw.lower() in COMMON_PASSWORDS

    # very simple repetition/predictability check
    #repeated = length >= 6 and (pw == pw[0] * length or pw in ("abcdef", "123456", "qwerty"))

    score = 0
    if length >= 8: score += 1
    if length >= 12: score += 1
    if any(c.islower() for c in pw): score += 1
    if any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(not c.isalnum() for c in pw): score += 1
    if is_common: score -= 2
    #if repeated: score -= 1

    if score <= 2: label = "very weak"
    elif score == 3: label = "weak"
    elif score == 4: label = "okay"
    elif score == 5: label = "strong"
    else: label = "very strong"

    return label

def password_meter():
    password = input("Enter Your Password for Assessment: ")
    #password_strength(password)
    print("Your Password Strength is", password_strength(password))

# Run main if this script is executed
#if __name__ == "__main__":
#    password_meter()