import requests, openpyxl
'''
url = 'https://sicnet2.aneel.gov.br/sicnetweb/pdf_consolidar.aspx?cod_protocolo=4241093&cod_id_usuario_externo=17939526&txt_email=paulo.renato.reche@gmail.com'
url2 = 'https://sicnet2.aneel.gov.br/sicnetweb/pdf_consolidar.aspx?cod_protocolo=4244085&cod_id_usuario_externo=17939526&txt_email=paulo.renato.reche@gmail.com'
r = requests.get(url2, verify=False) ## Ignorando validação do certificado SSL
##aqui = os.path.abspath(os.getcwd())
with open('nsample.pdf','wb') as f:
    f.write(r.content)'''



print('Carregando Arquivo...')
Arquivo = "[ANEEL]+Solar+Powerplants.xlsx"
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
        if celula == processos[len(processos)-1][0]:
            print('teste')
            continue
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
