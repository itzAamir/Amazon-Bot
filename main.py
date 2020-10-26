from bs4 import BeautifulSoup
import requests
import json
from mailer import Mailer
import time
import os


final_product_title = ""
final_price = ""
# Function To Scrape and Parse the data from the Given URL 
def check_price(url):
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
    r = requests.get(url, headers=headers).content
    soup = BeautifulSoup(r, "html.parser")

    product_title = soup.find(id="title").get_text()
    final_product_title = product_title.strip()
    print(f"\nProduct Name: {final_product_title}")

    price = soup.find(id="priceblock_dealprice")
    # print(price)
    if price != None:
        final_price = price.get_text()[2:]
        print(f"\nPrice: {final_price}")
    else:
        final_price = "Product is Unvailable Right Now"
        print(final_price)

    mail = Mailer(email= os.environ("emailID"), password= os.environ("emailPass"))
    mail.send(receiver= os.environ("receiverEmail"), subject='Amazon Products Prices', message= f'Product Name: {final_product_title}\n\nProduct Price: {final_price}')

if __name__ == "__main__":
    while True:
        url = r"https://www.amazon.in/dp/B086WN7BK6/ref=dp_prsubs_2"
        check_price(url)
        time.sleep(60*60)
