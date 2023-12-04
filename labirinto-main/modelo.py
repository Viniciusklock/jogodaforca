from config import *

# Aqui vão as classes persistentes, nesse caso só a Resultado, a única classe que vira uma tabela 
class Resultado (db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nome_jogador = db.Column(db.Text) 
    tentativas = db.Column(db.Integer)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'(id={self.id}) {self.nome_jogador}, '+\
               f'{self.tentativas}'
    
    # expressar a classe em formato json
    def json(self):
        return {
            "nome": self.nome_jogador,
            "n_movimentos": self.tentativas
        }

