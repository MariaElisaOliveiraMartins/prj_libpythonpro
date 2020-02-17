import requests   # instalação: (terminal):> pip install request


def buscar_avatar(usuario):
    '''
    Buscar o avatar de um usuário no Github

    param usuario: str com o nome do usuário no Github
    return : str com o link do avatar
    '''

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    print(url)
    return resp.json()['avatar_url']

'''

Substituição desse trecho do código pelo Mock

if __name__ == '__main__':
    print(buscar_avatar('MariaElisaOliveiraMartins'))

'''