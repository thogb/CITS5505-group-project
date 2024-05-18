from marshmallow import Schema, fields

class ItemCommentNewDTO(Schema):
    message = fields.String()