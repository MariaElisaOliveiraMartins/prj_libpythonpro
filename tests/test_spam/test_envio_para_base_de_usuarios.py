from prj_libpythonpro.spam.enviador_de_email import Enviador
from prj_libpythonpro.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails('remetente@gmail.com', 'Assunto: titulo do e-mail', 'Msg: blá-blá-blá-blá')
