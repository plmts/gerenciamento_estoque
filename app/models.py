from sqlalchemy import Column, String, Float, Integer
from database import Base

class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    valor = Column(Float, default=0)
    marca = Column(String, nullable=False)
    descricao = Column(String)
    quantidade = Column(Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id, "nome":self.nome, "valor":self.valor, "marca":self.marca, "descricao": self.descricao, "quantidade":self.quantidade}

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    cpf = Column(String, nullable=False, unique=True)
    endereco = Column(String, nullable=False)

    def to_dict(self):
        return {"id":self.id, "nome":self.nome, "email":self.email, "cpf":self.cpf, "endereco":self.endereco}