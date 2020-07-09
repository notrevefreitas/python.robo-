import requests
import json 


requisicao = requests.get("https://economia.awesomeapi.com.br/json/all/:moedas")
cotacao = json.loads (requisicao.text)

print(cotacao)