#This is the Easy way to write to file

#Add to the file
saved_passwordfile = open("savedpasswords.txt", "a")
saved_passwordfile.write("\n This is the new Password")
saved_passwordfile.close()

#Read and Print from the file
saved_passwordfile = open("savedpasswords.txt", "r")
print(saved_passwordfile.read())
saved_passwordfile.close()