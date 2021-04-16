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


class Netflix(Base):
    '''Model class for netflix table'''

    __tablename__ = 'netflix'

    id = Column(Integer(), primary_key=True)
    tipo = Column(String(255), nullable=True)
    titulo = Column(String(255), nullable=True)
    diretor = Column(String(255), nullable=True)
    elenco = Column(String(4000), nullable=True)
    pais = Column(String(255), nullable=True)
    data_lancamento = Column(DateTime(), nullable=True)
    ano_lancamento = Column(Integer(), nullable=True)
    censura = Column(String(255), nullable=True)
    duracao = Column(String(255), nullable=True)
    listado = Column(String(255), nullable=True)
    descricao = Column(String(4000), nullable=True)


class Perfil(Base):
    '''Model class for perfil table'''

    __tablename__ = 'perfil'

    survey_id = Column(String(20), primary_key=True)
    respondent_id = Column(String(20), primary_key=True)
    cnt = Column(Integer(), primary_key=True)
    question_1 = Column(String(255), nullable=True)
    question_2 = Column(String(255), nullable=True)
    question_3 = Column(String(255), nullable=True)
    question_4 = Column(String(255), nullable=True)
    question_5 = Column(String(255), nullable=True)
    question_6 = Column(String(255), nullable=True)


class Quadrante(Base):
    __tablename__ = 'quadrante'
    id = Column(Integer(), primary_key=True)
    survey_id = Column(String(20), primary_key=True)
    respondent_id = Column(String(20), primary_key=True)
    question_7 = Column(String(255), nullable=True)
    question_8 = Column(String(255), nullable=True)
    question_14 = Column(String(255), nullable=True)
    question_15 = Column(String(255), nullable=True)
    question_17 = Column(String(255), nullable=True)
    topico = Column(String(255), nullable=True)


class SurveyData(Base):
    __tablename__ = 'survey_data'
    id = Column(Integer(), primary_key=True)
    respondent = Column(String(100), nullable=True)
    question = Column(String(4000), nullable=True)
    category = Column(String(4000), nullable=True)
    answer = Column(String(4000), nullable=True)
    application = Column(String(100), nullable=True)
    survey_name = Column(String(100), nullable=True)
    load_date = Column(DateTime(), nullable=True)


class NetflixViewHistory(Base):
    __tablename__ = 'netflix_view_history'
    id = Column(Integer(), primary_key=True)
    conta = Column(String(100), nullable=True)
    perfil = Column(String(100), nullable=True)
    tipo = Column(String(20), nullable=True)
    titulo = Column(String(255), nullable=True)
    temporada = Column(String(255), nullable=True)
    episodio = Column(String(255), nullable=True)
    load_date = Column(DateTime(), nullable=True)


class Artigos(Base):
    __tablename__ = 'artigos'
    id = Column(Integer(), primary_key=True)
    titulo = Column(String(400), nullable=True)
    url = Column(String(400), nullable=True)
    data = Column(DateTime(), nullable=True)
    tag = Column(String(400), nullable=True)


class Combustivel(Base):
    __tablename__ = "combustivel"
    id = Column(Integer(), primary_key=True)
    data = Column(DateTime(), nullable=True)
    percorrida = Column(Float(), nullable=True)
    alcool = Column(Float(), nullable=True)
    gasolina = Column(Float(), nullable=True)
    valor = Column(Float(), nullable=True)
    litros = Column(Float(), nullable=True)
