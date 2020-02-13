from prj_libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None


def test_rementente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'mariaelisaoliveiramartins@gmail.com',
        'mariaelisaomartins@gmail.com',
        'Titulo do e-mail enviado',
        'conteúdo... conteúdo... conteúdo ...'
        )
    assert 'mariaelisaoliveiramartins@gmail.com' in resultado