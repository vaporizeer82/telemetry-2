import uuid

from dataclasses import dataclass

from app.extensions import db


@dataclass
class Track(db.Model):
    id: uuid.UUID = db.Column(db.Uuid(), primary_key=True, default=uuid.uuid4)
    track: str = db.Column(db.String, nullable=False)
