#!/usr/bin/env python
from selenium import webdriver
import time 
import os

loginFile = 'createdNames.txt'

#update with comment link or post link to upvote
postLink = ''
commentPermaLink = ''

def upvote_post(browser, username, password, postLink):
    #insert username
    browser.find_element_by_name('user').click()
    browser.find_element_by_name('user').send_keys(username)
    #insert password
    browser.find_element_by_name('passwd').click()
    browser.find_element_by_name('passwd').send_keys(password)
    #login
    browser.find_element_by_css_selector('.btn').click()
    time.sleep(2)
    #get link page
    browser.get(postLink)
    browser.find_element_by_css_selector('div.arrow:nth-child(1)').click()
    browser.find_element_by_css_selector('.logout > a:nth-child(4)').click()
    time.sleep(2)
    browser.get('http://www.reddit.com')
    

def upvote_comment(browser, username, password, commentLink):
    #insert username
    browser.find_element_by_name('user').click()
    browser.find_element_by_name('user').send_keys(username)
    #insert password
    browser.find_element_by_name('passwd').click()
    browser.find_element_by_name('passwd').send_keys(password)
    #login
    browser.find_element_by_css_selector('.btn').click()
    time.sleep(2)
    #get link page
    browser.get(commentLink)
    browser.find_element_by_css_selector('div.midcol:nth-child(2) > div:nth-child(1)').click()
    #logout
    browser.find_element_by_css_selector('.logout > a:nth-child(4)').click()
    time.sleep(2)
    browser.get('http://www.reddit.com')

def main():
    #comment out post or comment depending on what you'd like to upvote
    creds = [cred.strip() for cred in open(loginFile).readlines()]
    for cred in creds:
        username, password = cred.split(':')

        #set up profile for proxy
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.socks", '127.0.0.1')
        profile.set_preference("network.proxy.socks_port", 9050)
        profile.set_preference("network.proxy.socks_remote_dns", True)
        profile.update_preferences()
        browser = webdriver.Firefox(firefox_profile=profile)

        upvote_comment(browser, username,password,commentPermaLink)
        #upvote_post(browser, username, password, postLink)

        browser.quit()
        print('[+] restarting tor for a new ip address...')
        os.system('service tor restart')

main()
