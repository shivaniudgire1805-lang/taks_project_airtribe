import json

from pathlib import Path

from config.settings import BASE_DIR

BASE_DIR :Path = Path(__file__).resolve().parent.parent/"data"


def read_json(filename:str):
    file_path=BASE_DIR / filename
    
    #open means open the file r means for reading purpose
    file=  open(file_path, "r")
    return json.load(file)

def write_json(filename:str, data)->None:
    file_path=BASE_DIR/filename

    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)