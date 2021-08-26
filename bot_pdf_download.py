'''Selenium documentation at https://selenium-python.readthedocs.io/installation.html'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

urlToAirbusWorld = 'https://w3.airbus.com/H380/world/airbusworld/forms/airbus.sfcc?TYPE=33554433&REALMOID=06-653aefcb-c624-47d3-bc0a-85721530460f&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-t%2fTX88CtTFIPqQ15ugBfOME66PQGCWGuAAOSByMZUiVIJPozo431pS4LE4YuSGzU&TARGET=-SM-https%3a%2f%2fw3%2eairbus%2ecom%2fnewairbusworld'
urlLinktoDocument = 'https://w3.airbus.com/1H43/MEFO_AW/TFU/MzYuMTEuMDAxMDY=/article.html'

# userName = input("Enter your login: ")
# userPass = input("Enter your password: ")
# login = SAO_danilobs
# pass = 'Aib20211'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Path to use in personnal laptop
# driver = webdriver.Chrome("C:\\Users\\danil\OneDrive\\Dev Repository\\Packages-Resorces\\chromedriver.exe")

# Path to use in LATAM's laptop
driver = webdriver.Chrome("C:\\Users\\danilo.bezerra\\Documents\\Dev Resources\\chromedriver.exe", options=options)

driver.get(urlLinktoDocument)

loginField = driver.find_element_by_name("USER")
passwordField = driver.find_element_by_name("PASSWORD")

loginField.send_keys("SAO_danilobs")
passwordField.send_keys("Aib20211")
passwordField.send_keys(Keys.RETURN)

#driver.close()