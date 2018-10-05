import fme
import fmeobjects
import requests


def processFeature(feature):
    url = 'https://www.arcgis.com/sharing/generateToken'
    agol_username = feature.getAttribute('agol_username')
    agol_password = feature.getAttribute('agol_password')
    referer = feature.getAttribute('agol_referer')
    expiration_time = feature.getAttribute('agol_expiration')

    body = {
        'username': agol_username,
        'password': agol_password,
        'referer': referer,
        'request': 'gettoken',
        'f': 'json',
        'expiration': expiration_time
        }
    request = requests.post(url, headers={}, data=body).json()
    token = request[u'token']
    feature.setAttribute('token', token)
