from prj_libpythonpro.spam.modelos import Usuario


def test_salvar_usuarios(sessao):
    usuario = Usuario(nome='Maria Elisa')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Nome do Usuário 01'), Usuario(nome='Nome do Usuário 02')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
