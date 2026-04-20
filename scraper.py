from bs4 import BeautifulSoup
import requests
from datetime import datetime

def data_collect():
    s = requests.Session()
    now = datetime.now()
    datetime_req = now.strftime("%d/%m/%Y %H:%M")

    # Requisição para a BTP
    url = "https://novo-tas.btp.com.br/ConsultasLivres/RecebimentoExportacao"

    resp_get = s.get(url)

    if resp_get.status_code != 200:
        print("Erro no GET: ", resp_get.status_code)

    # Corpo do HTML
    sp = BeautifulSoup(resp_get.text, "html.parser")

    # Buscando o token para poder fazer as requisições
    token_input = sp.find("input", {"name":"__RequestVerificationToken"})

    if not token_input:
        print("Token não encontrado")
        return None
    
    token = token_input["value"]

    # Enviando no corpo do HTML os filtros para a pesquisa dos navios
    payload = {
        "tpPesquisa": "0",
        "dtInicial": "",
        "dtFinal": "",
        "Viagem": "",
        "Servico": "0"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "__RequestVerificationToken": token
    }

    url_post = "https://novo-tas.btp.com.br/ConsultasLivres/PesquisaRecebimentoExportacao"

    resp_post = s.post(url_post, data=payload, headers=headers)

    print(f"{datetime_req} - STATUS POST: {resp_post.status_code}")

    return resp_post.text