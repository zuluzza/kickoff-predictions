import requests
from bs4 import BeautifulSoup

URL = 'https://kickoff.ai/matches'
matches_page = requests.get(URL)

parsed_matches = BeautifulSoup(matches_page.content, 'html.parser')

#TODO there's show more button on the web page. This does not find the matches hidden behind import
predictions = parsed_matches.find_all("div", {"class": "prediction prediction-fixture"})

for pred in predictions:
	home_team = pred.find("div", {"class": "team-home"}).text
	away_team = pred.find("div", {"class": "team-away"}).text

	home_win = pred.find("span", {"class": "prediction-win-home"}).text
	home_win = int(home_win.strip("%"))
	tie = pred.find("span", {"class": "prediction-draw"}).text
	tie = int(tie.strip("%"))
	away_win = pred.find("span", {"class": "prediction-win-away"}).text
	away_win = int(away_win.strip("%"))

	print("{} vs {}Predicting: home {} - tie {} - away {}".format(home_team, away_team, home_win, tie, away_win))
