import pytest
from prj_libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize('destinatario',
                         ['mariaelisomartins@gmail.com', 'OMFCO@gmail.com'])
def test_dest(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        'mariaelisaoliveiramartins@gmail.com',
        destinatario,
        'Titulo do e-mail enviado',
        'conteúdo... conteúdo... conteúdo ...'
        )
    assert destinatario in resultado


@pytest.mark.parametrize('destinatario',
                         ['', 'OMFCOgmail.com'])
def test_dest_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            'mariaelisaoliveiramartins@gmail.com',
            destinatario,
            'Titulo do e-mail enviado',
            'conteúdo... conteúdo... conteúdo ...'
            )
        assert destinatario in resultado
