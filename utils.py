import config
import backoff
import openai
import json
from datetime import datetime

def write_list_of_dictionaries_to_file(list, filename):
    with open(filename, 'a') as f:
        f.write('[\n')
        for dictionary in list:
            json.dump(dictionary, f)
            f.write(',\n')
        f.write(']')

def LastLetterYes(input):
    for i in range(10):
        if input[-i] == 'Y':
            return True
        elif input[-i] == 'N':
            return False
    return False