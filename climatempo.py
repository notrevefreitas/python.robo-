import requests
import jason 


requisicao = requests.get("https://economia.awesomeapi.com.br/json/all/:moedas")
cotacao = jason.loads (requisicao.text)

print(cotacao)