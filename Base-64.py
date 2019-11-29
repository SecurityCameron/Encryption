import base64
import time

#Put the driver name (C:) followed by the directory and you
#can encrypt any file on a PC.

def menu():
    time.sleep(0.5)
    choice = input("\n1. encrypt File\n2. encrypt message\n3. decrypt message\n4. exit\nchoice: ")
    if choice == "1":
        encryptFile()
        
    elif choice == "2":
        encrypt()
    
        
    elif choice == "3":
        decryptMessage()
        
    elif choice == "4":
        exit()
        
    
        
    else:
        print ("Not a valid choice.")
        

def encryptFile():
    myFile = input("enter file to encrypt: ")
    file = open(myFile,"r")
    contents = file.read()
    contents = contents.encode()
    file = open(myFile, "w")
    encoded = base64.b64encode(contents)
    # the .decode() converts the bytes to str, taking off the b'...'
    file.write(str(encoded))
    print ("File is now encrypted... and the contents is unreadable")



def decryptMessage():
    pwd = "N3VIQUJmZ2pyNDVkZDRvMzNkZmd0NzBkZzlLOWRmcjJ0NWhCdmRm"
    key = base64.b64decode(pwd) #the decoded version of this is the key.
    value = input("Enter the decryption key: ").encode()
    if value == key:
        time.sleep(1)
        message = input("Enter the message to decode: ")
        decoded = base64.b64decode(message)
        print (decoded)
        menu()
        
    else:
        print("Decryption key is wrong.")
        menu()


def encrypt():
    password = input("Enter a message: ").encode()
    encoded = base64.b64encode(password)
    print (encoded.decode()) 
    menu()


menu() 
    
