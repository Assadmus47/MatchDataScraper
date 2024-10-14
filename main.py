import requests
from bs4 import BeautifulSoup
import csv

# input to enter the date of the match  
date = input("Enter the date in the format of mm/dd/yyyy: ")
page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}")

def main(page=page):
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    matches_details = []
    
    championships = soup.find_all('div', {'class': 'matchCard'})
    
    def get_matche_info(championship):
        # make sure that contetns is not empty
        if championship.contents:
            championship_title = championship.contents[1].find("h2").text.strip()
            all_matches = championship.contents[3].find_all('div', {'class': 'item finish liItem'})
            number_of_matches = len(all_matches)
            for i in range(number_of_matches): 
                #get teams names 
                team_a = all_matches[i].find('div', {'class': 'teamA'}).text.strip() 
                team_b = all_matches[i].find('div', {'class': 'teamB'}).text.strip() 
                
                #get match score 
                score = all_matches[i].find('div', {'class': 'MResult'}).find_all('span',{'class':'score'})
                score = f"{score[0].text.strip()} - {score[1].text.strip()}"
                
                #get match time
                time = all_matches[i].find('div', {'class': 'MResult'}).find_all('span',{'class':'time'}).text.strip()
                
                
                
    if championships:
        get_matche_info(championships[0])
    else:
        print("No championships found")

if __name__ == "__main__":
    main(page) 
    


