from config import * 
from modelo import *

#Testar a classe Resultado criando um objeto:
a = Resultado(nome_jogador = "Helena", tentativas = 2)

db.session.add(a)
db.session.commit()

print(a)

