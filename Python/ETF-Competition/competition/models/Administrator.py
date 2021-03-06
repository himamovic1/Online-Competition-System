from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from competition import db, Permission
from competition.models.Associations import Ownership
from competition.models.Role import Role
from competition.models.User import User


class Administrator(User):
    __tablename__ = 'administrator'

    user_id = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    position = db.Column(db.String(255), nullable=False)
    competitions = relationship("Competition", secondary=Ownership, backref='administrator')

    __mapper_args__ = {
        'polymorphic_identity': 'administrator',
    }

    def __init__(self, name, surname, email, position):
        super(Administrator, self).__init__(name, surname, email, 'administrator')
        self.position = position
        self.role = Role.query.filter_by(permissions=Permission.FULL_ACCESS).first()

    def is_administrator(self):
        return True
