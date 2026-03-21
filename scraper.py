from bs4 import BeautifulSoup
import requests
from config import TODAY, TOMORROW

def data_colect():
    s = requests.Session()

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
        "tpPesquisa": "6",
        "dtInicial": TODAY.strftime("%d/%m/%Y"),
        "dtFinal": TOMORROW.strftime("%d/%m/%Y"),
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

    print("STATUS POST: ", resp_post.status_code)

    return resp_post.text