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
