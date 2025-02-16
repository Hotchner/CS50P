from sqlalchemy import create_engine, Column, Integer, String, Date, MetaData, ForeignKey, inspect
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///app.db')
inspector = inspect(engine)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Colaborador(Base):
    __tablename__ = 'colaboradores'

    id = Column(Integer, nullable=False, primary_key=True)
    nome = Column(String(120), nullable=False)
    dt_nascimento = Column(Date)
    idade = Column(Integer)
    id_setor = Column(Integer, ForeignKey('setores.id'))

    setor = relationship('Setor', back_populates='colaboradores')

class Setor(Base):
    __tablename__ = 'setores'

    id = Column(Integer, nullable=False, primary_key=True)
    nome = Column(String(120), nullable=False)

    colaboradores = relationship('Colaborador', back_populates='setor')

#Base.metadata.create_all(engine)

tabelas = inspector.get_table_names()

#for tabela in tabelas:
#    print(f"Tabela: {tabela}")
#    colunas = inspector.get_columns(tabela)
#    for coluna in colunas:
#        print(f" - Coluna: {coluna['name']}, Tipo: {coluna['type']}")
#    print("\n")

'''session.query(Colaborador).delete()
session.commit()'''















#Função para adicionar os Colaboradores
def add_colab(id, nome, dt_nascimento, idade, setor):
    colaborador = Colaborador(id=id, nome=nome, dt_nascimento=dt_nascimento, idade=idade, id_setor=setor)
    session.add_all([colaborador])
    session.commit()

#Função para adicionar novos Setores
def add_sector(id, name):
    setor = Setor(id=id, nome=name, )
    session.add_all([setor])
    session.commit()

#Função que lista os colaboradores
def list_colab():
    colaboradores = session.query(Colaborador).all()
    for colaborador in colaboradores:
        print(f"Setor: {colaborador.nome}")

#Função que lista os setores
def list_sector():
    setores = session.query(Setor).all()
    for setor in setores:
        print(f"Colaborador: {setor.nome}, ID: {setor.id}")

#add_colab(1, "Carolina Ferreira Costa", None, 19, 7)
#add_sector(5, "Vendas")

list_colab()
#list_sector()

