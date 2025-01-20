import requests
from bs4 import BeautifulSoup
import json


with open('./all_tasks.txt', encoding="utf-8") as f:
	all_tasks = " ".join(list(f.readlines()))

all_tasks = all_tasks.replace("&shy", '').replace(";\xad", "").replace("\xad", "")

soup = BeautifulSoup(all_tasks, 'html.parser')

themes = soup.find_all(name='div', attrs={"class": "Theme nobg"})
links_for_search_answers = []
for theme in themes[:26]:
  links_for_search_answers.append(
		f"https://rus-ege.sdamgia.ru{theme.findChild(name='a', attrs={'class': 'Theme-link'}, recursive=False)['href']}"
	)


dct = {}

for link in links_for_search_answers:
	r = requests.get(link)
	request_text = r.text.replace("&shy", '').replace(";\xad", "").replace("\xad", "")
	soup_reponses = BeautifulSoup(request_text, 'html.parser')

	maindiv_answers = soup_reponses.find_all(name="div", attrs={"class": "prob_maindiv"})

	for maindiv_answer in maindiv_answers:

		maindiv_answer = maindiv_answer.parent
		divs = maindiv_answer.find_all(name="div", attrs={"class": "pbody"})
		for answer in divs:
			if answer.has_attr('id'):
				answer_id = answer['id']
				break
		answer_div = maindiv_answer.find(name="div", attrs={"class": "answer"})

		if not answer_div:
			continue

		ans_text = answer_div.get_text()
		# print(f"{answer_id}: {ans_text[ans_text.rfind(': ') + 2:]}")
		dct[answer_id] = ans_text[ans_text.rfind(': ') + 2:]

with open("rus.json", "w") as f:
	json.dump(dct, f)
