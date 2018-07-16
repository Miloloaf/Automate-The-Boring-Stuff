import re

# Strong Password Detection

# TODO: Get a password
# TODO: At least 8 characters long
# TODO: contains upper and lower case characters
# TODO: has at least one digit

lowerRegex = re.compile(r'(.*)?[a-z]+')
upperRegex = re.compile(r'(.*)?[A-Z]+')
numRegex = re.compile(r'(.*)?[0-9]+')

def strongPasswordDetection(password):

    if len(password) < 8:
        return "Password not long enough"

    else:
        if lowerRegex.search(password) is None:
            return "Password must have at least one lower case letter"

        elif upperRegex.search(password) is None:
            return "Password must have at least one upper case letter"

        elif numRegex.search(password) is None:
            return "Password must have at least one digit"

        else:
            print(lowerRegex.search(password))
            print(upperRegex.search(password))
            print(numRegex.search(password))

            return "Password is secure"

password = str(input("Please enter a password: "))

print(strongPasswordDetection(password))
