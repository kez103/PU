import requests


apiop = '57ebc3159922645bf83cf1e127bdd3'


def BuyItem(appID, itemName, itemPrice):

    url = 'https://api.opskins.com/ISales/Search/v1/?key=' + apiop\
        + '&app=' + appID + '_2' + '&search=' + itemName\
        + '&min=' + itemPrice + '&max=' + itemPrice

    r = requests.get(url)
    parsed_string = r.json()
    print(parsed_string)
