import time
import random
import requests

# URL of the Google Form (replace only from https to / - do not replace / change "formResponse")
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSemdQR4ZQbEAHgy7xzubL5WSoQrCtKqzgBSuVa0IDNqWWYRcQ/formResponse'

# The txt File with the answers (put it in the same place as the script) needs to be with the name "answers" or else change the name of the fiile below
answers_file = 'answers.txt'


with open(answers_file) as f:
    answers = f.read().strip().split('\n')


while True:
    
    answer = random.choice(answers)
    
    # Set the form fields
    form_data = {
        'entry.12345678': answer,  # Replace 12345678 with the actual field ID
    }
    

    r = requests.post(form_url, data=form_data)
    

    print(f'Status code: {r.status_code}')
    

    time.sleep(0)
