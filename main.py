from urllib.request import urlopen
import requests
import json
import sys
#from termcolor import colored



#------------------Define Point to calculate
my_price=float(0)
while 1:
    q=input('\n\n\n    Enter your point:')
    if q!="":
        my_price=float(q)
        print('\nYour current point is %.5f' %float(q))
        break
    else:
        print('Enter Your sell point')



position_type='sell'




def get_jsonparsed_data(url):
    response = requests.get(url)
    return response.json()


#import pprint
url = ("https://financialmodelingprep.com/api/v3/forex")
from time import sleep
import sys,os
from datetime import datetime as dt



def range():
    min_c=float(2)
    max_c=float(0)
    while 1:
        global n_num
        n_num += 1
        time=dt.now().strftime('%H:%M:%S')
        h=get_jsonparsed_data(url)
        #print(h)
        s=h['forexList']
        for i in s:
            if i['ticker'] == 'EUR/USD':
                su=str(float(i['ask']) - float(my_price))
                if position_type=="sell":
                    ww="\n" + str(float(my_price)-float(i['ask']))[0:7]
                print('\n\n\n\nTime:%s\n_____________________\nMe:' %time + str(my_price))
                print('Cu:' + str(i['ask']) + ww + '\n_____________________\n')
                #
                #
                #os.system("clear")
                global avrg
                avrg +=float(i['ask'])
                if (float(i['ask'])) > float(max_c):
                    max_c=float(i['ask'])
                if (float(i['ask'])) < float(min_c):
                    min_c=float(i['ask'])
                #if min_max ==5:
                #
                suum=float(avrg / n_num)
                print("\nMAX: " + str(max_c) + " - MIN: " + str(min_c) + " - Avr: " + "%.5f" % suum)
                #print(n_num)
                sleep(5)


n_num=0
avrg=float(0)
while 1:
    try:
        range()
    except:
        print('Error')
