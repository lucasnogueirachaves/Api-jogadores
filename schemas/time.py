from marshmallow import Schema, fields
from schemas.jogador import JogadorSchema

class TimeSchema(Schema):
    id = fields.Str(required=False)
    nome = fields.Str(required=True)
    jogadores = fields.List(fields.Nested(JogadorSchema), required=True)
    
class TimeSchemaUpdate(Schema):
    nome = fields.Str(required=False)
    jogadores = fields.List(fields.Nested(JogadorSchema), required=True)