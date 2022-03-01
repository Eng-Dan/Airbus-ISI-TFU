from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import keyboard
import time


def run_bot(document_id, document_type, document_url, airbus_login, airbus_password, wait_to_download, chromedriver):
    """
    Automated web browsing with Selenium to download Airbus ISI or TFU documents in "pdf" format from
    Airbus World Portal.
    It uses Google Chrome browser.

    :param document_id: the reference number of the document defined by Airbus.
    :param document_type: the type of document (ISI or TFU).
    :param document_url: the link to directly download the document.
    :param airbus_login: you user name to access the Airbus World Portal.
    :param airbus_password: your password to access the Airbus World Portal.
    :param wait_to_download: an initial time interval to wait for complete download of the document.
    :param chromedriver: path to the Chrome Driver .exe file
    :return: None.

    """

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # chrome_driver = "C:\\Users\\danilo.bezerra\\Programming\\Resources\\chromedriver.exe" <-- Obsolete
    # ATTENTION! Check the correct Google Chrome Driver version in accordance with your Chrome version.
    with webdriver.Chrome(chromedriver, options=options) as driver:
        print("Bot message: Getting PDF document:", document_type, document_id, "at", document_url)

        driver.get(document_url)

        login_field = driver.find_element_by_name("USER")
        password_field = driver.find_element_by_name("PASSWORD")

        document_window_handle = driver.current_window_handle

        login_field.send_keys(airbus_login)
        password_field.send_keys(airbus_password)
        password_field.send_keys(Keys.RETURN)
        
        try:
            save_button = driver.find_element_by_xpath('//*[@id="save"]/a')
        except:
            try:
                save_button = driver.find_element_by_xpath('/html/body/div/div[1]/table/tbody/tr[1]/td[2]/a/img')
            except:
                print('\nBot message: Save button not found by XPath')
                print(">>>> ERROR to download", document_type, document_id, ': Check for correct URL link')
                driver.quit()

        actions = ActionChains(driver)
        actions.move_to_element(save_button)
        actions.click()
        actions.perform()

        time.sleep(1)

        for window_handle in driver.window_handles:
            if window_handle != document_window_handle:
                driver.switch_to.window(window_handle)
                break

        time.sleep(5)

        keyboard.send(['ctrl', 's'])

        time.sleep(5)

        document_name = document_id + '_' + document_type

        for char in document_name:
            keyboard.write(char)

        keyboard.press('enter')
        print("Bot message: Download launched")

        time.sleep(wait_to_download)
