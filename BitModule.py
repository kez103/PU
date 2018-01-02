import requests
import pyotp


apiKey = 'b0aec946-4b15-4985-99fa-98e0b1b1dec4'
code = 'WJIPH5QE3O6IQBA7'


def CABO(appID):  # Cancel All Buy Orders

    totp = pyotp.TOTP(code)                # Секретный код

    url = 'https://bitskins.com/api/v1/get_active_buy_orders/?api_key='\
          + apiKey + '&code=' + totp.now() + '&app_id=' + appID

    r = requests.get(url)

    for item in r.json()["data"]["orders"]:

        name = item["market_hash_name"]

        url = 'https://bitskins.com/api/v1/cancel_all_buy_orders/?api_key='\
              + apiKey + '&code=' + totp.now() + '&market_hash_name=' + name\
              + '&app_id=' + appID

        r = requests.get(url)


def BuyItem(appID, itemName, itemPrice):

    totp = pyotp.TOTP(code)

    url = 'https://bitskins.com/api/v1/get_inventory_on_sale/?api_key='\
          + apiKey + '&code=' + totp.now() + '&page=1&app_id=' + appID\
          + '&market_hash_name=' + itemName + '&min_price=' + str(itemPrice)\
          + '&max_price=' + str(itemPrice)

    r = requests.get(url)

    parsedString = r.json()

    itemID = parsedString["data"]["items"][0]["item_id"]

    url = 'https://bitskins.com/api/v1/buy_item/?api_key=' + apiKey + '&code='\
          + totp.now() + '&item_ids=' + itemID + '&prices=' + str(itemPrice)\
          + '&app_id=' + appID

    r = requests.get(url)


def GAB():  # Get Account Ballance

    totp = pyotp.TOTP(code)

    url = 'https://bitskins.com/api/v1/get_account_balance/?api_key='\
          + apiKey + '&code=' + totp.now()

    r = requests.get(url)

    return(float(r.json()["data"]["available_balance"]))


if __name__ == "__main__":

    pass
