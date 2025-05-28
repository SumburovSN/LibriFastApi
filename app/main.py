from fastapi import FastAPI
from utils import json_to_dict_list
import os
from typing import Optional

import os


# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))
# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)
# Получаем путь к JSON
path_to_json = os.path.join(parent_dir, 'students.json')

app = FastAPI()

@app.get("/students")
def get_all_students():
    return json_to_dict_list(path_to_json)

print(get_all_students())