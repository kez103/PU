import requests

apiop = '57ebc3159922645bf83cf1e127bdd3'
appID = '578080'


url = 'https://api.opskins.com/IPricing/GetAllLowestListPrices/v1/?key='\
      + apiop + '&appid=' + appID

r = requests.get(url)
sales = r.json()["response"]


url = 'https://loot.farm/fullprice.json'
r = requests.get(url)
parsed_string_loot = r.json()

with open("Ops-Loot.txt", "w") as f:
    for name in sales.keys():
        for item in parsed_string_loot:
            if name == item["name"] and (item["max"] > item["have"]):

                dim = (float(sales[name]['price']) / 100 /
                       (float(item["price"]) * 0.97) * 100 - 1)

                if (dim <= -0.32) and (sales[name]['price'] > 30):

                    itemPrice = float(sales[name]['price']) / 100

                    url = 'https://api.opskins.com/ISales/Search/v1/?key=' + apiop\
                        + '&app=' + appID + '_2' + '&search_item=' + name\
                        + '&min=' + str(itemPrice) + '&max=' + str(itemPrice)

                    r = requests.get(url)
                    parsed_string = r.json()
                    # print(parsed_string)
                    # print()

                    f.write(str(name.encode('utf-8')) + "  " +
                            str(sales[name]['price'] / 100) + "  " +
                            str(dim) + "\n\n")
                    break

# Buy Item
