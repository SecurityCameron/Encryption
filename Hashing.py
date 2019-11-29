import hashlib

running_state = True

def hashing(password):
    hash1 = hashlib.md5(str.encode(password)).hexdigest()
    print ("your hashed password is:", hash1,"\n")
    


def main():
    password = input("enter a password: ")
    hashing(password)


while running_state == True:
    main()