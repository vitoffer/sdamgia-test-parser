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
print(len(list(filter(lambda task: task.has_attr('id'), tasks))))

k = 1

dct = json.load(open('rus.json', 'r'))

for task in tasks:
	task_text = BeautifulSoup(str(task), 'html.parser').find(attrs={"class": "pbody"})
	if not task_text.has_attr('id'):
		continue
	task_id = task_text['id']
	if task_id in dct.keys():
		print(str(k) + ')', dct[task_id])
	else:
		print(str(k) + ') не найден')
	k += 1
