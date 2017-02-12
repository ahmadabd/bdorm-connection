#!/usr/bin/env python

import db
import requests
import BeautifulSoup
import time,sys

# bdorm check connection. 
# auther : Ahmad Abdollahzade (ahmadabd13741112@gmail.com)

def getPasswd():        # Get your user and password and stores them into account.scv .
    user = raw_input("Enter userName : ")
    passwd = raw_input("Enter password : ")
    if len(user) > 0 and len(passwd) > 0:
        db.add(user,passwd)
    else:
        getPasswd()
    
def post():              # This function connect one of your account to http://bdorm.co/login and check the connection.
    account = db.sendInfoToSite()
    while True:          # Sleep program for 5 second.
        time.sleep(5)
        for i in range(len(account)):
            try:
                check = requests.get("http://bdormhot.co/login")
            except:
                print "connection failed."
                break
            soup = BeautifulSoup.BeautifulSoup(check.content)
            if soup.find("meta",{"http-equiv" : "refresh"}) == None:  # Check http://bdormhot.co/status is available or not. 
                r = requests.post("http://bdormhot.co/login",data = account[i])
                print "user: ",account[i]["username"]
                if soup.find("meta",{"http-equiv" : "refresh"}) != None:
                    break
        
def check():              # It is for seeing all of available usernames.
    db.check()

def delete():             # Delete accounts base on username.
    db.delete()

def update():             # Update password of accounts base on username.
    check()
    user = raw_input("Enter user for update : ")
    passwd = raw_input("Enter new password : ")
    db.update(user,passwd)

def help():               # Show program options.
    print "bdorm.py: "
    print "Usage: bdorm.py [-a add new account] [-b connect to bdorm] [-c check valid accounts] \n                [-d delete an account] [-u update password of account] "

def main():
    #db.createTable()     # It makes account table for the first time.
    if len(sys.argv) > 1:
        if sys.argv[1] == "-a":
            getPasswd()
            exit()
        elif sys.argv[1] == "-b":
            post()
        elif sys.argv[1] == "-c":
            check()
            exit()
        elif sys.argv[1] == "-d":
            delete()
            exit()
        elif sys.argv[1] == "-u":
            update()
            exit()
        elif sys.argv[1] == "--help":
            help()
            exit()

    choice = raw_input("(a) For adding new account\n(b) For conneting to net\n(c) And for seeing added account\n(d) For deleting account\n(u) For update password\n(q) Exit\n>>") # Ask what do you want to do?
    if len(choice) > 0:
        if choice == 'a':
            getPasswd()
            main()
        elif choice == 'b':
            post()
        elif choice == 'c':
            check()
            main()
        elif choice == 'd':
            delete()
            main()
        elif choice == 'u':
            update()
            main()
        elif choice == 'q':
            exit()
        else:
            main()
    else:
        main()

main()
