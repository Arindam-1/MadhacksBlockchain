#!/usr/bin/python
import base64
import getpass
def create():
    username = "0"
    file = open("userpass.txt","a")
    while not username == "-1":
        print("If you do not want to continue, enter -1")
        username = str(raw_input("Enter your username : ").strip())
        if(username == "-1"):
            break
        else:
            password = getpass.getpass().strip()
            cr = base64.encodestring(password)
            file.write(username+","+cr+'\n')
    file.close()


def enter():
    up_username = str(raw_input("Username: ").strip())
    up_password = password = getpass.getpass().strip()
    enc_pass = base64.encodestring(up_password)
    with open("userpass.txt","r") as f:
        for line in f:
            if line.split(",")[0] == up_username and line.split(",")[1] == enc_pass:
                return True
        return False

def verifyUser(username, password, bc):
    # Verify count
    count = 0
    for i in range(len(bc)):
        if bc[i][1] == username:
            if count >= 1:
                return False
            else:
                count += 1

    # Verify uid and password
    enc_pass = base64.encodestring(password)
    with open("userpass.txt","r") as f:
        for line in f:
            if line.split(",")[0] == username and line.split(",")[1] == enc_pass:
                return True
        return False

def main():
    choice = str(raw_input("Add new usernames/passwords or login --> Enter [1 or 2]"))
    if choice=="1":  
        create()
    else:
        if enter():
            print("Logged in!")
        else:
            print("Incorrect!")

if __name__ == "__main__":
    main()
