import requests 
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

response = requests.get(URL)

print(response.status_code)
soup = BeautifulSoup(response.content,"html.parser")

first_book= soup.find("article",class_="product_pod")
title = first_book.h3.a["title"]
price = first_book.find ("p",class_= "price_color").text

rating_p_tag = first_book.p 
rating_classes = rating_p_tag["class"] 

rating = rating_classes[1]

print (f"title : {title}")
print(f"Price: {price}")
print(f"Rating : {rating} stars")

