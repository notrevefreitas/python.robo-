import mercadopago
import json

mp = mercadopago.MP("7108800302220549", "anwBygOp2RmDKSCDx9ekGWdhaW0meEyK")

resposta = []

def create_checkout(nome,quantidade,preco, **kwargs):
  preference = {
    "items": [
      {
        "title": nome,
        "quantity": quantidade,
        "currency_id": "BRL",
        "unit_price": preco
      }
    ]
  }
  preferenceResult = mp.create_preference(preference)
  print(preferenceResult)
  link = preferenceResult['response']['sandbox_init_point']
  id = preferenceResult['response']['id']
  return id, nome, link

def updade_checkout(req, **kwargs):
  preference = {
    "items": [
      {
        "title": "Test Modified",
        "quantity": 1,
        "currency_id": "BRL",
        "unit_price": 20.40
      }
    ]
  }
  preferenceResult = mp.update_preference(id, preference)
  return json.dumps(preferenceResult, indent=4)

def menu():
  print("1 - Criar item para pagamento")
  op = input("Escolha uma opção: ")

  if op == "1":
    nome = input("Nome do produto: ")
    quantitade = int(input("Quantidade: "))
    valor = float(input("Valor: "))
    resposta.append(create_checkout(nome,quantitade,valor))
    print(resposta)
