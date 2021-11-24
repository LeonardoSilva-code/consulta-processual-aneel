import requests

def download(link, processo):
    print('starting: ' + str(processo))
    alerta = 'Devido ao tamanho do PDF deste protocolo, você receberá por e-mail, em breve, um link de download do arquivo solicitado.'
    nome = (str(processo[0]) + '.' + str(processo[1]) + '_' + str(processo[2]) + '.pdf')
    r = requests.get(link, verify=False)
    try:
        t = r.text
        print(t)
        if t.find(alerta) > -1:
            print(nome + ' to email')
            return 
        with open(nome,'wb') as f:
            f.write(r.content)
            print("Baixado")
    except:
        with open(nome,'wb') as f:
            f.write(r.content)
            print("Baixado")


url = 'https://sicnet2.aneel.gov.br/sicnetweb/pdf_consolidar.aspx?cod_protocolo=4722977&cod_id_usuario_externo=17939526&txt_email=paulo.renato.reche@gmail.com'

download(url,['9','9','9'])