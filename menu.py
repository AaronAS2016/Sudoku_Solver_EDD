
# Module with md5 encrypt
import hashlib
from getpass import getpass
import time
import os

import utils

usernamehash = "10007cc9dedb708c2825f593c2168eac"
passwordhash = "a8878feb49b7c66c6f3780d879882b2b"

os.system('clear')
print("==============================================")
print("          WELCOME TO SODOKU SOLVER           ")
print("Welcome to the result of the TP")
print("Please login...")
print('\n')
username = input("Username: ")
password = getpass("Password: ")
os.system('clear')
print("Logging in....")
time.sleep(3)

if hashlib.md5(username.encode()).hexdigest() == usernamehash and hashlib.md5(password.encode()).hexdigest() == passwordhash:
    print("Logging successfull")
    time.sleep(2)
    os.system('clear')
    print("Loading solver...")
    time.sleep(2)
    # A List of Items
    items = list(range(0, 57))
    l = len(items)

    # Initial call to print 0% progress
    utils.printProgressBar(0, l, prefix='Progress:',
                           suffix='Complete', length=50)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.1)
        # Update Progress Bar
        utils.printProgressBar(i + 1, l, prefix='Progress:',
                               suffix='Complete', length=5)
    os.system('clear')

else:
    print("Logging incorrect... Exit the application")
    exit()
