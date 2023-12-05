from config import * 
from modelo import *

#Testar a classe Resultado criando um objeto:
a = Jogador(nome_jogador = "Joao", tentativas = 2)

db.session.add(a)
db.session.commit()

print(a)

