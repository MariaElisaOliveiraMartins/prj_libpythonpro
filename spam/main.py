class EnviadorDeSpam:
    def __init__(self, sessao, enviador):
        self.sessao = sessao
        self.enviador = enviador

    def enviar_emails(self, remetente, assunto, msg):
        for usuario in self.sessao.lista_usr:
            self.enviador.enviar(remetente, usuario.email, assunto, msg)
        pass
