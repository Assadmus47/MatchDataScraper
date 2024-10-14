import requests
from bs4 import BeautifulSoup
import csv


date = input("Enter the date in the format of mm/dd/yyyy: ")
page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}")

def main(page=page):
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    matches_details = []
    
    championship = soup.find_all('div', {'class': 'matchCard'})
    
   
 


if __name__ == "__main__":
    main(page)    
    


