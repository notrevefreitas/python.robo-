import numpy as np   
import PySimpleGUI as sg

class Automovel:

    def __init__(self, quilometrosLitro, carro, modelo):
        self.modelo = modelo 
        self.carro = carro 
        self.quilometrosLitro = quilometrosLitro
        self.qtdeCombustivel = 0

        self.layout = [
            [sg.Text('QUAL É SEU CARRO ?')],
            [sg.Button('fusca'),sg.Button('ferrare')]
        ]
    
     def IniciarVerificacao(self):
       

    def VerificarDados():
        meuFusca = Automovel(15)
        # 15 quilometros por litro de combustivel.
        meuFusca.adicionarGasolina(20)
        # abastece com 20 litros de combustivel.
        meuFusca.andar(100)
        # anda 100 quilometros.
        meuFusca.obterGasolina()  
    def adicionarGasolina(self, quantidade):    
        self.qtdeCombustivel += float(quantidade)

    def andar(self, distancia):
        gasto = distancia / self.quilometrosLitro
        self.qtdeCombustivel -= gasto

    def obterGasolina(self):
        print (self.qtdeCombustivel)

# TESTE DA CLASSE
meuFusca = Automovel(15)
# 15 quilometros por litro de combustivel.
meuFusca.adicionarGasolina(20)
# abastece com 20 litros de combustivel.
meuFusca.andar(100)
# anda 100 quilometros.
meuFusca.obterGasolina()  

minhaferrare =Automovel (20)
minhaferrare.adicionarGasolina()
