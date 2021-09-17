# parse content from json file

import json

with open('test.json') as f:
    data = json.load(f)

print(type(data))
print(data)

# now trying to print second course from the list, here value is fetched based on index

print(data['courses'])
print(data['courses'][1])
print(data['courses'][1]['title'])


# trying to fetch the value based on the choice
sampleList = data['courses']
for course in sampleList:
    if course['title'] == 'RPA':
        print(course['price'])
