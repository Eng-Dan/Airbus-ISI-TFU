from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import keyboard
import time

def activate_bot(documentUrl, AirbusUserName, AirbusUserPass):
    urlLinktoDocument = documentUrl

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

    loginField.send_keys(AirbusUserName)
    passwordField.send_keys(AirbusUserPass)
    passwordField.send_keys(Keys.RETURN)

    assert driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[1]/td[2]/a/img')
    saveButton = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[1]/td[2]/a/img') #--> To ISI 36.11.00106
    #saveButton = driver.find_element_by_xpath('//*[@id="save"]/a')
                                            
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

    time.sleep(5)

    driver.quit()