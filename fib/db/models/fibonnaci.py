from ..db import db


class Fibonnacci(db.Document):
    request = db.IntField(required=True)
    response = db.ListField(required=True)
