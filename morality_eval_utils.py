import config
import backoff
import openai
import json
from datetime import datetime

def write_responses_to_file(responses, filename="results.json"):
    with open(filename, 'a') as f:
        for response in responses:
            json.dump(response.to_dict(), f)
            f.write('\n')

def LastLetterYes(input):
    for i in range(10):
        if input[-i] == 'Y':
            return True
        elif input[-i] == 'N':
            return False
    return False