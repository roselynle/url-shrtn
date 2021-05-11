import json

def test_home(api):
    resp = api.get('/')
    assert resp.status == '200 OK'
    assert b'Enter an https' in resp.data


def test_post_url(api):
    form_data = {'}
    resp = api.post('/', data=form_data)
    assert resp.status == '200 OK'
 