import pytest
from unittest.mock import Mock
from prj_libpythonpro.spam.main import EnviadorDeSpam
from prj_libpythonpro.spam.modelos import Usuario

'''

Essr trecho do código foi substituido pelo Mock:

class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.parametros_de_envios = None
        self.qtde_emails_env = 0

    def enviar(self, remetente, destinatario, assunto, mensagem):
        self.parametros_de_envios = (remetente, destinatario, assunto, mensagem)
        self.qtde_emails_env += 1

'''


@pytest.mark.parametrize(
    "lst_usuarios",
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


def test_qtde_de_spam(sessao, lst_usuarios):
    for user in lst_usuarios:
        sessao.salvar(user)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('remetente_1@gmail.com', 'Assunto: titulo do e-mail 01', 'Msg: 01 - blá-blá-blá-blá')
    contador = enviador.enviar.call_count
    assert len(lst_usuarios) == contador


def test_parametros_de_spam(sessao):
    user = Usuario(nome='Maria Elisa', email='mariaelisa@gmail.com')
    sessao.salvar(user)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails('remetente_2@gmail.com', 'Assunto: titulo do e-mail 02', 'Msg: 02 - blá-blá-blá-blá')
    enviador.enviar.assert_called_once_with('remetente_2@gmail.com', 'mariaelisa@gmail.com',
                                          'Assunto: titulo do e-mail 02', 'Msg: 02 - blá-blá-blá-blá')
