from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://stephenl6705.pythonanywhere.com/')

assert 'Django' in browser.title