import requests
from bs4 import BeautifulSoup
import csv

date = input("Enter the date in the format of mm/dd/yyyy: ")
page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}")

def main(page=page):
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    matches_details = []
    
    championships = soup.find_all('div', {'class': 'matchCard'})
    
    def get_matche_info(championship):
        if championship.contents:
            championship_title = championship.contents[1].find("h2").text.strip()
            all_matches = championship.contents[3].find_all('div', {'class': 'item finish liItem'})
            number_of_matches = len(all_matches)
            print(number_of_matches)   
    if championships:
        get_matche_info(championships[0])
    else:
        print("No championships found")

if __name__ == "__main__":
    main(page) 
    


