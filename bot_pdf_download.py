from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import keyboard
import time

urlLinktoDocument = 'https://w3.airbus.com/1H43/MEFO_AW/TFU/MzYuMTEuMDAxMDY=/article.html'

userName = input("Enter your login: ")
userPass = input("Enter your password: ")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Path to use in personnal laptop
# driver = webdriver.Chrome("C:\\Users\\danil\OneDrive\\Dev Repository\\Packages-Resorces\\chromedriver.exe")

# Path to use in LATAM's laptop
driver = webdriver.Chrome("C:\\Users\\danilo.bezerra\\Documents\\Dev Resources\\chromedriver.exe", options=options)

driver.get(urlLinktoDocument)

loginField = driver.find_element_by_name("USER")
passwordField = driver.find_element_by_name("PASSWORD")

documentWindowHandle = driver.current_window_handle

loginField.send_keys(userName)
passwordField.send_keys(userPass)
passwordField.send_keys(Keys.RETURN)

saveButton = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[1]/td[2]/a/img')

actions = ActionChains(driver)
actions.move_to_element(saveButton)
actions.click()
actions.perform()

for window_handle in driver.window_handles:
        if window_handle != documentWindowHandle:
            driver.switch_to.window(window_handle)
            break

time.sleep(1)

keyboard.press(['ctrl', 's'])
time.sleep(1)
keyboard.press('enter')

time.sleep(20)

driver.quit()