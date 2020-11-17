import datetime
import json
import matplotlib.pyplot as mplt
from collections import Counter
import csv


# Suivi des commits quotidiens
with open('commits.json') as f:
    commits = json.load(f)

tmp = []
for i in range(len(commits)):
    data = datetime.datetime.strptime(
        commits[i]['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ')
    commits[i]['commit']['author']['date'] = data.date()
    tmp.append(str(data.month) + '-' + str(data.day))

tmp.reverse()
tmp = Counter(tmp)
x = []
y = []
for k, v in tmp.items():
    x.append(k)
    y.append(tmp[k])

bars = mplt.bar(x, y, width=0.5, color='skyblue')

for i in range(len(y)):
    if y[i] < 2:
        bars[i].set_facecolor('red')

mplt.xticks(rotation=45)
mplt.title('Historique des commits')
mplt.xlabel("Date")
mplt.savefig('test.png')


# Suivi des contributions du top 10 des contributeurs
with open('contributors.json') as f:
    contributors = json.load(f)

cell_text = []

for i in range(len(contributors)):
    tmp = []
    if contributors[i]['type'] == 'User':
        tmp.append(contributors[i]['login'])
        tmp.append(contributors[i]['contributions'])
        tmp.append('')
    if contributors[i]['type'] == 'Anonymous':
        tmp.append(contributors[i]['name'])
        tmp.append(contributors[i]['contributions'])
        tmp.append('X')
    if contributors[i]['type'] == 'Bot':
        tmp.append(contributors[i]['login'])
        tmp.append(contributors[i]['contributions'])
        tmp.append('BOT')
    cell_text.append(tmp)

with open('contributors.csv', 'w', encoding='utf-8', newline='') as f_csv:
    writer = csv.writer(f_csv, delimiter='|')
    writer.writerows(cell_text)
