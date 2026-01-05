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

# Atualizar jogador
@app.route("/jogador/<int:id>", methods=['PATCH'])
def atualizar_jogador(id):
    dado = request.get_json()
    
    if not dado:
        return jsonify(Mensagem = "Erro"), 400
    
    for jogador in jogadores:
        if jogador["id"] == id:
            if "nome" in dado:
                jogador["nome"] = dado["nome"]
            if "idade" in dado:
                jogador["idade"] = dado["idade"]
            if "valor" in dado:
                jogador["valor"] = dado["valor"]
            if "aposentado" in dado:
                jogador["aposentado"] = dado["aposentado"]
            if "time" in dado:
                jogador["time"] = dado["time"]
            return jsonify(Mensagem = "Jogador atualizado com sucesso", Jogador = jogador), 200
    return jsonify(Mensagem = "Jogador não encontrado"), 404

# Atualização completa
@app.route("/jogador/<int:id>", methods=['PUT'])
def atualizar(id):
    dado = request.get_json()
    if not dado:
        return jsonify(Mensagem = "Erro"), 400
    
    campos_obrigatorios = ["nome", "valor", "idade", "aposentado", "time"]
    
    for campo in campos_obrigatorios:
        if campo not in dado:
            return jsonify(Mensagem = f"O campo {campo} é obrigatório"), 400
        
    for jogador in jogadores:
        if jogador["id"] == id:
            jogador["nome"] = dado["nome"]
            jogador["idade"] = dado["idade"]
            jogador["time"] = dado["time"]
            jogador["valor"] = dado["valor"]
            jogador["aposentado"] = dado["aposentado"]
            return jsonify(Mensagem = "Jogador atualizado com sucesso", Jogador = jogador), 200
        
    return jsonify(Mensagem = "Jogador não encontrado"), 404

# Remover jogador por id
@app.route("/jogador/<int:id>", methods=['DELETE'])
def remover_jogador(id):
    jogador_removido = False
    
    for jogador in jogadores:
        if jogador["id"] == id:
            jogador_removido = True
            jogadores.remove(jogador)
            return jsonify(Mensagem = "Jogador removido com sucesso"), 200
        
    if not jogador_removido:
        return jsonify(Mensagem = "Jogador não encontrado"), 404
    
# Remover jogador por nome
@app.route("/jogador", methods=['DELETE'])
def remover_jogador_nome():
    nome = request.args.get("nome")
    jogador_removido = False
    
    if not nome:
        return jsonify(Mensagem = "Erro"), 400
    
    for jogador in jogadores:
        if jogador["nome"] == nome:
            jogador_removido = True
            jogadores.remove(jogador)
            return jsonify(Mensagem = "Jogador removido com sucesso"), 200
        
    if not jogador_removido:
        return jsonify(Mensagem = "Jogador não encontrado"), 404          

app.run()