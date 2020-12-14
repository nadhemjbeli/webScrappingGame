#http://quotes.toscrape.com
import requests
from bs4 import BeautifulSoup
from csv import writer
from random import choice
all_quotes=[]
base_url="http://quotes.toscrape.com"
url = "/page/1"


with open ("article_data.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["articles"])
    while url:
        response = requests.get(f"{base_url}{url}")
        print(f"now scraping {base_url}{url} ...")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            
            all_quotes.append({
                "text":quote.find(class_="text").get_text(),
                "author":quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })
        

        next_btn= soup.find(class_="next")
        
        if next_btn:
            url = next_btn.find("a")["href"] 
        else:
            url=None
        
quote =choice(all_quotes)
remaining_quesses = 4
print("Here is a quote")
print(quote["text"])
print(quote["author"])
guess=""
while guess.lower() != quote["author"].lower() and remaining_quesses> 0:
    guess=input(f"who said this quote ? Gesses remaining {remaining_quesses}\n")
    remaining_quesses-=1
print("AFTER WHILE LOOP")