import requests
import html5lib
from bs4 import BeautifulSoup
import time

def bse_scraper(bse_code):
    url=f"https://www.marketwatch.com/investing/Stock/{bse_code}?countryCode=IN"

    t1=time.time()
    r=requests.get(url)
    soup=BeautifulSoup(r.content, "html.parser")

    for tag in soup.find_all("meta"):
        if tag.get("name",None)=="name":
            name=tag.get("content",None)
        if tag.get("name",None)=="price":
            price=tag.get("content", None)
        if tag.get("name",None)=="priceChange":
            priceChange=tag.get("content", None)
        if tag.get("name",None)=="priceChangePercent":
            priceChangePercent=tag.get("content", None)
        if tag.get("name",None)=="quoteTime":
            quoteTime=tag.get("content", None)
        
    t2=time.time()

    print("Security Exchange:","BSE")
    print("Security name:",name)
    print("Security price:",price)
    print("Data fetched at:",quoteTime)
    print("Price change (absolute):",priceChange)
    print("Price change (percentage):",priceChangePercent)

    

    print("Time taken to fetch the data (in seconds):",round(t2-t1,4))

def nse_scraper(nse_code):
    url=f"https://www.marketwatch.com/investing/Stock/{nse_code}?countryCode=IN"

    t1=time.time()
    r=requests.get(url)
    soup=BeautifulSoup(r.content, "html.parser")

    for tag in soup.find_all("meta"):
        if tag.get("name",None)=="name":
            name=tag.get("content",None)
        if tag.get("name",None)=="price":
            price=tag.get("content", None)
        if tag.get("name",None)=="priceChange":
            priceChange=tag.get("content", None)
        if tag.get("name",None)=="priceChangePercent":
            priceChangePercent=tag.get("content", None)
        if tag.get("name",None)=="quoteTime":
            quoteTime=tag.get("content", None)
        
    t2=time.time()

    print("Security Exchange:","NSE")
    print("Security name:",name)
    print("Security price:",price)
    print("Data fetched at:",quoteTime)
    print("Price change (absolute):",priceChange)
    print("Price change (percentage):",priceChangePercent)

    

    print("Time taken to fetch the data (in seconds):",round(t2-t1,4))


#-----test-----
bse_code='539300'
nse_code="AIROLAM"
bse_scraper(bse_code)
print("-"*40)
nse_scraper(nse_code)
#--------------