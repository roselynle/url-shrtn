import json

def test_home(api):
    resp = api.get('/')
    assert resp.status == '200 OK'
    assert b'Enter your URL' in resp.data


# def test_post_url(api):
#     form_data = {'}
#     resp = api.post('/', data=form_data)
#     assert resp.status == '200 OK'



def test_404_handling(api):
    resp = api.get('/tgy')
    assert resp.status == '404 NOT FOUND'


def test_405_handling(api):
    resp = api.post('/tgy')
    assert resp.status == '405 METHOD NOT ALLOWED'

    

 