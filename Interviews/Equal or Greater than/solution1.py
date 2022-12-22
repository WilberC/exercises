import os
import json

# import requests # Import requests for making query to endpoint

# r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
# data = r.json()['data'] # returns data of endpoint
# -------------
file_path = os.getcwd() + "/Interviews/Equal or Greater than/age-counting.json"
data = json.load(open(file_path))['data']


def equal_or_greater_than(number: int = 50):
    return sum(
        filter(lambda x: int(x) >= number, [int(age) for age in ''.join(data.split(',')[1::2]).split('age=')[1:]]))


equal_or_greater_than()
