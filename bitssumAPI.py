import asyncio
import websockets
import json
import time
import math
import base64
import hmac, hashlib
import urllib.parse
import requests
import datetime

list = [['fb626d26310fd6bdfcd6e91c29df24b5', '8e60d228b7f3db4475a907bea3374b1f'], #민정
       ['468bc3ed87b933e66b8909e1125abc16', '885091c0958302c8cf2c07aec080c4db'], #김윤성
       ['c934d94a198a6d9262de027fee116f35' ,'bd01259c721dcb3ab73bc3517ee6a72c'], #김재현
       ['2fb4778490491f808b858cc331f6da37', '4a3fdbaa97c2fe47cd539a569d54dbb0']] #김희상

class XCoinAPI:
    api_url = "https://api.bithumb.com"
    api_key = ""
    api_secret = ""

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def body_callback(self, buf):
        self.contents = buf

    def microtime(self, get_as_float = False):
        if get_as_float:
            return time.time()
        else:
            return '%f %d' % math.modf(time.time())

    def usecTime(self) :
        mt = self.microtime(False)
        mt_array = mt.split(" ")[:2]
        return mt_array[1] + mt_array[0][2:5]

    def xcoinApiCall(self, endpoint, rgParams):
        # 1. Api-Sign and Api-Nonce information generation.
        # 2. Request related information from the Bithumb API server.
        #
        # - nonce: it is an arbitrary number that may only be used once.
        # - api_sign: API signature information created in various combinations values.

        endpoint_item_array = {
            "endpoint" : endpoint
        }

        uri_array = dict(endpoint_item_array, **rgParams) # Concatenate the two arrays.

        str_data = urllib.parse.urlencode(uri_array)

        nonce = self.usecTime()

        data = endpoint + chr(0) + str_data + chr(0) + nonce
        utf8_data = data.encode('utf-8')

        key = self.api_secret
        utf8_key = key.encode('utf-8')

        h = hmac.new(bytes(utf8_key), utf8_data, hashlib.sha512)
        hex_output = h.hexdigest()
        utf8_hex_output = hex_output.encode('utf-8')

        api_sign = base64.b64encode(utf8_hex_output)
        utf8_api_sign = api_sign.decode('utf-8')

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            "Api-Key": self.api_key,
            "Api-Nonce": nonce,
            "Api-Sign": utf8_api_sign
        }

        url = self.api_url + endpoint

        r = requests.post(url, headers=headers, data=rgParams)
        return r.json()


def buy_limit(api, currency, price, qty):
    while True:
        try:
            seParams = {
                'endpoint' : '/trade/place',
                'order_currency' : currency,
                'payment_currency' : 'KRW',
                'units' : float(qty),
                'price' : price,
                'type' : 'bid'
            }
            result = api.xcoinApiCall(seParams['endpoint'], seParams)
            if result['status'] == '0000':
                return result['order_id']

        except Exception as e:
            print('buy limit, ', e)
            time.sleep(0.5)
            continue

def sell_market(api, currency, qty):
    cnt = 0
    while True:
        try:
            cnt = cnt + 1
            if cnt == 3 : 
                return False
            seParams = {
                'endpoint' : '/trade/market_sell',
                'order_currency' : currency,
                'payment_currency' : 'KRW',
                'units' : qty
            }
            time.sleep(0.5)
            result = api.xcoinApiCall(seParams['endpoint'],seParams)
            if result['status'] == '0000':
                return True
            else :
                #print('sell_market' , result)
                continue
        except Exception as e :
            print('sell_market , ', e)
            cnt = cnt - 1
            continue

def sell_all(api, currency):
    while True:
        try:
            seParams = {
                'endpoint' : '/info/balance',
                'currency' : currency,
            }
            result = api.xcoinApiCall(seParams['endpoint'], seParams)
            time.sleep(0.5)
            if result['status'] == '0000':
                str_currency = 'available_' + currency.lower()
                qty = float(result['data'][str_currency])
                qty = float(math.trunc(qty*10000))/10000
                #print(qty)
                seParams = {
                    'endpoint' : '/trade/market_sell',
                    'order_currency' : currency,
                    'payment_currency' : 'KRW',
                    'units' : qty
                }
                result = api.xcoinApiCall(seParams['endpoint'],seParams)
                if result['status'] == '0000':
                    return qty
                else :
                    #print('sell_all', result)
                    return 0
            else :
                print(result)
                continue
            

        except Exception as e :
            print('sell all , ', e)
            continue
def cancle_order(api, currency, order_id):
    while True:
        seParams = {
            'endpoint' : '/trade/cancel',
            'type' : 'bid',
            'order_id' : order_id,
            'order_currency' : currency,
            'payment_currency' : 'KRW'
        }
        try:
            result = api.xcoinApiCall(seParams['endpoint'], seParams)
            #print('calcel order : ', order_id)
            time.sleep(0.5)
            if result['status'] == '0000':
                #print(result)
                return True
            else :
                #print('cancle_order', result)
                #continue
                return False
        except Exception as e:
            print('cancle_order', e)
            time.sleep(0.5)
            continue
        
def start(currency, goal, qty):
    try:
        btcprice = 0
        volume = 0
    
        for connectkey, secretkey in list:
            api = XCoinAPI(connectkey, secretkey)
            volume = 0
            while True:
                if volume > goal:
                    break
                #get btc orderbook
                try:
                    url = "https://api.bithumb.com/public/orderbook/BTC_KRW"
                    headers = {"accept": "application/json"}
                    response = requests.get(url, headers=headers).text
                    response = json.loads(response)
                except Exception as e:
                    print(e)
                    time.sleep(3)
                    continue
                
                    
                btcprice = int(response['data']['bids'][0]['price'])
                
                print('orderprice : ', btcprice)
                order_id = buy_limit(api, currency, btcprice, qty)

                if sell_market(api, currency, qty):
                    volume = volume + btcprice * qty
                    print('volume : ', volume)
                    
                
                cancle_order(api, currency, order_id)
                sellqty = sell_all(api, currency)
                volume = volume + btcprice * sellqty
                print('volume : ', volume)
    except Exception as e:
        api = XCoinAPI(connectkey, secretkey)
        print(e)
        

currency = 'BTC'
goal = 600000000
qty = 0.009

start(currency, goal, qty)