import random
import time
#Get the chars to use in the password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNIOPQRSTUVWXYZ1234567890!@#$%^&*()_+=,./;"
#Open the file outside of the loop


while 1:
    passsword_len = int(input("What Length would you like the paassword to be : "))
    password_units = int(input("How many password would you like to create : "))
    password_count = password_units + 1
    for x in range(0,password_units):
        password = ""
        password_count -=1
        password_name = input("What is this password for ?: ")
        for x in range(0,passsword_len):
            password_char = random.choice(chars)
            password = password + password_char
        saved_passwordfile = open("savedpasswords.txt", "a")
        saved_passwordfile.write("\n %s : %s " % (password_name, password))
        saved_passwordfile.close()        

