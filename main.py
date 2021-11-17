from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


user = 'paulo.renato.reche@gmail.com'
password = '1234'
chaves = ['48500', '002913', '2019']

driver = webdriver.Chrome(executable_path='C:\Cdriver\chromedriver.exe')
driver.get('http://www.aneel.gov.br/consulta-processual')
##time.sleep(3)


elem = driver.find_element_by_css_selector('#_58_login')
elem.clear()
elem.send_keys(user)

elem = driver.find_element_by_css_selector('#_58_password')
elem.clear()
elem.send_keys(password)



time.sleep(6)
elem.send_keys(Keys.RETURN)
time.sleep(6)
x = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div/div[2]/div/div[2]/div/div/div[1]/a')
x.click()
time.sleep(4)
numeroOrgao = driver.find_element_by_id('txt_numero_orgao')
numeroOrgao.send_keys(chaves[0])

numeroSeq = driver.find_element_by_id('txt_numero_sequencial')
numeroSeq.send_keys(chaves[1])

ano = driver.find_element_by_id('txt_numero_ano')
ano.send_keys(chaves[2])
time.sleep(6)
ano.send_keys(Keys.RETURN)
time.sleep(3)
link = driver.find_element_by_partial_link_text(chaves[1])
link.click()

ns = '002943'
time.sleep(3)
driver.execute_script("document.getElementById('acao_voltar').setAttribute('value', '1')")
driver.execute_script("document.getElementById('txt_numero_orgao').setAttribute('value','48500')")
driver.execute_script("document.getElementById('txt_numero_ano').setAttribute('value','2019')")
driver.execute_script("document.getElementById('txt_numero_sequencial').setAttribute('value','002943')")
voltar = driver.find_element_by_css_selector('#conteudo > p > input[type=button]:nth-child(2)')
voltar.click()
time.sleep(3)
link = driver.find_element_by_partial_link_text(chaves[1])
link.click()




'''
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()'''