import requests

url = 'https://sicnet2.aneel.gov.br/sicnetweb/pdf_consolidar.aspx?cod_protocolo=4241093&cod_id_usuario_externo=17939526&txt_email=paulo.renato.reche@gmail.com'
url2 = 'https://sicnet2.aneel.gov.br/sicnetweb/pdf_consolidar.aspx?cod_protocolo=4244085&cod_id_usuario_externo=17939526&txt_email=paulo.renato.reche@gmail.com'
r = requests.get(url2, verify=False) ## Ignorando validação do certificado SSL
##aqui = os.path.abspath(os.getcwd())
with open('nsample.pdf','wb') as f:
    f.write(r.content)