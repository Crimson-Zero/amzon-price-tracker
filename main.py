# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 20:34:11 2022

"""
import smtplib
from bs4 import BeautifulSoup
import requests

link = "https://www.amazon.com/dp/B08PQ2KWHS/"
headers = {
    "Accept-Language" : "lan",
    "User-Agent" : "Agent"
    
    }
response = requests.get(url=link,headers=headers)

website = response.text
soup = BeautifulSoup(website , "html.parser")

find_price = soup.find(class_="a-offscreen")
price_string = find_price.getText()

split_price=price_string.split("$")

price = float(split_price[1])

desired_price = 200

fromaddr = "from"
toaddr = "to"

password = "password"

if(price < desired_price):
    msg = f"Subject:Amazon Price Alert\n\n Hey the Pot price has reached your desired price click on the given link : {link} to buy the pot"
    server = smtplib.SMTP('smtp.any.com',587,timeout=120)
    server.ehlo()
    
    server.starttls()
    
    server.ehlo()
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
