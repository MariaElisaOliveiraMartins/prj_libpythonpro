import pytest
from prj_libpythonpro.spam.db import Conexao


@pytest.fixture
def conexao():
    #setup
    conexao_obj = Conexao()
    yield conexao_obj
    #Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.rollback()
    sessao_obj.fechar()