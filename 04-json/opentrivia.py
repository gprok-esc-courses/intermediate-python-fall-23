import requests
import json
import html

response = requests.get('https://opentdb.com/api.php?amount=10')

# print(response.text)
data = json.loads(response.text)

quiz = data['results']

counter = 1
for item in quiz:
    print("Q" + str(counter) + ": " + html.unescape(item['question']))
    print("a. " + html.unescape(item['correct_answer']))
    print("b. " + html.unescape(item['incorrect_answers'][0]))
    if item['type'] == 'multiple':
        print("c. " + html.unescape(item['incorrect_answers'][1]))
        print("d. " + html.unescape(item['incorrect_answers'][2]))
    counter += 1
    answer = input("> ")

    # Check the answer, update score

# Display score
