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


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.parametros_de_envios = None
        self.qtde_emails_env = 0

    def enviar(self, remetente, destinatario, assunto, mensagem):
        self.qtde_emails_env += 1


def test_qtde_de_spam(sessao, usuarios):
    for usrs in usuarios:
        sessao.salvar(usrs)
    enviador_de_spam = EnviadorDeSpam(sessao, EnviadorMock())
    enviador_de_spam.enviar_emails('remetente_1@gmail.com', 'Assunto: titulo do e-mail 01', 'Msg: 01 - blá-blá-blá-blá')


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Maria Elisa', email='mariaelisa@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('remetente_2@gmail.com', 'Assunto: titulo do e-mail 02', 'Msg: 02 - blá-blá-blá-blá')
    assert enviador.parametros_de_envio == ('meom@gmail.com', 'mariaelisa@gmail.com',
                                            'Assunto: titulo do e-mail 02', 'Msg: 02 - blá-blá-blá-blá')
