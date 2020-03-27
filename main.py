from urllib.request import urlopen
import requests
import json
import sys





my_price=1.10314





def get_jsonparsed_data(url):
    response = requests.get(url)
    return response.json()


#import pprint
url = ("https://financialmodelingprep.com/api/v3/forex")
from time import sleep
import sys,os
from datetime import datetime as dt

def range():
    while 1:
        time=dt.now().strftime('%H:%M:%S')
        h=get_jsonparsed_data(url)
        #print(h)
        s=h['forexList']
        for i in s:
            if i['ticker'] == 'EUR/USD':
                su=str(float(i['ask']) - float(my_price))
                print('\n\n\n\nTime:%s\n_____________________\nMe:' %time + str(my_price))
                print('Cu:' + str(i['ask']) + '\n_____________________\n')
                #
                sleep(3)
                #os.system("clear")


while 1:
    try:
        range()
    except:
        print('Error')
