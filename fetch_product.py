"""
Copyright (c) 2024 Tomi Bilcu. All rights reserved.

This work is licensed under the terms of the MIT license.  
For a copy, see LICENSE.txt.
"""

import requests
from bs4 import BeautifulSoup


def fetch_product(barcode):

    link = f"https://www.barcodespider.com/{barcode}" 

    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    r = requests.get(link, headers = headers)


    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "lxml")

        product_name = soup.find_all('h2')

        return product_name[1].text
    
    else:
        return f"Couldn't find product with code: {barcode}"


# for testing
if __name__ == "__main__":
    print( fetch_product('9781617292231') )