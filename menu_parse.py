import requests
import restaurants_parse


# Collect menus of the restaurants
def get_menu():
    result = []
    rest_dict = restaurants_parse.get_rest_dict()
    # Get restaurants list
    rest_list = rest_dict.keys()
    for restaurant in rest_list:
        url = f"https://deliveryuser.live.boltsvc.net/deliveryClient/public/getMenuCategories?provider_id={restaurant}&version=FW.0.17.1&deviceId=server&deviceType=web&device_name=UNKNOWN&device_os_version=Google+Inc.&language=pl-PL"
        resp = requests.get(url)
        print(rest_dict[restaurant])
        if resp.status_code == 200:
            for i in resp.json()['data']['items'].values():
                i['restaurant'] = rest_dict[restaurant]
                result.append(i)
    return result
