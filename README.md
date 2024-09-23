# Python-Trashmail
Python Trashmail Wrapper from futquest trashmail

# Installation

We currently don't have our lib on pip or yarn, so you need to download the trashmail.py from the github files manuelly or using git.

# How to use?

```py
from trashmail import Trashmail

def new_email_callback(emails):
    print("New emails received:", emails)

mail = Trashmail()
print("Adress: " + mail.adress)
mail.onEmail(new_email_callback)
```

This is a simple example how to get an adress and log emails to it.

# Functions

You got a few functions you can use.
```py
getAdress() # returns the adress you are using

revokeAdress() # will clear the adress

renewAdress() # will give you a new adress and return the new adress

getInbox() # will return the current inbox of the adress

onEmail(callback) # will trigger the callback function every time you receive a new email
```


# Future

In future we will implement the option to choose own adresses and not get a random one.


# Disclaimer

The domain will always be futquest.com. It is not blacklisted for any service and we are happy if you won't use it too offensive and get it banned on a website :).
