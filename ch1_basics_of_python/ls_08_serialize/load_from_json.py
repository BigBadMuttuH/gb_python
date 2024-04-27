import json


def load_from_json(file):
    with open(file) as f:
        result = json.load(f)
        return result


def save_to_jsont(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    conf = {'server': '172.0.0.1',
            'username': 'admin'}

    save_to_jsont('config.json', conf)

    cfg = load_from_json('config.json')
    print(f'{cfg["server"]=}, {cfg["username"]=}')

