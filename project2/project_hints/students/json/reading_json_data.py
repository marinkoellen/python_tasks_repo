import json
with open("data/quiz.json") as json_file:
    json_data = json.load(json_file)


for item in json_data['quiz']:
    question = json_data['quiz'][item]['question']
    options = json_data['quiz'][item]['options']

    print( f"Question {item}: {question}")
    for option in options:
        print(f"       {option}")




# with open('new_file.json','w') as f:
#     json.dump(json_data, f,indent = 2)

# with open("new_file.json") as json_file:
#     json_data = json.load(json_file)