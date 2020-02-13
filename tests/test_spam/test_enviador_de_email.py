from prj_libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_rementente():
    enviador = Enviador()
    destinatarios = ['mariaelisomartins@gmail.com','OMFCO@gmail.com']
    for dest in destinatarios:
        resultado = enviador.enviar(
            'mariaelisaoliveiramartins@gmail.com',
            dest,
            'Titulo do e-mail enviado',
            'conteúdo... conteúdo... conteúdo ...'
            )
        assert dest in resultado
