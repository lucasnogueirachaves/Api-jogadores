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

