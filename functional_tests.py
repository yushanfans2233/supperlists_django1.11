from selenium import webdriver

browser = webdriver.Chrome(executable_path=r"F:\app\chromedriver.exe")
browser.get('http://localhost:8000')

assert 'Django' in browser.title
