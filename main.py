from kickoff_prediction import groups, predict_group
from veikkaus_selenium import get_veikkaus_odds
from colorama import Fore
from colorama import Style
# check premier league
predictions = predict_group("27")
odds = get_veikkaus_odds()

print(predictions)
print("########################")
print(odds)

mappings = {"Wolverhampton" : "Wolves",
			"Burnley FC" : "Burnley",
			"Norwich City" : "Norwich",
			"Manchester United" : "Man United",
			"Leeds Utd" : "Leeds"}

for game_prediction in predictions:
	if game_prediction[0] in mappings:
		game_prediction[0] = mappings[game_prediction[0]]
	if game_prediction[1] in mappings:
		game_prediction[1] = mappings[game_prediction[1]]

	for game_odds in odds:
		if game_odds[0] in mappings:
			game_odds[0] = mappings[game_odds[0]]
		if game_odds[1] in mappings:
			game_odds[1] = mappings[game_odds[1]]

		if game_prediction[0] == game_odds[0] and game_prediction[1] == game_odds[1]:
			bettable = game_odds[2] > 1.1 * game_prediction[2] or game_odds[3] > 1.1 * game_prediction[3] or game_odds[4] > 1.1 * game_prediction[4]
			color = Fore.GREEN if bettable else Fore.RED
			print(f"{color}{game_prediction[0]} vs {game_prediction[1]}: {game_odds[2]}-{game_odds[3]}-{game_odds[4]} (prediction {game_prediction[2]}-{game_prediction[3]}-{game_prediction[4]}{Style.RESET_ALL})")
