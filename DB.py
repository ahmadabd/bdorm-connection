#!/usr/bin/env python

import sqlite3

db = sqlite3.connect('account.db')  # set address as /home/$USER/bdorm/account.db . 
db.row_factory = sqlite3.Row

def createTable():
    db.execute('CREATE TABLE account (username VARCHAR(15), password VARCHAR(30))')
    db.commit()

def add(user,passwd):
    db.execute('INSERT INTO account (username,password) VALUES (?,?)',(user,passwd))
    db.commit()

def check():
    c = 1
    cursor = db.execute('SELECT * FROM account')
    for result in cursor:
        print "",c,".",result['username'],':',result['password']
        c += 1

def sendInfoToSite():
    account = []
    reader = db.execute('SELECT * FROM account')
    for result in reader:
        account.append(dict(result))
    return account

def delete():
    l = []
    c = 0
    cursor = db.execute('SELECT * FROM account')
    for result in cursor:
        l.append(result['username'])
        print c,".",result['username']
        c += 1
    userNum = raw_input("Enter num of account for delete : ")
    if int(userNum) > len(l) - 1:
        print "your input was out of range."
        exit()
    db.execute('DELETE FROM account WHERE username=?',(l[int(userNum)],))
    db.commit()

def update():
    l = []
    c = 0
    cursor = db.execute('SELECT * FROM account')
    for result in cursor:
        l.append(result['username'])
        print c, ".", result['username']
        c += 1
    userNum = raw_input("Enter num of user for update : ")
    if int(userNum) > len(l) - 1:
        print "your input was out of range."
        exit()
    passwd = raw_input("Enter new password : ")
    db.execute('UPDATE account SET password=? WHERE username=?',(passwd,l[int(userNum)]))
    db.commit()
