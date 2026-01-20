from marshmallow import Schema, fields

class JogadorSchema(Schema):
    id = fields.Str(required=False)
    nome = fields.Str(required=True)
    idade = fields.Int(required=True)
    time = fields.Str(required=True)
    valor = fields.Float(required=True)

class JogadorSchemaUpdate(Schema):
    nome = fields.Str(required=False)
    idade = fields.Int(required=False)
    time = fields.Str(required=False)
    valor = fields.Float(required=False)