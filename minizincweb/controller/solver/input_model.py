from marshmallow import Schema, fields


class RequestSchema(Schema):
    parameters = fields.Dict(required=True)
