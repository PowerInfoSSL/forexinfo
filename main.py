#!/usr/bin/python3
import requests
from time import sleep
from datetime import datetime as dt
import os

my_price = 1.10314
currency_pair = 'EUR/USD'

api_v3_forex_url = "https://financialmodelingprep.com/api/v3/forex"

def get_jsonparsed_data(url):
    response = requests.get(url)
    return response.json()

def range():
    while True:
        time = dt.now().strftime('%H:%M:%S')
        try:
            result_json = get_jsonparsed_data(api_v3_forex_url)
            os.system('clear')
            forex_list = result_json['forexList']
            for element in forex_list:
                if element['ticker'] == currency_pair:
                    subtraction_result = str(float(element['ask']) - my_price)
                    print('\n\n\n\nTime:%s\n_____________________\nMe:' %time + str(my_price))
                    #print("subtraction:"+subtraction_result)
                    print('Cu:' + str(element['ask']) + '\n_____________________\n')
        except Exception as e:
            print (str(e))
        sleep(3)

if __name__ == '__main__':
    range()
