

import requests


def len_joke():
    return len(get_joke())


def get_joke():
    url = 'http://api.icndb.com/jokes/random'

    res = requests.get(url)

    if res.ok:
        joke = res.json()['value']['joke']
    else:
        joke = 'no joke'

    return joke


if __name__ == '__main__':
    print(get_joke())
