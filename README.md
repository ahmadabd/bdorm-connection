# bdormhot.co-check-connection

This program get your accounts and stores them into database.<br> 
it connect you to bdormhot.co with one of your available account and check your connection all the time.

This program is written by Ahmad Abdollahzade . Use it , make it better and share it.

##Usage :
First run these commands on terminal :
```
    sudo apt update
    sudo apt install python-pip
    pip install BeautifulSoup
    pip install requests
```
###run this program by :
```
    python index.py
    or
    ./index.py
```
###Options :
valid args:<br>
'--help' show you all of options.<br>
'-a' for add new account.<br>
'-b' for to bdorm.<br>
'-c' for check all added account.<br>
'-d' delete one of your account.<br>
'-u' update password of your account.
```
    python index.py -option
    or 
    ./index.py arg -option
```