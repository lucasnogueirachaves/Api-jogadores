from marshmallow import Schema, fields

class TimeSchema(Schema):
    id = fields.Str(required=False)
    nome = fields.Str(required=True)
    valor_elenco = fields.Float(required=True)
    jogadores = fields.List(required=True)
    
class TimeSchemaUpdate(Schema):
    nome = fields.Str(required=False)
    valor_elenco = fields.Float(required=False)
    jogadores = fields.List(required=False)