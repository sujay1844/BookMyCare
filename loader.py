import json
from json.decoder import JSONDecodeError
from enum import Enum

class Datatype(Enum):
    DICT = 1
    LIST = 2

def load(fname:str, datatype:Datatype) -> dict:
    try:
        with open(fname, 'r') as file:
            data = json.load(file)
    except (JSONDecodeError, FileNotFoundError):
        with open(fname, 'w') as file:
            if datatype == Datatype.DICT:
                file.write('{}')
                data = {}
            elif datatype == Datatype.LIST:
                file.write('[]')
                data = []
            else:
                data = None
    return data
