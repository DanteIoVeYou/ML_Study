import requests

if __name__ == '__main__':
    url = 
    query = input('enter# ')
    headers = {
        'User-Agent': 
    }
    param = {
        'query': query
    }
    resp = requests.get(url=url, params=param, headers=headers)
    text = resp.text
    filename = query+'.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(text)
    print(filename, 'has saved...')
