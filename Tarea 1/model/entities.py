from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector
class Usuario(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    codigo = Column(Integer)
    nombre = Column(String(12))
    apellido = Column(String(12))
    password = Column(String(120))