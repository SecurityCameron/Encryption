#finding a file in a directory.
import os
import time


#----
def finding():
    
    dir1 = input("enter exact path of directory you\nwant to search: ")
    file_search = input("enter file name to search for: ")
    entries = os.listdir(dir1)

    for item in entries:
        if item == file_search:
        
            print (file_search,"is in the directory")
            time.sleep(0.5)
            return

    else:
        print ("File is not found in", dir1)
#----

finding()




