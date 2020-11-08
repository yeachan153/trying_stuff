import json


def f():
    with open("src/test.json") as f:
        file = json.load(f)
    print(f)