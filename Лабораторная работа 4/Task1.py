# TODO решите задачу
import json


def task() -> float:
    input_data = "input.json"
    with open(input_data) as f:
        data = json.load(f)

    sum_ = sum(item['score'] * item['weight'] for item in data)
    return round(sum_, 3)




print(task())
