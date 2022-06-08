import requests
import json
if __name__ == '__main__':
    url = 
    headers = {
        'User-Agent': 
    }
    query=input("enter# ")
    data = {
        'kw': query
    }
    resp = requests.post(url=url,data=data,headers=headers)
    filename = data['kw']
    filename += '.json'
    # header = resp.headers
    # for k,v in header.items():
    #     print(k,": ",v)
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(resp.json(),fp=fp,ensure_ascii=False)
    print('done')