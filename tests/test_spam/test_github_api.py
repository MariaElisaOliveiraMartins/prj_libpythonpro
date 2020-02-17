import pytest
from unittest.mock import Mock
from prj_libpythonpro.tests import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = "https://avatars1.githubusercontent.com/u/58866392?v=4"
    resp_mock.json.return_value = {"login": "MariaElisaOliveiraMartins",
                                   "id": 58866392, "node_id": "MDQ6VXNlcjU4ODY2Mzky",
                                   "avatar_url": url
                                   }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original



def test_buscar_avatar(avatar_url): #teste unitário (isolado no ambiente local)
    url = github_api.buscar_avatar('MariaElisaOliveiraMartins')
    assert avatar_url == url



def test_integrado_buscar_avatar(): #teste integrado (acesso ao ambiente externo)

    url = github_api.buscar_avatar('MariaElisaOliveiraMartins')
    assert 'https://avatars1.githubusercontent.com/u/58866392?v=4' == url
