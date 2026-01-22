from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify
import uuid
from db import times, contratacoes, jogadores
from schemas.contratar import ContratarSchema
from resource.time import time_blp

@time_blp.route("/time/<string:time_destino_id>/contratar")
class ContratarJogador(MethodView):
    
    @time_blp.arguments(ContratarSchema)
    @time_blp.response(200, ContratarSchema)
    def post(self, dados, time_destino_id):
        contratar_id = uuid.uuid4().hex
        
        if time_destino_id not in times:
            abort(404, message="Time não encontrado")
        if not dados:
            abort(400, message="Campos não podem ser vazios")
        if dados["jogador_id"] not in jogadores:
            abort(404, message="Jogador não encontrado")
        if dados["time_origem_id"] not in times:
            abort(404, message="Time não encontrado")
        
        time_origem = times[dados["time_origem_id"]]
        time_destino = times[time_destino_id]

        jogador = next(
            (j for j in time_origem["jogadores"] if j["id"] == dados["jogador_id"]),
            None
        )

        if not jogador:
            abort(404, message="Jogador não encontrado no time de origem")

        time_origem["jogadores"].remove(jogador)

        time_destino["jogadores"].append(jogador)
        
        contratacao_nova = {**dados, "id_time_destino": time_destino_id, "id": contratar_id}
        
        return jsonify({"message": contratacao_nova}), 200
