import secrets
import string

#defining constants
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

pwd_length = 12

#function to generate password
def generate_password(length=pwd_length):
    pwd = ''
    for i in range(length):
        pwd += ''.join(secrets.choice(alphabet)) 
    return pwd

#main function
if __name__ == "__main__":
    print("Generated Password: ", generate_password())
