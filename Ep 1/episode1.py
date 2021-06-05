"""
How to use the `requests` module!

Async tutorial with `aiohttp` soon™️
"""

import requests

def ascii(text: str):
    newtext = text.replace(" ", "+")
    rg = requests.get(f'https://artii.herokuapp.com/make?text={newtext}')
    return rg.text

# Want a one line example?
def oneline(text: str):
    return requests.get(f'https://artii.herokuapp.com/make?text={text.replace(" ", "+")}').text

print(ascii("This is an example"))
