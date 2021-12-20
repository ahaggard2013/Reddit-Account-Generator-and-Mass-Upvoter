#!/usr/bin/env python
import random
import string
import names


def generate_username_password(amount, ulength, plength, list):
    for _ in range(0,amount):
        username = names.get_full_name()
        username = ''.join(username.split())
        username+=str(random.randint(100,9999))
        list.write(username+':'+ ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(plength)) + '\n')

        
list = open('redditNameList.txt', 'w')
generate_username_password(100,15,15, list)
list.close()
