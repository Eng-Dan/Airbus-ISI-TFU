from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import keyboard
import time

def run_bot_pdf_download(document_id, documentType, documentUrl, AirbusUserName, AirbusUserPass, waitToDownload=5):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    with webdriver.Chrome("C:\\Users\\danilo.bezerra\\Programming\\Resources\\chromedriver.exe", options=options) as driver:
        print("Bot: Getting PDF document:", documentType, document_id, "...")
        #driver.implicitly_wait(10)

        driver.get(documentUrl)

        loginField = driver.find_element_by_name("USER")
        passwordField = driver.find_element_by_name("PASSWORD")

        documentWindowHandle = driver.current_window_handle

        loginField.send_keys(AirbusUserName)
        passwordField.send_keys(AirbusUserPass)
        passwordField.send_keys(Keys.RETURN)

        #time.sleep(1)
        
        try:
            saveButton = driver.find_element_by_xpath('//*[@id="save"]/a')
        except:
            print('-- Bot: Error: Save button not found by XPath = //*[@id="save"]/a')

            try:
                saveButton = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[1]/td[2]/a/img')
            except:
                print('-- Bot: Error: Save button not found by XPath = /html/body/div/div[1]/table/tbody/tr[1]/td[2]/a/img')
                print("   Bot: None files downloaded")
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
                
        time.sleep(1)

        keyboard.send(['ctrl', 's'])

        time.sleep(1)

        documentName =  document_id + '_' + documentType

        for char in documentName:
            keyboard.write(char)

        keyboard.press('enter')
        print("  Bot: Download launched")

        time.sleep(waitToDownload)