from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = "https://in.tradingview.com/markets/stocks-india/market-movers-gainers/"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("tr",{"class":"tv-data-table__row tv-data-table__stroke tv-screener-table__result-row"})
count = 0

filename = "topgain.csv"
f = open(filename,"w")
headers = "company,Close_val,Perc_inc,Stockval_change,Market_opinion,Vol_trade,Marketcap \n"
f.write(headers)

for container in containers:
    count = count + 1

    if count == 11:
        break
    else:
        values = container.find_all("td")

        i=0
        for value in values:
            i=i+1

            if i==1:
                company = value.span.text.strip()
                print("company " + value.span.text.strip())

            if i==2:
                Close_val = value.text.strip()
                print("Closing Value: " + value.text.strip())

            if i==3:
                Perc_inc = value.text.strip()
                print("Perc increase: " + value.text.strip())

            if i==4:
                Stockval_change = value.text.strip()
                print("Val Changed: " + value.text.strip())

            if i==5:
                Market_opinion = value.text.strip()
                print("Buy Or Sell: " + value.text.strip())

            if i==6:
                Vol_trade = value.text.strip()
                print("Vol Traded: " + value.text.strip())

            if i==7:
                Marketcap = value.text.strip()
                print("Market Capital: " + value.text.strip() + "\n")



    f.write(company + "," + Close_val + "," + Perc_inc + "," + Stockval_change + "," + Market_opinion + "," + Vol_trade + ","  + Marketcap + "\n")
f.close()

























