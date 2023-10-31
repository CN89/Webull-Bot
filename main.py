# Imports
from webull import paper_webull, endpoints # for real money trading, just import 'webull' instead
from retrieve import retrieve_messages
from login import webull_login
import re


# Variables
wb = paper_webull()


def main():
    webull_login()
    
    balance = wb.get_portfolio()
    
    lines = retrieve_messages('1002648699723325450')

    symbol = 'SPY'
    enteredTrade = False

    buy_pattern = r"(spy) (\d+)([cp] @(\d+\.\d+))"
    sell_pattern = r"(TP)"
    out_pattern = r"(out)", r"(Out)"

    for line in lines : 
        if re.search(buy_pattern, line) and enteredTrade == False:
            quantity = int(balance * 0.5)
            order = wb.place_order(stock=symbol.upper(), action='BUY', orderType='MKT', enforce='DAY', quant=quantity)
            print(order)
            enteredTrade = True

        if re.search(sell_pattern, line) and enteredTrade == True:
            order = wb.place_order(stock=symbol.upper(), action='BUY', orderType='MKT', enforce='DAY', quant=int(quantity * 0.5))
            print(order)
            remaining_quantity = quantity - int(quantity * 0.5)
            enteredTrade = True

        if re.search(out_pattern, line) and enteredTrade == True:
            order = wb.place_order(stock=symbol.upper(), action='BUY', orderType='MKT', enforce='DAY', quant=remaining_quantity)
            print(order)
            enteredTrade = False

main()