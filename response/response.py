from validator_collection import validators, checkers, errors

email = input("What's your email adress? ")

try:
    email_address = validators.email(email)
    print("Valid")
except ValueError:
    print("Invalid")
