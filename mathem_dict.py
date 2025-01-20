import requests
from bs4 import BeautifulSoup
import json


links_for_search_answers = [
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=79&cat_id[]=90&cat_id[]=96&cat_id[]=102&cat_id[]=94&cat_id[]=111&cat_id[]=112&cat_id[]=113&cat_id[]=114&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=182&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=192&cat_id[]=193&cat_id[]=180&cat_id[]=148&cat_id[]=140&cat_id[]=178&cat_id[]=177&cat_id[]=197&cat_id[]=194&cat_id[]=144&cat_id[]=151&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=166&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=185&cat_id[]=265&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=14&cat_id[]=9&cat_id[]=10&cat_id[]=11&cat_id[]=12&cat_id[]=13&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=55&cat_id[]=60&cat_id[]=57&cat_id[]=62&cat_id[]=56&cat_id[]=61&cat_id[]=58&cat_id[]=63&cat_id[]=65&cat_id[]=59&cat_id[]=64&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=69&cat_id[]=68&cat_id[]=70&cat_id[]=183&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=71&cat_id[]=72&cat_id[]=76&cat_id[]=77&cat_id[]=73&cat_id[]=74&cat_id[]=75&cat_id[]=184&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=88&cat_id[]=84&cat_id[]=85&cat_id[]=86&cat_id[]=87&cat_id[]=89&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=267&cat_id[]=294&cat_id[]=125&cat_id[]=122&cat_id[]=272&cat_id[]=191&cat_id[]=296&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=175&cat_id[]=81&cat_id[]=83&cat_id[]=82&cat_id[]=80&cat_id[]=78&filter=all',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=79&cat_id[]=90&cat_id[]=96&cat_id[]=102&cat_id[]=94&cat_id[]=111&cat_id[]=112&cat_id[]=113&cat_id[]=114&filter=all_a',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=182&filter=all_a',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=192&cat_id[]=193&cat_id[]=180&cat_id[]=148&cat_id[]=140&cat_id[]=178&cat_id[]=177&cat_id[]=197&cat_id[]=194&cat_id[]=144&cat_id[]=151&filter=all_a',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=166&filter=all_a',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=185&cat_id[]=265&filter=all_a',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=14&cat_id[]=9&cat_id[]=10&cat_id[]=11&cat_id[]=12&cat_id[]=13&filter=all_a',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=55&cat_id[]=60&cat_id[]=57&cat_id[]=62&cat_id[]=56&cat_id[]=61&cat_id[]=58&cat_id[]=63&cat_id[]=65&cat_id[]=59&cat_id[]=64&filter=all_a',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=69&cat_id[]=68&cat_id[]=70&cat_id[]=183&filter=all_a',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=71&cat_id[]=72&cat_id[]=76&cat_id[]=77&cat_id[]=73&cat_id[]=74&cat_id[]=75&cat_id[]=184&filter=all_a',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=88&cat_id[]=84&cat_id[]=85&cat_id[]=86&cat_id[]=87&cat_id[]=89&filter=all_a',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=267&cat_id[]=294&cat_id[]=125&cat_id[]=122&cat_id[]=272&cat_id[]=191&cat_id[]=296&filter=all_a',
	'https://ege.sdamgia.ru/test?a=view_many&cat_id[]=175&cat_id[]=81&cat_id[]=83&cat_id[]=82&cat_id[]=80&cat_id[]=78&filter=all_a',
]

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

with open("mathem.json", "w") as f:
	json.dump(dct, f)
