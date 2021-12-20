#!/usr/bin/env python
from selenium import webdriver
from random import randint
import time 
import os
from selenium.common.exceptions import NoSuchElementException



userNamePasswordFile = 'redditNameList.txt'
createdUserNamePasswordFile = 'createdNames.txt'


def create_account(username, password):
    #set up profile for proxy
    profile = webdriver.FirefoxProfile()
    '''profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", '127.0.0.1')
    profile.set_preference("network.proxy.socks_port", 9050)
    profile.set_preference("network.proxy.socks_remote_dns", True)'''
    profile.update_preferences()
    browser = webdriver.Firefox(firefox_profile=profile)

    #get reddit account creation page
    browser.get('https://www.reddit.com/register/')
    print("waiting for you to enter a email")
    time.sleep(randint(2,3))
    browser.find_element_by_id('regEmail').send_keys(username+"@cds.com"+'\n')
    browser.find_element_by_xpath("//button[contains(text(), 'Continue')]").click()
    #insert username
    time.sleep(randint(1,5))
    browser.find_element_by_id('regUsername').click()
    browser.find_element_by_id('regUsername').send_keys(username)
    #insert password
    time.sleep(randint(1,5))
    browser.find_element_by_id('regPassword').click()
    browser.find_element_by_id('regPassword').send_keys(password)
    time.sleep(randint(1,5))
    browser.find_element_by_xpath("//*[contains(text(), 'Sign Up')]").click()
    #pause to manually enter captcha
    myinput = input("[*] Solve captcha, create account, then press enter... enter 'r' as input if captcha doesn't appear to skip username" + '\n')
    if (myinput == 'r'):
        
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
    global username,password
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
        
    created.close()

    
main()
