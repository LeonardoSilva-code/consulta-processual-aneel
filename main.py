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
import tempfile
import shutil


solicitarAcesso = []
toEmail = []
threads = list()

user = 'paulo.renato.reche@gmail.com'
password = '1234'
Arquivo = "[ANEEL]+Solar+Powerplants.xlsx"

print('Carregando Arquivo...')
Excel = openpyxl.load_workbook(Arquivo)
active_excel = Excel.active
linha = []
processos = [['0']]
print(processos[0][0])
linhaAtual = active_excel.max_row + 1
for row in range(2,linhaAtual):  
    for column in "H":                                              
        cell_name = "{}{}".format(column, row)
        celula = str(active_excel[cell_name].value)
        celula = celula.replace('/','.').replace(',','.')
        processos.append([celula])

processos = processos[:50]  
#print(processos)
chaves = [[]]
for processo in processos:
    aux = processo[0].split('.')
    if len(aux) > 3:
        print(aux[5])
        while(len(aux) > 3):
            if int(aux[2][:4]) > int(aux[5][:4]):
                aux = aux[:3]
            else:
                aux = aux[3:]
    if aux != chaves[len(chaves)-1]:
            chaves.append(aux)

chaves = chaves[2:]
print(chaves)
print(len(chaves))


dirpath = tempfile.mkdtemp()
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument('download.default_directory=' + str(dirpath))
driver = webdriver.Chrome(executable_path='C:\Cdriver\chromedriver.exe', options=options)


driver.get('http://www.aneel.gov.br/consulta-processual')
##time.sleep(3)


##Login
elem = driver.find_element_by_css_selector('#_58_login')
elem.clear()
elem.send_keys(user)

elem = driver.find_element_by_css_selector('#_58_password')
elem.clear()
elem.send_keys(password)


## Primeiro Processo

time.sleep(6)
elem.send_keys(Keys.RETURN)
time.sleep(3)
x = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div/div[2]/div/div[2]/div/div/div[1]/a')
x.click()
time.sleep(4)
print("Baixando Primeiro Processo...")

numeroOrgao = driver.find_element_by_id('txt_numero_orgao')
numeroOrgao.send_keys(chaves[0][0])

numeroSeq = driver.find_element_by_id('txt_numero_sequencial')
numeroSeq.send_keys(chaves[0][1])
ano = driver.find_element_by_id('txt_numero_ano')
ano.send_keys(chaves[0][2][:4])
time.sleep(6)
ano.send_keys(Keys.RETURN)
##time.sleep(3)
link = driver.find_element_by_partial_link_text(str(chaves[0][1]))
link.click()
d = driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/div/p[1]/input')
if d.get_attribute("value") == ' SOLICITAR ACESSO ':
    solicitarAcesso.append(chaves[0])
else:    
    d.click()
    time.sleep(2)
    ##d.send_keys(Keys.RETURN)
    windows = driver.window_handles
    if (len(windows) == 2):
        driver.switch_to.window(windows[1])
        driver.close()
        driver.switch_to.window(windows[0])
    else:
        time.sleep(2)
        dowl = driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/div/div/div[1]/table/tbody/tr[6]/td[2]/a')
        url = str(dowl.get_attribute('href'))
        x = threading.Thread(target=dt.download, args=(url,chaves))
        threads.append(x)
        x.start()


chaves = chaves[1:]



##time.sleep(3)
print('Baixando demais processos')
alerta = 'Devido ao tamanho do PDF deste protocolo, você receberá por e-mail, em breve, um link de download do arquivo solicitado.'
for numero in chaves:
    try:
        time.sleep(1)
        driver.execute_script("document.getElementById('acao_voltar').setAttribute('value', '1')")
        driver.execute_script(f"document.getElementById('txt_numero_orgao').setAttribute('value','{numero[0]}')")
        driver.execute_script(f"document.getElementById('txt_numero_sequencial').setAttribute('value','{numero[1]}')")
        driver.execute_script(f"document.getElementById('txt_numero_ano').setAttribute('value','{numero[2][:4]}')")
        voltar = driver.find_element_by_css_selector('#conteudo > p > input[type=button]:nth-child(2)')
        voltar.click()

        link = driver.find_element_by_partial_link_text(f'{numero[1]}')  ##Sequencial
        link.click()
        dLink = driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/div/div/div[1]/table/tbody/tr[6]/td[2]/a')
        dLink = dLink.get_attribute('href')
        x = threading.Thread(target=dt.download, args=(dLink,numero))
        threads.append(x)
        ##x.start()

    except:
        solicitarAcesso.append(numero)
        continue

driver.close()
for thread in threads:
    thread.start()
    thread.join()

print("Processos a solicitar acesso: " + str(len(solicitarAcesso)) + "\n" + str(solicitarAcesso))
##print("\nProcessos para o email: " + str(len(toEmail)) + "\n" + str(toEmail))

shutil.rmtree(dirpath)