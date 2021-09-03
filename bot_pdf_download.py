from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import keyboard
import time

def run_bot_pdf_download(document_id, documentUrl, AirbusUserName, AirbusUserPass):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    with webdriver.Chrome("C:\\Users\\danilo.bezerra\\Programming\\Resources\\chromedriver.exe", options=options) as driver:
        print("Getting PDF...")
        #driver.implicitly_wait(10)

        driver.get(documentUrl)

        loginField = driver.find_element_by_name("USER")
        passwordField = driver.find_element_by_name("PASSWORD")

        documentWindowHandle = driver.current_window_handle

        loginField.send_keys(AirbusUserName)
        passwordField.send_keys(AirbusUserPass)
        passwordField.send_keys(Keys.RETURN)

        time.sleep(1)
        
        try:
            saveButton = driver.find_element_by_xpath('//*[@id="save"]/a')
        except:
            print('-- Error: Save button not found by XPath = //*[@id="save"]/a')

            try:
                saveButton = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[1]/td[2]/a/img')
            except:
                print('-- Error: Save button not found by XPath = /html/body/div/div[1]/table/tbody/tr[1]/td[2]/a/img')
                print("   No files downloaded")
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

        for letter in document_id:
            keyboard.write(letter)

        time.sleep(1)

        keyboard.press('enter')
        print("  Download launched")

        time.sleep(8)



# Single test case
docId = '11.00.33.444'
url = 'https://w3.airbus.com/1H43/MEFO_AW/ISI/MjcuNTQuMDAwMDE=/article.html'
run_bot_pdf_download(docId, url, 'SAO_danilobs', 'Aib20211')