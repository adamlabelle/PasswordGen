from tkinter import *
import random, time, os

#Get the chars to use in the password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNIOPQRSTUVWXYZ1234567890!@#$%^&*()_+=,./;"

#Start the GUI
root = Tk()
root.title("Password Generator")
root.geometry('375x350')

def new_rand():
    #Clear the Entry Box
    pw_entry.delete(0, END)
    pw_Length = int(char_entry.get())
    password = ""
    for x in range(0,pw_Length):
            password_char = random.choice(chars)
            password = password + password_char
    pw_entry.insert(0,password)

def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

def openFile():
    b1="c:/Users/Adam/Desktop/PasswordGen/savedPasswords.txt"
    os.system('notepad.exe ' + b1)

def enterInfo():
    ifStatement_entry.delete(0, END)   
    ifStatement_entry.insert(0,"Please Enter all the Info")

def saveToFile():
    if (char_entry.get() != "" and my_entryName.get()!="" and pw_entry.get()!=""):
        #Write to the password file
        ifStatement_entry.delete(0, END)   
        ifStatement_entry.insert(0,"The Filed was Saved")
        saved_passwordfile = open("savedpasswords.txt", "a")
        saved_passwordfile.write("\n %s : %s" % (my_entryName.get(), pw_entry.get()))
        saved_passwordfile.close()   

        #Clear Out the Input fields 
        pw_entry.delete(0,END)
        my_entryName.delete(0,END)
        char_entry.delete(0,END)
    else:
        enterInfo()
  
def on_closing():
    #Add a Time stamp to the file to know the last used time 
    saved_passwordfile = open("savedpasswords.txt", "a")
    saved_passwordfile.write("\n Last used: " + time.asctime() + "\n")
    saved_passwordfile.close()    

    #Close the File  
    root.destroy()

#Label Frame
lf = LabelFrame(root, text = "How many characters?")
lf.pack(pady=8)

#Create Entry Box
char_entry = Entry(lf, font =('Tahoma', 15))
char_entry.pack(pady=20,padx=20)

#Label Frame for Name
lf2 = LabelFrame(root, text = "The Password Use?")
lf2.pack(pady=8)

#Create Entry Box for Namee
my_entryName = Entry(lf2, font =('Tahoma', 15))
my_entryName.pack(pady=12,padx=20)

#Create Entry Box of Retuened Password
pw_entry = Entry(root, text='', font=('Tahoma', 18), bd=0, bg="lightgrey")
pw_entry.pack(pady=7)

#Create Entry Box of ifStatement_entry
ifStatement_entry = Entry(root, text='', font=('Tahoma', 13), bd=0, bg="systembuttonface")
ifStatement_entry.pack(pady=7)

#Create a frame for Buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#Create the buttons
my_buttons = Button(my_frame, text ="Create Passsword",command =new_rand, fg='black', bg='lightgreen')
my_buttons.grid(row=-0,column=0, padx=10)

save_button =Button(my_frame, text='Save To File', command=saveToFile, fg='black', bg='lightgreen')
save_button.grid(row=-0,column=10, padx=10)

clip_button =Button(my_frame, text='Open File', command=openFile, fg='black', bg='lightgreen')
clip_button.grid(row=-0,column=20, padx=10)


#On Closing Action
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()