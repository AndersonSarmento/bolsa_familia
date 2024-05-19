import json


def read_json(path):
    with open(path, 'r', encoding='utf8') as json_file:
        data = json.load(json_file)
    return data

def requisicao(url):
   reponse=requests.get(url)
   return reponse

