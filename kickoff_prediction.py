import requests
from bs4 import BeautifulSoup

groups = ["29", "31", "35", "33", "27"]

def predictionString2Odds(str):
	return 1.0 / (float(str.strip("%")) / 100)

URL = 'https://kickoff.ai/matches'

def predict_group(group_id):
	matches_page = requests.get(URL + "/" + group_id)

	parsed_matches = BeautifulSoup(matches_page.content, 'html.parser')

	#TODO there's show more button on the web page. This does not find the matches hidden behind it
	predictions = parsed_matches.find_all("div", {"class": "prediction prediction-fixture"})

	results = []
	for pred in predictions:
		home_team = pred.find("div", {"class": "team-home"}).text.replace('\n', '')
		away_team = pred.find("div", {"class": "team-away"}).text.replace('\n', '')

		home_win = pred.find("span", {"class": "prediction-win-home"}).text
		home_win = predictionString2Odds(home_win)
		tie = pred.find("span", {"class": "prediction-draw"}).text
		tie = predictionString2Odds(tie)
		away_win = pred.find("span", {"class": "prediction-win-away"}).text
		away_win = predictionString2Odds(away_win)

		#print("{} vs {}: predicted odds: home {} - tie {} - away {}".format(home_team.strip(), away_team.strip(), home_win, tie, away_win))
		results.append([home_team, away_team, home_win, tie, away_win])

	return results
