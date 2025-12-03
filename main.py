import secrets
import string

#defining constants
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

pwd_length = 12

#function to generate password
def generatePassword(length=pwd_length):
    pwd = ''
    for i in range(length):
        pwd += ''.join(secrets.choice(alphabet)) 
    return pwd

def generatePasswordConstraints():
    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
        if ( any(special_char in special_chars for special_char in pwd) and
            sum(char in digits for char in pwd) >= 2):
            break
    return pwd

#main function
if __name__ == "__main__":
    print("Generated Password: ", generatePassword())
    print("Generated Password with Constraints: ", generatePasswordConstraints())