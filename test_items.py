import pytest, time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def test_language(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link) 
    button = None
    try:
        button = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    except NoSuchElementException as exception:
        print ("Button 'Add to Basket' not found")
    assert button, "Button 'Add to Basket' not found"