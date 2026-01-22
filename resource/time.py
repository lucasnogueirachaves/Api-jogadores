from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify
import uuid
from db import times
from schemas.time import TimeSchema, TimeSchemaUpdate

time_blp = Blueprint(
    "Time",
    __name__,
    description="Operações relacionadas a time"
)

@time_blp.route("/time")
class Time(MethodView):
    
    @time_blp.response(200, TimeSchema(many=True))
    def get(self):
        return times.values()
    
    @time_blp.arguments(TimeSchema)
    @time_blp.response(201, TimeSchema)
    def post(self, time_dado):
        time_id = uuid.uuid4().hex
        time_novo = {**time_dado, "id": time_id}
        times[time_id] = time_novo
        return jsonify(time_novo), 201
    
@time_blp.route("/time/<string:time_id>")
class TimeId(MethodView):
    
    @time_blp.response(200, TimeSchema)
    def get(self, time_id):
        if time_id not in times:
            abort(404, message="Time não encontrado")
        return jsonify(times[time_id]), 200
    
    @time_blp.arguments(TimeSchema)
    @time_blp.response(200, TimeSchema)
    def put(self, dados_novos, time_id):
        if time_id not in times:
            abort(404, message="Time não encontrado")
            
        if "id" in dados_novos and dados_novos["id"] != time_id:
            abort(400, message="Não é permitido alterar o id")
            
        times[time_id].update(dados_novos)
        
        return jsonify({"Time atualizado": times[time_id]}), 200
    
    @time_blp.arguments(TimeSchemaUpdate)
    @time_blp.response(200, TimeSchema)
    def patch(self, dados_parciais, time_id):
        if time_id not in times:
            abort(404, message="Time não encontrado")
            
        if not dados_parciais:
            abort(400, message="Nenhum campo enviado para atualização")
            
        times[time_id].update(dados_parciais)
        
        return jsonify({"Time tualizado": times[time_id]}), 200
    
    @time_blp.response(200, TimeSchema)
    def delete(self, time_id):
        if time_id not in times:
            abort(404, message="Time não encontrado")
        times.pop(time_id)
        
        return jsonify({"message": "Time removido com sucesso"}), 200
    
@time_blp.route("/time/<string:time_id>/valor")
class TimeValor(MethodView):
    
    @time_blp.response(200, TimeSchema)
    def get(self, time_id):
        if time_id not in times:
            abort(404, message="Time não encontrado")
        valor = sum(jogador["valor"] for jogador in times[time_id]["jogadores"])
        
        return jsonify({"message" : f"O valor do elenco é {valor}"}), 200
    
@time_blp.route("/time/ranking")
class TimeRanking(MethodView):
    
    @time_blp.response(200)
    def get(self):
        ranking = []
        
        for time in times.values():
            valor = sum(j["valor"] for j in time["jogadores"])
            ranking.append({
                "id": time["id"],
                "nome": time["nome"],
                "valor_elenco": valor
            })
            
        ranking.sort(key=lambda t: t["valor_elenco"], reverse=True)
        
        return jsonify({"message": ranking}), 200
    
@time_blp.route("/time/<string:time_id>/jogadores")
class TimeJogadores(MethodView):
    
    @time_blp.response(200)
    def get(self, time_id):
        if time_id not in times:
            abort(404, message="Time não encontrado")
            
        jogadores = []
        
        for jogador in times[time_id]["jogadores"]:
            jogadores.append({
                "nome": jogador["nome"],
                "valor": jogador["valor"]
            })
        
        jogadores.sort(key=lambda t: t["valor"], reverse=True)
        
        return jsonify({"message": jogadores}), 200