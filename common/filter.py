import json
import csv

data = None
result = []
keywords = [
	'url',
    'BIM Modeling',
    'CAD',
    'mechanical',
    'industrial',
    'piping',
    'power generation'
]

with open('test.json') as f:
    data = json.load(f)

for dataitem in data:
	flag = False
	i = 0
	for resultitem in result:
		if dataitem["url"] == resultitem["url"]:			
			flag = True
			break
		i += 1
	if flag is False:
		result.append({})
		for keyitem in keywords:
			if keyitem is 'url':
				result[i]['url']=dataitem['url']
			elif dataitem[keyitem] == 1:
				result[i][keyitem] = "YES"
			else:
				result[i][keyitem] = "NO"
	else:
		for keyitem in keywords:
			if keyitem == 'url':
				result[i]['url']=dataitem['url']
			elif dataitem[keyitem] == 1:
				result[i][keyitem] = "YES"	
print result

with open('result.csv', 'w') as csvfile:
    fieldnames = keywords
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in result:
    	writer.writerow(item)
print("Writing complete")

