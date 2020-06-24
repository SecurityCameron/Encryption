
# This basic project is to allow CMD commands to be used within a python script
# to open a file in the terminal input 'TYPE' followed by the text file name in quotes.
# issue with directory change, fix: split location off on last '/' to act as a
# revert to previous directory.
# Any commands used in CMD should work within this script.

import os

def cmd():
    x = 0
    # print current dir and store as 'location'.
    location = os.getcwd()
    while x ==0:
        # allow user input.
        command = input(location+": ")
        os.system(command)
        
        # attempt of dir change.
        if command == "cd ..":
            location = os.chdir("/")
            print("Directory changed")



cmd()