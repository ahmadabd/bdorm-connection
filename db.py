#!/usr/bin/env python

import sqlite3

db = sqlite3.connect('account.db')  # You cat set there main address like /home/$USER/... .
db.row_factory = sqlite3.Row

def createTable():
    db.execute('CREATE TABLE account (username VARCHAR(15), password VARCHAR(30))')
    db.commit()

def add(user,passwd):
    db.execute('INSERT INTO account (username,password) VALUES (?,?)',(user,passwd))
    db.commit()

def check():
    cursor = db.execute('SELECT * FROM account')
    for result in cursor:
        print result['username'],':',result['password']

def sendInfoToSite():
    account = []
    reader = db.execute('SELECT * FROM account')
    for result in reader:
        account.append(dict(result))
    return account

def delete():
    cursor = db.execute('SELECT * FROM account')
    for result in cursor:
        print result['username']
    userOfDelete = raw_input("Enter user for delete : ")
    db.execute('DELETE FROM account WHERE username=?',(userOfDelete,))
    db.commit()

def update(user,passwd):
    db.execute('UPDATE account SET password=? WHERE username=?',(passwd,user))
    db.commit()
