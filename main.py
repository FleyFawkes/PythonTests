from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "D:\Pliki\Git_repo\Selenium\chromedriver.exe" # Path to the webdriver.
driver = webdriver.Chrome(PATH)

driver.get("https://www.amazon.com/")

stringtest = "   " #string to test

try:
    assert stringtest in driver.title #first assertion to test if a string is a substring of a landing page title
except AssertionError:
    print("Assertion Error #1 - String is not a substring of a title.")

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("python")
search.send_keys(Keys.RETURN)
search = driver.find_element_by_css_selector("[alt='Automate the Boring Stuff with Python, 2nd Edition: Practical Programming for Total Beginners']")
search.click()


time.sleep(3)
driver.close()

