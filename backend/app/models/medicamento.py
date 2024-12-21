from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from app.database import Base

class Medicamento(Base):
    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False, index=True)
    descricao = Column(String(255), nullable=True, index=True)
    preco_custo = Column(Float, nullable=False)
    preco_venda = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
    estoque_minimo = Column(Integer, nullable=False, default=0)
    estoque_maximo = Column(Integer, nullable=True)
    lote = Column(String(50), nullable=True)
    data_fabricacao = Column(Date, nullable=True)
    data_validade = Column(Date, nullable=False)
    fornecedor = Column(String(100), nullable=True)
    contato_fornecedor = Column(String(100), nullable=True)
    ativo = Column(Boolean, default=True)
