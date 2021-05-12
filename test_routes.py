import json


def test_home(api):
    resp = api.get('/') 
    print(resp.data)
    assert resp.status == '200 OK'

def test_display_short_url(api):
    resp = api.get("/display/test1")
    assert resp.status_code == 200
    assert b'Here is your shortened URL:' in resp.data


def test_404_handling(api):
    resp = api.get('/tgy')
    assert resp.status == '404 NOT FOUND'
    assert b'You seem to be a bit lost!' in resp.data


def test_405_handling(api):
    resp = api.post('/tgy')
    assert resp.status == '405 METHOD NOT ALLOWED'
    assert b'That\'s Forbidden!' in resp.data

# def test_post_url(api):
#     form = {'url':'https://stackoverflow.com'}
#     resp = api.post('/', data=form)
#     assert resp.status == '200 OK'



# def test_short_url(api):
#     resp = api.get("/dii")
#     assert resp.status_code == 200

    

 