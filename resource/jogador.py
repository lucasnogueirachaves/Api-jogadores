from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify
import uuid
from db import jogadores
from schemas.jogador import JogadorSchema, JogadorSchemaUpdate

jogador_blp = Blueprint(
    "Jogador",
    __name__,
    description="Operações relacionadas a jogador"
)

@jogador_blp.route("/jogador")
class Jogador(MethodView):
    
    @jogador_blp.response(200, JogadorSchema(many=True))
    def get(self):
        return jogadores.values()
    
    @jogador_blp.arguments(JogadorSchema)
    @jogador_blp.response(201, JogadorSchema)
    def post(self, jogador_dado):
        jogador_id = uuid.uuid4().hex
        jogador_novo = {**jogador_dado, "id": jogador_id}
        jogadores[jogador_id] = jogador_novo
        return jsonify(jogador_novo), 201
    
@jogador_blp.route("/jogador/<string:jogador_id>")
class JogadorId(MethodView):
    
    @jogador_blp.response(200, JogadorSchema)
    def get(self, jogador_id):
        if jogador_id not in jogadores:
            abort(404, message="Jogador não encontrado")
        return jsonify(jogadores[jogador_id]), 200
    
    @jogador_blp.arguments(JogadorSchema)
    @jogador_blp.response(200, JogadorSchema)
    def put(self, dados_novos, jogador_id):
        if jogador_id not in jogadores:
            abort(404, message="Jogador não encontrado")
            
        if "id" in dados_novos and dados_novos["id"] != jogador_id:
            abort(400, message="Não é permitido alterar o id")
            
        jogadores[jogador_id].update(dados_novos)
        
        return jsonify({"Jogador atualizado": jogadores[jogador_id]}), 200
    
    @jogador_blp.arguments(JogadorSchemaUpdate)
    @jogador_blp.response(200, JogadorSchema)
    def patch(self, dados_parciais, jogador_id):
        if jogador_id not in jogadores:
            abort(404, message="Jogador não encontrado")
            
        if not dados_parciais:
            abort(400, message="Nenhum campo enviado para atualização")
            
        jogadores[jogador_id].update(dados_parciais)
        
        return jsonify({"Jogador tualizado": jogadores[jogador_id]}), 200
    
    @jogador_blp.response(200, JogadorSchema)
    def delete(self, jogador_id):
        if jogador_id not in jogadores:
            abort(404, message="Jogador não encontrado")
        jogadores.pop(jogador_id)
        
        return jsonify({"message": "Jogador removido com sucesso"}), 200