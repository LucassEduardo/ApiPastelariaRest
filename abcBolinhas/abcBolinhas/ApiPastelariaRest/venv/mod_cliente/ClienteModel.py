import db
from sqlalchemy import Column, VARCHAR, Integer

class ClienteDB(db.Base):
    __tablename__ = 'tb_cliente'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    cpf = Column(VARCHAR(11), unique=True, nullable=False)
    telefone = Column(VARCHAR(11))
    compra_fiado = Column(Integer)
    dia_fiado = Column(Integer)
    senha = Column(VARCHAR(200))
    
    def __init__(self, id_cliente, nome, cpf, telefone, compra_fiado, dia_fiado, senha):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.compra_fiado = compra_fiado
        self.dia_fiado = dia_fiado
        self.senha = senha
