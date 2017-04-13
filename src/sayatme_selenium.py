# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:09:02 2017

@author: Swapnil.Walke
"""


import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint

def init():
    chromedriver = "C:\Users\chromedriver_win32\chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    return driver

def foo(sayat_link, driver):
    driver.get(sayat_link)
    elem = driver.find_element_by_name("write")
    elem.clear()
    comments = {1 : 'Better you ask your mom, she still regret that mistake. :P',
                2 : 'huh! Well I dont wanna tell anything about you',
                3 : 'If I had a gun with two bullets and had to shoot either you or Trump then, I would have shooted you twice in the head, B**ch!', 
                4 : 'hmmm...cant think of anything...',
                5 : 'Are you the one who asks everybody about how he/she is? :P',
                6 : 'ohh god! Dont ask me this, I have got a life to live! ',
                7 : 'Do you know when the stupidity was invented?, it was invented on your birthday :D',
                8 : 'Huh! do you really want me to write about you? come one, forget about it!',
                9 : 'Have got work, cant waste time writing about it. :P',
                10 : 'I know you were friend zoned! I know your secrets! haha! :D'}
    elem.send_keys(comments[randint(1,10)])
    driver.find_element_by_xpath("//div[@class='give-feedback']/form/div[@class='row']/div[@class='col-md-4 col-sm-12 col-xs-12 pull-right']/input[@value='Say it.']").click()
    driver.close()

if __name__ == '__main__':
    driver = init()
    sayat_link = ''
    while True:
        foo(sayat_link, init())
    