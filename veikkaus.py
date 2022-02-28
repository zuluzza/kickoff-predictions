import requests
from bs4 import BeautifulSoup

URL = 'https://www.veikkaus.fi/fi/pitkaveto?sportId=1&selectedLeagues=1-Valioliiga,Serie%20A,Bundesliiga,Ligue%201,LaLiga'
betting_odds_page = requests.get(URL)

parsed_odds = BeautifulSoup(betting_odds_page.content, 'html.parser')
print(parsed_odds)
all_odds = parsed_odds.find_all("div", {"class": "sports-events"})
print(all_odds)
for match in all_odds:
    print("new match!")
    teams = match.find("div", {"class": "event-title bold"}).text.split
    if len(teams) != 2:
        print("failed to retrive both teams")
        for team in teams:
            print(team)
    
    match_odds = match.find("div", {"class": "event-title bold"}).text.split

    print("new match_odds!")
    odds = match_odds.find_all("span", {"class": "odds"})

    print("new odds!")
    if len(odds) != 3:
        print("failed to retrieve correct number of odds")
        continue

    home_win = odds[0].text
    tie = odds[1].text
    away_win = odds[2].text
    
    print("{} vs {}odds: home {} - tie {} - away {}".format(teams[0], teams[1], home_win, tie, away_win))
