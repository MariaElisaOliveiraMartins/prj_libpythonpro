import pytest
from prj_libpythonpro.spam.db import Conexao


@pytest.fixture
def conexao():
    conexao_obj = Conexao()  # Setup
    yield conexao_obj
    conexao_obj.fechar()  # Teardown


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.rollback()
    sessao_obj.fechar()
