# parse content from json file

import json
courses = '{"name": "Lee", "languages":["Java", "Python"]}'

# Loads method parse json string and it returns dictionary

dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

# get the first language

list_courses = dict_courses['languages']
print(type(list_courses))
print(list_courses[0])

print(dict_courses['languages'][0]) # simpler version

