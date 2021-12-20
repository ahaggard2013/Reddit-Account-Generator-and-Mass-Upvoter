#!/usr/bin/env python
from selenium import webdriver
from random import randint
import time 
import os



userNamePasswordFile = 'redditNameList.txt'
createdUserNamePasswordFile = 'createdNames.txt'


def create_account(username, password):
    #set up profile for proxy
    profile = webdriver.FirefoxProfile()
    #profile.set_preference("network.proxy.type", 1)
    #profile.set_preference("network.proxy.socks", '127.0.0.1')
    #profile.set_preference("network.proxy.socks_port", 9050)
    #profile.set_preference("network.proxy.socks_remote_dns", True)
    profile.update_preferences()
    browser = webdriver.Firefox(firefox_profile=profile)

    #get reddit account creation page
    browser.set_window_size(683, 744)
    browser.get('https://www.reddit.com/account/register/')
    #insert username
    time.sleep(randint(1,5))
    browser.find_element_by_id('loginUsername').click()
    browser.find_element_by_id('loginUsername').send_keys(username)
    #insert password
    time.sleep(randint(1,5))
    browser.find_element_by_id('loginPassword').click()
    browser.find_element_by_id('loginPassword').send_keys(password)
    time.sleep(randint(1,5))
    browser.find_element_by_id('passwd2_reg').click()
    browser.find_element_by_id('passwd2_reg').send_keys(password)
    #pause to manually enter captcha
    some_input = input("[*] Solve captcha, create account, then press enter... enter 'r' as some_input if captcha doesn't appear to skip username" + '\n')
    if (some_input == 'r'):
        os.system('clear')
        browser.quit()
        return False
    else:
        browser.quit()
        return True





def main():
    os.system('clear')
    #run account generator for each user in list
    created = open(createdUserNamePasswordFile, 'a')
    creds = [cred.strip() for cred in open(userNamePasswordFile).readlines()]
    for cred in creds:
        username, password = cred.split(':')
        print('[+] creating account for %s with password %s' % (username,password))
        account_created = create_account(username, password)
        print('[+] restarting tor for a new ip address...')
        os.system('service tor restart')
        if account_created:
            print('[+] writing name:password to created names...')
            created.write(username + ':' + password + '\n')
            print('[+] deleting name:password from original file...')
            lines = [line.strip() for line in open(userNamePasswordFile).readlines()]
            f = open(userNamePasswordFile, 'w')
            for line in lines:
                if (line != cred):
                    f.write(line + "\n")
            f.close()
        else:
            print('[-] name not recorded due to captcha issue')
        time.sleep(2)
        os.system('clear')
    created.close()

    
main()
