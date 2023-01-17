
# Google Forms Spam Tool V1 2023

A tool that used for spamming Google forms with answeres saved in an "answers.txt" file, in a loop until stopping the bot

Around 140 answers per 1 minute

WARNING: This project are for educational purposes only, I don't recommend you to use it against google forms!


## Installation

Install my-project with npm

```bash
  git clone https://github.com/MaorDayanOfficial/FormSpamToolV1.git
  cd FormSpamToolV1.0
```
    
## How to run?

1. Edit the python file and replace ReplaceTheID to the actual ID of the form to be like that in the file:
form_url = 'https://docs.google.com/forms/d/e/ReplaceTheID/formResponse'

2. Open Developer tools in the forms page and search in the code: entry.
then add it to the script at:
form_data = {
        'entry.12345678': answer,  # Replace 12345678 with the actual field ID
    }

Save it and :
```bash
cd FormSpamToolV1.0 (if you're not in the folder already)
python FormSpamTool.py
```
To stop it : ctrl + c 


