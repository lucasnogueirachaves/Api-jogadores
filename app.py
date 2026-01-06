from flask import Flask, request, jsonify
from db import jogadores
from flask_smorest import abort
import uuid

app = Flask(__name__)
app.json.sort_keys = False

# GET da lista
@app.route("/jogadores", methods=['GET'])
def get_jogadores():
    return jsonify(Jogadores = list(jogadores.values()))

# Busca jogador por id
@app.route("/jogador/<string:id>", methods=['GET'])
def get_jogador_id(id):
    try:
        return jsonify(jogador = jogadores[id]), 200
    except:
        abort(404, message="Jogador não encontrado")

# Busca jogador por nome
@app.route("/jogador", methods=['GET'])
def get_jogador_nome():
    nome = request.args.get("nome")
    
    for jogador in jogadores.values():
        if jogador["nome"] == nome:
            return jsonify(Mensagem = "Jogador encontrado", Jogador = jogador), 200
        
    abort(404, message="Jogador não encontrado")

# Cadastro de jogador
@app.route("/jogador", methods=['POST'])
def cadastrar_jogador():
    dado_jogador = request.get_json()
    jogador_id = uuid.uuid4().hex
    
    jogador_novo = {**dado_jogador, "id": jogador_id}
    
    jogadores[jogador_id] = jogador_novo
    
    return jsonify(Mensagem = "Jogador adicionado"), 201
    

# Atualizar jogador
@app.route("/jogador/<string:id>", methods=['PATCH'])
def atualizar_jogador(id):
    dado = request.get_json()
    
    if not dado:
        abort(400, message="Dados inválidos")
    
    jogador = jogadores.get(id)

    if not jogador:
        abort(404, message="Jogador não encontrado")

    jogador.update(dado)
    
    return jsonify(Mensagem = "Jogador atualizado com sucesso", Jogador = jogador), 200

# Atualização completa
@app.route("/jogador/<string:id>", methods=['PUT'])
def atualizar_completo(id):
    dado = request.get_json()

    campos_obrigatorios = ["nome", "valor", "idade", "aposentado", "time"]

    for campo in campos_obrigatorios:
        if campo not in dado:
            abort(400, message=f"Campo {campo} é obrigatório")

    if id not in jogadores:
        abort(404, message="Jogador não encontrado")

    jogadores[id] = {
        "id": id,
        **dado
    }

    return jsonify(Mensagem="Jogador atualizado com sucesso", Jogador=jogadores[id]), 200

    
# Remover jogador por id
@app.route("/jogador/<string:id>", methods=['DELETE'])
def remover_jogador(id):
    jogador_removido = False
    
    for jogador in jogadores.values():
        if jogador["id"] == id:
            jogador_removido = True
            jogadores.pop(id)
            return jsonify(Mensagem = "Jogador removido com sucesso"), 200
        
    if not jogador_removido:
        abort(404, message="Jogador não encontrado")   

if __name__ == "__main__":
    app.run(debug=True)