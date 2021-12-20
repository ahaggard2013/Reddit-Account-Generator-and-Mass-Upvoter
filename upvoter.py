#!/usr/bin/env python
from selenium import webdriver
import time 
import os

loginFile = 'createdNames.txt'

#update with comment link or post link to upvote
postLink = 'https://www.reddit.com/r/hiring/comments/rkdb6f/for_hire_freelance_recruiter_hr_pro_looking_for/?utm_source=share&utm_medium=web2x&context=3'
commentPermaLink = ''
def login(browser, username, password):
     #insert username
    browser.find_element_by_id('loginUsername').click()
    browser.find_element_by_id('loginUsername').send_keys(username)
    #insert password
    browser.find_element_by_id('loginPassword').click()
    browser.find_element_by_id('loginPassword').send_keys(password)
    #login
    browser.find_element_by_xpath("//*[contains(text(), 'Log In')]").click()
    time.sleep(2)
def upvote_post(browser, username, password, postLink):
    login(browser, username, password)    #get link page
    browser.get(postLink)
    browser.find_element_by_xpath("//button[contains(@aria-label, 'upvote')]").click()
    
    time.sleep(2)

def upvote_comment(browser, username, password, commentLink):
    login(browser, username, password)
    #get link page
    browser.get(commentLink)
    browser.find_element_by_css_selector('div.midcol:nth-child(2) > div:nth-child(1)').click()
    #logout
    browser.find_element_by_css_selector('.logout > a:nth-child(4)').click()
    time.sleep(2)
    browser.get('http://www.reddit.com')

def main():
    browser = webdriver.Firefox()
    browser.get('http://reddit.com/login')

    #comment out post or comment depending on what you'd like to upvote
    creds = [cred.strip() for cred in open(loginFile).readlines()]
    for cred in creds:
        username, password = cred.split(':')
        #upvote_comment(browser, username,password,commentPermaLink)
        upvote_post(browser, username, password, postLink)

main()
