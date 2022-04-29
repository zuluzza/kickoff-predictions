from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.maximize_window()
URL = 'https://www.veikkaus.fi/fi/pitkaveto'
browser.get(URL)

#accept all cookies to reveal the page behind the popup
accept_cookies_button = browser.find_element(by=By.XPATH, value="//*[starts-with(@class, 'all-cookies button')]")
accept_cookies_button.click()

time.sleep(5)

#select premier league games
football_expand = browser.find_element(by=By.XPATH, value="//*[starts-with(@aria-label, 'Jalkapallo')]")
football_expand.click()
time.sleep(2)
england_expand = browser.find_element(by=By.XPATH, value="//*[starts-with(@aria-label, 'Englanti')]")
england_expand.click()
time.sleep(2)
premier_league_expand = browser.find_element(by=By.XPATH, value="//*[starts-with(@for, 'Valioliiga')]/..")
premier_league_expand.click()

time.sleep(10)

games = browser.find_elements(by=By.CLASS_NAME, value="subpage-game-row")

for game in games:
	info = game.find_element(by=By.XPATH, value=".//div[@class='gameinfo-teams']").get_attribute("innerHTML")
	info = BeautifulSoup(info, 'html.parser')
	home_team = info.find("span", {"class": "gameinfo-teams-team gameinfo-teams-team--home"}).text
	away_team = info.find("span", {"class": "gameinfo-teams-team gameinfo-teams-team--away"}).text

	odds = game.find_elements(by=By.XPATH, value=".//*[starts-with(@class, 'bet-selection-button')]")

	home_win = BeautifulSoup(odds[0].get_attribute("innerHTML"), 'html.parser').find("span").text
	tie = BeautifulSoup(odds[1].get_attribute("innerHTML"), 'html.parser').find("span").text
	away_win = BeautifulSoup(odds[2].get_attribute("innerHTML"), 'html.parser').find("span").text

	print(f"{home_team} vs {away_team}: {home_win}-{tie}-{away_win}")

browser.quit()