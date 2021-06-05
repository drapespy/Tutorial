"""
How to use the `requests` module!
"""

import requests

def ascii(text: str):
    newtext = text.replace(" ", "+")
    rg = requests.get(f'https://artii.herokuapp.com/make?text={newtext}')
    return rg.text

print(ascii("This is an example"))