from marshmallow import Schema, fields

class ItemRequestSendDTO(Schema):
    amount = fields.Float()
    message = fields.String()