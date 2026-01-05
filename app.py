from flask import Flask, request, jsonify

app = Flask(__name__)
app.json.sort_keys = False

jogadores = [
    {
        "id" : 0,
        "nome": "Lionel Messi",
        "idade": 37,
        "valor": 35000000,
        "aposentado": False,
        "time": "Inter Miami"
    },
    {
        "id" : 1,
        "nome": "Cristiano Ronaldo",
        "idade": 39,
        "valor": 15000000,
        "aposentado": False,
        "time": "Al-Nassr"
    },
    {
        "id" : 2,
        "nome": "Neymar Jr",
        "idade": 32,
        "valor": 45000000,
        "aposentado": False,
        "time": "Santos"
    },
    {
        "id" : 3,
        "nome": "Ronaldinho Gaúcho",
        "idade": 44,
        "valor": 0,
        "aposentado": True,
        "time": "Sem clube"
    },
    {
        "id" : 4,
        "nome": "Pelé",
        "idade": 82,
        "valor": 0,
        "aposentado": True,
        "time": "Sem clube"
    }
]

# GET da lista
@app.route("/jogadores", methods=['GET'])
def get_jogadores():
    return jsonify(Jogadores = jogadores)

# Busca jogador por id
@app.route("/jogador/<int:id>", methods=['GET'])
def get_jogador_id(id):
    for jogador in jogadores:
        if jogador["id"] == id:
            return jsonify(Mensagem = "Jogador encontrado com sucesso", Jogador = jogador), 200
        
    return jsonify(Mensagem = "Jogador não encontrado"), 404

# Busca jogador por nome
@app.route("/jogador", methods=['GET'])
def get_jogador_nome():
    nome = request.args.get("nome")
    
    for jogador in jogadores:
        if jogador["nome"] == nome:
            return jsonify(Mensagem = "Jogador encontrado", Jogador = jogador), 200
        
    return jsonify(Mensagem = "Jogador não encontrado"), 404

# Cadastro de jogador
@app.route("/jogador", methods=['POST'])
def cadastrar_jogador():
    jogador = request.get_json()
    
    if not jogador:
        return jsonify(Mensagem = "Erro"), 400
    if "id" not in jogador:
        return jsonify(Mensagem = "O campo 'id' é obrigatório"), 400
    if "nome" not in jogador:
        return jsonify(Mensagem = "O campo 'nome' é obrigatório"), 400
    if "aposentado" not in jogador:
        return jsonify(Mensagem = "O campo 'aposentado' é obrigatório"), 400
    
    jogadores.append(jogador)
    
    return jsonify(Mensagem = "Jogador adicionado", Jogador = jogador), 200

