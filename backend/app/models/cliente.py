from sqlalchemy import Column, Integer, String, Boolean, Date
from app.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    telefone = Column(String(20), nullable=True)
    endereco = Column(String(255), nullable=True)
    ativo = Column(Boolean, default=True)
    tipo_pessoa = Column(String(10), nullable=False, default="Física")  
    cpf = Column(String(11), unique=True, nullable=True)  
    cnpj = Column(String(14), unique=True, nullable=True)  
    inscricao_estadual = Column(String(20), nullable=True) 
    data_cadastro = Column(Date, nullable=True)  
    observacoes = Column(String(500), nullable=True)  
