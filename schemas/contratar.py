from marshmallow import Schema, fields

class ContratarSchema(Schema):
    id = fields.Str(required=False)
    jogador_id = fields.Str(required=True)
    time_origem_id = fields.Str(required=True)