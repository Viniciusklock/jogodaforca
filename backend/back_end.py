# importações
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from config import *
from modelo import Jogador

# rota para retornar os resultados
@app.route("/")
def ola():
    return "backend operante"

# curl localhost:5000/listar_resultados

@app.route("/listar_resultados")
def listar_resultados():
    try:
        # obter os resultados
        lista = db.session.query(Jogador).all()
        # converter resultado pra json
        lista_retorno = [x.json() for x in lista]
        # preparar uma parte da resposta: resultado ok
        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": lista_retorno})
        # retornar a lista de pessoas json, com resultado ok
        resposta = jsonify(meujson)
        return resposta
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})

# iniciar o backend (app.run)
with app.app_context():

    # criar o banco de dados, caso não esteja criado
    db.create_all()

    # provendo o CORS ao sistema
    CORS(app)

    # iniciar o servidor
    app.run(debug=True)