from unittest.mock import Mock
from prj_libpythonpro.tests import github_api

def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {"login":"MariaElisaOliveiraMartins",
                                   "id":58866392,"node_id":"MDQ6VXNlcjU4ODY2Mzky",
                                   "avatar_url":"https://avatars1.githubusercontent.com/u/58866392?v=4"
                                  }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('MariaElisaOliveiraMartins')
    assert 'https://avatars1.githubusercontent.com/u/58866392?v=4' == url
