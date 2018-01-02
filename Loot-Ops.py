import requests

apiop = '57ebc3159922645bf83cf1e127bdd3'
appID = '578080'


url = 'https://api.opskins.com/IPricing/GetAllLowestListPrices/v1/?key='\
      + apiop + '&appid=' + appID

r = requests.get(url)
sales = r.json()["response"]


url = 'https://loot.farm/fullpricePUBG.json'
r = requests.get(url)
parsed_string_loot = r.json()

with open("Loot-Ops.txt", "w") as f:
    for name in sales.keys():
        for item2 in parsed_string_loot:
            if name == item2["name"] and (item2["have"] > 0):

                dim = (float(sales[name]['price']) * 0.9 / 100 /
                       float(item2["price"]) * 100 - 1)

                if (dim >= -0.3) and (10000 > sales[name]['price'] > 100):

                    f.write(str(name.encode('utf-8')) + "  " +
                            str(sales[name]['price'] / 100) + "  " +
                            str(dim) + "\n\n")
                    break

# appID = '730'


# url = 'https://api.opskins.com/IPricing/GetAllLowestListPrices/v1/?key='\
#       + apiop + '&appid=' + appID

# r = requests.get(url)
# sales = r.json()["response"]


# url = 'https://loot.farm/fullprice.json'
# r = requests.get(url)
# parsed_string_loot = r.json()

# with open("Loot-Ops.txt", "w") as f:
#     for name in sales.keys():
#         for item2 in parsed_string_loot:
#             if name == item2["name"] and (item2["have"] > 0):

#                 dim = (float(sales[name]['price']) * 0.9 / 100 /
#                        float(item2["price"]) * 100 - 1)

#                 if (dim >= -0.3) and (10000 > sales[name]['price'] > 100):

#                     f.write(str(name.encode('utf-8')) + "  " +
#                             str(sales[name]['price'] / 100) + "  " +
#                             str(dim) + "\n\n")
#                     break
