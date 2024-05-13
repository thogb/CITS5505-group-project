from marshmallow import Schema, fields

class ItemRequestRespondDTO(Schema):
    accepted = fields.Boolean()
    message = fields.String()