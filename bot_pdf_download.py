from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import keyboard
import time


def run_bot_pdf_download(document_id, documentType, documentUrl, AirbusUserName, AirbusUserPass, waitToDownload=10):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    pathToChromeDriver = "C:\\Users\\danilo.bezerra\\Programming\\Resources\\chromedriver.exe"
    with webdriver.Chrome(pathToChromeDriver, options=options) as driver:
        print("Bot: Getting PDF document:", documentType, document_id, "at", documentUrl)

        driver.get(documentUrl)

        loginField = driver.find_element_by_name("USER")
        passwordField = driver.find_element_by_name("PASSWORD")

        documentWindowHandle = driver.current_window_handle

        loginField.send_keys(AirbusUserName)
        passwordField.send_keys(AirbusUserPass)
        passwordField.send_keys(Keys.RETURN)
        
        try:
            saveButton = driver.find_element_by_xpath('//*[@id="save"]/a')
        except:
            try:
                saveButton = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[1]/td[2]/a/img')
            except:
                print('\nBot: Save button not found by XPath')
                print(">>>> ERROR to download", documentType, documentType, ': Check for correct URL link')
                driver.quit()

        actions = ActionChains(driver)
        actions.move_to_element(saveButton)
        actions.click()
        actions.perform()

        time.sleep(1)

        for window_handle in driver.window_handles:
            if window_handle != documentWindowHandle:
                driver.switch_to.window(window_handle)
                break

        # wait = WebDriverWait.

        time.sleep(waitToDownload)

        keyboard.send(['ctrl', 's'])

        time.sleep(5)

        documentName = document_id + '_' + documentType

        for char in documentName:
            keyboard.write(char)

        keyboard.press('enter')
        print("Bot: Download launched")

        time.sleep(waitToDownload)