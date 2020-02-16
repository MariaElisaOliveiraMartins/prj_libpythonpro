class Enviador():
    def __init__(self):
        self.qtde_emails_env = 0

    def enviar(self, remetente, destinatario, assunto, mensagem):
        if '@' not in destinatario:
            raise EmailInvalido (f' Destinatário Invalido : {destinatario} ')
        self.qtde_emails_env += 1
        return destinatario



class EmailInvalido(Exception):
    pass
