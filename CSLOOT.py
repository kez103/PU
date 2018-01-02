import requests
import pyotp
import json
from pygame import mixer
from time import sleep

totp = pyotp.TOTP("WJIPH5QE3O6IQBA7")                # Секретный код
print("Current OTP:", totp.now())                # 30-секундный пароль
print()

mixer.init()
mixer.music.load("d:\ICQ.mp3")            # Звук

# JSON предметов на продаже
url2 = 'https://loot.farm/fullprice.json'

bitskloot_cost_filt = []

while True:
    try:
        url1 = 'https://bitskins.com/api/v1/get_price_data_for_items_on_sale/?api_key=b0aec946-4b15-4985-99fa-98e0b1b1dec4&code=' + totp.now() + '&app_id=730'
        r1 = requests.get(url1)

        parsed_string_bitsk = json.loads(r1.text)

        i = 0
        r2 = requests.get(url2)

        parsed_string_loot = json.loads(r2.text)
        bitsk_cost_filt = []

        for item in parsed_string_bitsk["data"]["items"]:
            if 10 <= float(item["lowest_price"]) <= 70:  # Фильтр по цене bits
                bitsk_cost_filt.append(parsed_string_bitsk["data"]["items"][i])

            i += 1

        loot_filt = []

        for item in parsed_string_loot:
            if item["max"] > item["have"]:
                loot_filt.append(item)

        for item in loot_filt:
            name = item["name"]
            for k in bitsk_cost_filt:
                nameBit = k.get("market_hash_name")
                if (nameBit == name):
                    dim = (float(k["lowest_price"]) / (float(item["price"]) * 0.98) * 100 - 1)
                    if (dim <= -0.31) and (k not in bitskloot_cost_filt):
                        f = open('textCSGO.txt', 'a')
                        f.write(str(round(dim, 4)) + '\n')
                        f.write(str(name.encode('utf-8')) + '\n')
                        f.write(k["lowest_price"] + '\n')
                        f.write('\n')
                        f.close()
                        bitskloot_cost_filt.append(k)

                        mixer.music.play()         # Звук
                        while mixer.music.get_busy():
                            pass
                        mixer.stop()

                        break

    except Exception as ex:
        f = open('textCSGO.txt', 'a')
        f.write(str(ex) + '\n\n')
        f.close()

    finally:
        sleep(1)


#       BUY ITEM
