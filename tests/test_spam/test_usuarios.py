import pytest
from prj_libpythonpro.spam.db import Conexao
#from prj_libpythonpro.spam.db import Sessao
from prj_libpythonpro.spam.modelos import Usuario


@pytest.fixture
def conexao():
    #setup
    conexao_obj = Conexao()
    yield conexao_obj
    #Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao():
    sessao_obj = conexao.gerar.sessao()
    yield sessao_obj
    sessao_obj.rollback()
    sessao_obj.fechar()


def test_salvar_usuarios():
    usuario = Usuario(nome='Maria Elisa')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios():
    usuarios = [Usuario(nome='Nome do Usuário 01'), Usuario(nome='Nome do Usuário 02')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
