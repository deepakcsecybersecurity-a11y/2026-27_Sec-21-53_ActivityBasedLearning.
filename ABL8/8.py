#8. Password Policy Validation Engine (PDF Task 29)
password = input("Enter a sample password: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:
    if ch >= "A" and ch <= "Z":
        has_upper = True
    if ch >= "a" and ch <= "z":
        has_lower = True
    if ch >= "0" and ch <= "9":
        has_digit = True

valid = True

if len(password) < 8:
    print("Failed: password must have at least 8 characters.")
    valid = False
if not has_upper:
    print("Failed: add an uppercase letter.")
    valid = False
if not has_lower:
    print("Failed: add a lowercase letter.")
    valid = False
if not has_digit:
    print("Failed: add a number.")
    valid = False

if valid:
    print("Password meets the example rules.")
else:
    print("Password does not meet the example rules.")
