import requests


# Collect sushi restaurants in the Warsaw
def get_rest_dict(id_to_rest=True):
    url = 'https://deliveryuser.live.boltsvc.net/eaterWeb/providersIdentifiers/byCityId'
    params = {
        'city_id': '307',
        'tag_id': '6',
        'version': 'FW.0.17.1',
        'deviceId': 'server',
        'deviceType': 'web',
        'device_name': 'UNSET',
        'device_os_version': 'Google Inc.',
        'language': 'pl-PL'
    }

    response = requests.get(url, params=params)

    rest_id = {}
    # If id_to_rest == True => dictionary keys are id's of the restaurants (12737: 'SushiDeli', 2649: 'Sana Sushi')
    # Else keys are the names of the restaurants ('SushiDeli': 12737, 'Sana Sushi': 2649)
    if id_to_rest:
        for i in response.json()['data']['providers']:
            rest_id[i['id']] = i['name']['en-US']
    else:
        for i in response.json()['data']['providers']:
            rest_id[i['name']['en-US']] = i['id']
    return rest_id
