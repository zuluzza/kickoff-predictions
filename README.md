# kickoff-predictions

A web scraping script that gets football predictions by artificial intelligence from http://kickoff.ai/ and converts the predictions to betting odds. Provided betting odds are compared to actual odds from http://veikkaus.fi (Finnish betting provider). If any of the odds from veikkaus are better than predicted by 10% safety marging, the line of the game is colorized green, otherwise red.

## Install dependencies:
pip install requests

pip install beautifulsoup4

pip install selenium

pip install webdriver-manager

Note: also requires installed chrome and chromedriver on your machine

## running
python main.py

#### Next steps
1. compare predictions and results to determine if articial intelligence beats betting market
2. ~~make a web scraper for booker's betting odds~~
3. combine predictions and betting odds to propose winning bets
4. recreate own AI from papers in http://kickoff.ai/
5. expand to cover more leagues
