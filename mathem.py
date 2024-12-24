from bs4 import BeautifulSoup
import json


with open('./input.txt', encoding="utf-8") as f:
	text = " ".join(list(f.readlines()))
	text = text.replace("&shy", '').replace(";\xad", "").replace("\xad", "")

soup = BeautifulSoup(text, 'html.parser')

all_divs = soup.find_all(name="div", attrs={"class": "pbody"})
tasks = []
for div in all_divs:
	tasks.append(div)
print(len(tasks))

base_url = "https://ege.sdamgia.ru/search"

k = 1

dct = json.load(open('mathem.json', 'r'))

for task in tasks:
	task_id = BeautifulSoup(str(task), 'html.parser').find(attrs={"class": "pbody"})['id']
	print(str(k) + ')', dct[task_id])
	k += 1


	# usable_task = task.get_text()[:200]
	# mx_ind_znak = max(usable_task.rfind(" "),
	# 								 usable_task.rfind("."),
	# 								 usable_task.rfind(","),
	# 								 usable_task.rfind("?"))
	# usable_task = usable_task[:mx_ind_znak]

	# n_page = 1
	# ans = []
	# while len(ans) == 0:
	# 	params = {"search": usable_task, "cb": 1, "body": 3, 'page': n_page}
	# 	try:
	# 		r = requests.get(base_url, params=params, timeout=1)
	# 		# print(k)
	# 	except requests.exceptions.Timeout:
	# 		print(f'{k}) *пропущен')
	# 		break
	# 	except requests.exceptions.RequestException as e:
	# 		print(f"Произошла ошибка: {e}")
	# 		break

	# 	request_text = r.text.replace("&shy", '').replace(";\xad", "").replace("\xad", "")
	# 	soup_reponses = BeautifulSoup(request_text, 'html.parser')
	# 	maindiv_answers = soup_reponses.find_all(name="div", attrs={"class": "prob_maindiv"})

	# 	for maindiv_answer in maindiv_answers:
	# 		answer_soup = BeautifulSoup(str(maindiv_answer), 'html.parser')
	# 		answer_id = answer_soup.find(name="div", attrs={"class": "pbody"})['id']
	# 		answer_div = answer_soup.find(name="div", attrs={"class": "answer"})

	# 		if answer_id == task_id:
	# 			ans_text = answer_div.get_text()
	# 			ans.append(ans_text[ans_text.rfind(': ') + 2:])

	# 	n_page += 1

	# if len(ans):
	# 	print(str(k) + ')', " или ".join(ans))

	# k += 1
