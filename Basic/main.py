import numbers
import random
import string
from contextlib import redirect_stdout
from time import sleep


def get_random_string():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(2))
    result_dig = ''.join(random.choice(string.digits) for i in range(4))
    url = ("https://prnt.sc/"+ result_str + result_dig)
    print(url)
    with open("Output.txt", "a") as  f:
        f.write(f'{url}\n')

while True:
    get_random_string()