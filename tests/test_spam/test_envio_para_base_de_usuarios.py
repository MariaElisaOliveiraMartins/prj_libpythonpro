import pytest
from prj_libpythonpro.spam.enviador_de_email import Enviador
from prj_libpythonpro.spam.main import EnviadorDeSpam
from prj_libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Nome do Usuário 01', email='MEOM@gmail.com'),
            Usuario(nome='Nome do Usuário 02', email='OMFCO@gmail.com')
        ],
        [
            Usuario(nome='Nome do Usuário 01', email='mariaelisa@gmail.com')
        ]
    ]
)


def test_qtde_de_spam(sessao, usuarios):
    for usrs in usuarios:
        sessao.salvar(usrs)
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails('remetente@gmail.com', 'Assunto: titulo do e-mail', 'Msg: blá-blá-blá-blá')
