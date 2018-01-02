import requests
import pyotp

totp = pyotp.TOTP("WJIPH5QE3O6IQBA7")

apiop = '57ebc3159922645bf83cf1e127bdd3'
apibit = 'b0aec946-4b15-4985-99fa-98e0b1b1dec4'
appID = '730'

url = 'https://api.opskins.com/IPricing/GetAllLowestListPrices/v1/?key='\
      + apiop + '&appid=' + appID

r = requests.get(url)
sales = r.json()["response"]
# print(sales)

url = 'https://bitskins.com/api/v1/get_price_data_for_items_on_sale/?api_key='\
      + apibit + '&code=' + totp.now() + '&app_id=' + appID

r = requests.get(url)
parsed_string = r.json()

for name in sales.keys():

    for item in parsed_string["data"]["items"]:

        if ((item["market_hash_name"] == name) and
           (10 < float(item["lowest_price"]) < 100) and
           (sales[name]['quantity'] > 10)):

            if (float(sales[name]['price'])/100 - float(item["lowest_price"]) >
               0.12*float(sales[name]['price'])/100):

                dim = (float(sales[name]['price'])/100 /
                       float(item["lowest_price"]))

                if dim > 1.2 and 'Sticker' not in name:
                    print(name + '     ' + item["lowest_price"] +
                          '     ' + str(sales[name]['price']/100) +
                          '     ' + str(sales[name]['quantity']) +
                          '     ' + str(dim))
