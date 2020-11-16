import json
import requests


# Generation des données sur les utilisateurs
i = 1
data = ""

while i < 18:
    temp = 'https://api.github.com/repos/Facebook/react/contributors?anon=true&page=%s&per_page=100' % (
        i)
    response = requests.get(temp)
    str = json.dumps(response.json())
    data = data+','+str[1:-1]
    i = i+1

data = "[" + data[1:] + "]"
f = open("contributors.json", "w+")
f.write(data)

# Generation des données sur les commits
response = requests.get(
    'https://api.github.com/repos/Facebook/react/commits?per_page=100')
commits = response.json()

with open('commits.json', 'w+') as f:
    json.dump(commits, f)
