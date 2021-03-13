from sqlalchemy import (
    Column, String, Integer, DateTime, func, Sequence, Float, and_, Boolean, Text)
from marshmallow import ValidationError, pre_load, post_load
from database import Base


class FilmesBrasil(Base):
    '''Model class for filmes_brasil table'''

    __tablename__ = 'filmes_brasil'

    id = Column(Integer(), primary_key=True)
    ano_exibicao = Column(Integer(), nullable=True)
    titulo = Column(String(255), nullable=True)
    genero = Column(String(100), nullable=True)
    pais_produtor = Column(String(255), nullable=True)
    nacionalidade = Column(String(255), nullable=True)
    empresa_distribuidora = Column(String(255), nullable=True)
    origem_empresa_distribuidora = Column(String(255), nullable=True)
    publico_ano_exibicao = Column(Integer(), nullable=True)
    renda_ano_exibicao = Column(Float(), nullable=True)


class Brasileirao(Base):
    '''Model class for filmes_brasil table'''

    __tablename__ = 'brasileirao'

    id = Column(Integer(), primary_key=True)
    rodada = Column(String(255), nullable=True)
    data = Column(DateTime(), nullable=True)
    horario = Column(String(255), nullable=True)
    dia = Column(String(255), nullable=True)
    mandante = Column(String(255), nullable=True)
    visitante = Column(String(255), nullable=True)
    vencedor = Column(String(255), nullable=True)
    arena = Column(String(255), nullable=True)
    placar_mandante = Column(Integer(), nullable=True)
    placar_visitante = Column(Integer(), nullable=True)
    estado_mandante = Column(String(255), nullable=True)
    estado_visitante = Column(String(255), nullable=True)
    estado_vencedor = Column(String(255), nullable=True)


class BrasileiraoStats(Base):
    '''Model class for filmes_brasil table'''

    __tablename__ = 'brasileirao_stats'

    id = Column(Integer(), primary_key=True)
    rodada = Column(String(255), nullable=True)
    data = Column(DateTime(), nullable=True)
    horario = Column(String(255), nullable=True)
    dia = Column(String(255), nullable=True)
    mandante = Column(String(255), nullable=True)
    visitante = Column(String(255), nullable=True)
    vencedor = Column(String(255), nullable=True)
    arena = Column(String(255), nullable=True)
    placar_mandante = Column(Integer(), nullable=True)
    placar_visitante = Column(Integer(), nullable=True)
    estado_mandante = Column(String(255), nullable=True)
    estado_visitante = Column(String(255), nullable=True)
    estado_vencedor = Column(String(255), nullable=True)
    mandante = Column(Integer(), primary_key=True)
    chutes = Column(Integer(), nullable=True)
    chutes_gol = Column(Integer(), nullable=True)
    posse_bola = Column(Float(), nullable=True)
    passes = Column(Integer(), nullable=True)
    precisao_passe = Column(Float(), nullable=True)
    faltas = Column(Integer(), nullable=True)
    cartoes_amarelos = Column(Integer(), nullable=True)
    cartoes_vermelhos = Column(Integer(), nullable=True)
    impedimentos = Column(Integer(), nullable=True)
    escanteios = Column(Integer(), nullable=True)
