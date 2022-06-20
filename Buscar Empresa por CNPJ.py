from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/<cnpj_params>")
def hello_world(cnpj_params):
    cnpj = {'cnpj': cnpj_params}
    api_url_base = "https://cnpj.biz/api/v2/empresas/cnpj"
    api_token = "L3msTmzII3B0k0Schq3D6GIFa2CYAK2pqLMeDzY8Ksq5gUDtwz4qHdWj5E3x"
    headers = {'Content-Type': 'application/json','Authorization': 'Bearer {0}'.format(api_token), 'Accept':'application/json'}
    api_url = '{0}'.format(api_url_base)
    requesito = requests.post(api_url, headers=headers, json=cnpj)
    if requesito.status_code == 200:
        total = json.loads(requesito.content.decode('utf-8'))
        return {
            "Nome da Empresa": total['razao_social'],
            "CNPJ" : total['cnpj'],
            "Situação": total['situacao'],
            "Telefone" : total['telefones'][0]['telefone']
        }
    else:
        return "CNPJ não Encontrado"
    
if __name__ == '__main__':
    app.run(debug=True)