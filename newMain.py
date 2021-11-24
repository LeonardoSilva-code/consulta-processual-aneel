from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time, openpyxl, requests, threading
import downloadThread as dt


solicitarAcesso = []
toEmail = []
threads = list()

user = 'paulo.renato.reche@gmail.com'
password = '1234'
Arquivo = "[ANEEL]+Solar+Powerplants.xlsx"


processoDow = ['48500', '002913', '2019']
processoEmail = ['48500','001475','2019']
processoSolicitar = ['48500', '002226', '2017']

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(executable_path='C:\Cdriver\chromedriver.exe', options=options)
driver.get('http://www.aneel.gov.br/consulta-processual')

##Login
elem = driver.find_element_by_css_selector('#_58_login')
elem.clear()
elem.send_keys(user)

elem = driver.find_element_by_css_selector('#_58_password')
elem.clear()
elem.send_keys(password)

print('6 segundos para o captcha...')
time.sleep(6)
elem.send_keys(Keys.RETURN)

#Clickando no botão
time.sleep(3)
x = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div/div[2]/div/div[2]/div/div/div[1]/a')
x.click()
time.sleep(4)

print("Baixando Primeiro Processo...")
numeroOrgao = driver.find_element_by_id('txt_numero_orgao')
numeroSeq = driver.find_element_by_id('txt_numero_sequencial')
ano = driver.find_element_by_id('txt_numero_ano')
numeroOrgao.send_keys(processoEmail[0])
numeroSeq.send_keys(processoEmail[1])
ano.send_keys(processoEmail[2])
print("6 segundos para o captcha")
time.sleep(6)
ano.send_keys(Keys.RETURN)
link = driver.find_element_by_partial_link_text(str(processoEmail[1]))
link.click()

downloadButton = driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/div/p[1]/input')
downloadButton.click()

time.sleep(1)
try:
    actions = ActionChains(driver.switch_to.window(driver.window_handles[1]))
    actions.send_keys(Keys.ENTER)
    actions.perform()
    '''
    WebDriverWait(driver,4).until(EC.number_of_windows_to_be(1))
    print("no alert")
    '''
except:
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    driver.close()
    driver.switch_to.window(windows[0])
    print('alert closed')
