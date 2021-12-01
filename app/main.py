from typing import Any, Dict
import pandas as pd
import requests

    

def read_file(file_name: str) -> Dict:
    df = pd.read_excel(file_name)
    df["AC + PN"] = df["AC + PN"].apply(lambda x: str(x)[-10:])
    return {"F"+ str(k + 2):v for k, v in df["AC + PN"].to_dict().items()}

def encrypt_values(rows: Dict) -> Dict:
    return {"H" + k[1:]:encrypt_phone(v) for k, v in rows.items()}

def write_to_file(file_name: str, data: Dict) -> None:
    pass

def encrypt_phone(phone: str) -> str:
    response = requests.get("http://localhost:8080/hash/phone/" + phone)
    if response:        
        return response.text
    return "" #TODO Catch exceptions and act accordingly


if __name__ == '__main__':
    output = read_file("Phones.xlsx")