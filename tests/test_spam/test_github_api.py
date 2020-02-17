from prj_libpythonpro.tests import github_api

def test_buscar_avatar():
    url = github_api.buscar_avatar('MariaElisaOliveiraMartins')
    assert 'https://avatars1.githubusercontent.com/u/58866392?v=4' == url
