from prj_libpythonpro.spam.db import Conexao
from prj_libpythonpro.spam.modelos import Usuario


def test_salvar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Maria Elisa')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.rollback()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Nome do Usuário 01'), Usuario(nome='Nome do Usuário 02')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.rollback()
    sessao.fechar()
    conexao.fechar()
