class Enviador():

    def enviar(self, remetente, destinatario, assunto, mensagem):
        if '@' not in destinatario:
            raise EmailInvalido (f' Destinatário Invalido : {destinatario} ')
        return destinatario


class EmailInvalido(Exception):
    pass
