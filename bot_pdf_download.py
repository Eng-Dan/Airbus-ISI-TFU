from selenium import webdriver
import selenium
# from selenium.webdriver.common.keys import Keys

# To use in personnal laptop
# driver = webdriver.Chrome("C:\\Users\\danil\OneDrive\\Dev Repository\\Packages-Resorces\\chromedriver.exe")

# To use in LATAM's laptop
driver = webdriver.Chrome("C:\\Users\\danilo.bezerra\\Documents\\Dev Resources\\chromedriver.exe")

urlToAirbusWorld = 'https://w3.airbus.com/H380/world/airbusworld/forms/airbus.sfcc?TYPE=33554433&REALMOID=06-653aefcb-c624-47d3-bc0a-85721530460f&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-t%2fTX88CtTFIPqQ15ugBfOME66PQGCWGuAAOSByMZUiVIJPozo431pS4LE4YuSGzU&TARGET=-SM-https%3a%2f%2fw3%2eairbus%2ecom%2fnewairbusworld'
urlLinktoDocument = 'https://w3.airbus.com/1H43/MEFO_AW/TFU/MzYuMDAuMDAuMDA5/article.html'

driver.get(urlLinktoDocument)

# userName = 'SAO_danilobs'
# passWord = 'Aib20211'

# C:\Users\danil\Programming\anaconda3\Scripts\pip.exe install selenium