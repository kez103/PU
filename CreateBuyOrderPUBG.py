import requests
import pyotp
import CABO
from time import time

CABO.CABO()

totp = pyotp.TOTP("WJIPH5QE3O6IQBA7")                # Секретный код
print("Current OTP:", totp.now())                # 30-секундный пароль
print()

api_key = 'b0aec946-4b15-4985-99fa-98e0b1b1dec4'

url = 'https://bitskins.com/api/v1/get_account_balance/?api_key=' + api_key + '&code=' + totp.now()

r = requests.get(url)

bal = float(r.json()["data"]["available_balance"])


url = 'https://loot.farm/fullpricePUBG.json'

r = requests.get(url)

parsed_string_loot = r.json()

loot_filt = []

for item in parsed_string_loot:
    if float(item["max"]) > float(item["have"]) + 3:
        loot_filt.append(item)

url = 'https://bitskins.com/api/v1/get_market_buy_orders/?api_key=b0aec946-4b15-4985-99fa-98e0b1b1dec4&code=' + totp.now() + '&market_hash_name=Jeans (Tan)&page=2,3&app_id=578080'
r = requests.get(url)

parsed_string = r.json()

d = parsed_string["data"]["overall_summary"]

while bal > 3:

    for item in loot_filt:
        
        name = item["name"]
        price = (float(item["price"]) / 100 * 0.97) * 0.66
        
        if  (3 < price < bal) and (name in d.keys()):

            if d[name] < 10:

                url = 'https://bitskins.com/api/v1/get_sales_info/?api_key=b0aec946-4b15-4985-99fa-98e0b1b1dec4&market_hash_name=' + name +'&page=1&app_id=578080&code=' + totp.now()
                r = requests.get(url)
                parsed_string = r.json()
                k = 0
                f = False
                for item1 in parsed_string["data"]["sales"]:
                    if (int(time()) - int(item1["sold_at"]) < 259200):
                        if (float(item1["price"]) <= price):
                            f = True
                        k += 1
                if k > 2 and f:

                    url = 'https://bitskins.com/api/v1/create_buy_order/?api_key=' + api_key + '&code=' + totp.now() + '&name=' + name + '&price=' + str(round(price,2)) + '&quantity=1&app_id=578080'

                    r = requests.get(url)

                    bal -= price

    # for item in loot_filt:
            
    #     name = item["name"]
    #     price = (float(item["price"]) / 100 * 0.97) * 0.66
        
    #     if  0.1 < price < bal:

    #         url = 'https://bitskins.com/api/v1/get_sales_info/?api_key=b0aec946-4b15-4985-99fa-98e0b1b1dec4&market_hash_name=' + name +'&page=1&app_id=578080&code=' + totp.now()
    #         r = requests.get(url)
    #         parsed_string = r.json()
    #         k = 0
    #         for item1 in parsed_string["data"]["sales"]:
    #             if int(time()) - int(item1["sold_at"]) < 86400:
    #                 k += 1
    #         if k > 2:

    #             url = 'https://bitskins.com/api/v1/create_buy_order/?api_key=' + api_key + '&code=' + totp.now() + '&name=' + name + '&price=' + str(round(price,2)) + '&quantity=1&app_id=578080'

    #             r = requests.get(url)

    #             bal -= price

