class Sessao:

    contador = 0

    lista_usr = []

    def salvar(self, usuario):
        Sessao.contador += 1
        usuario.id = Sessao.contador
        self.lista_usr.append(usuario)

    def rollback(self):
        self.lista_usr.clear()


    def fechar(self):
        pass

    def listar(self):
        return Sessao.lista_usr


class Conexao:

    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass
