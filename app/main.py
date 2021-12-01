from typing import Any, Dict
import pandas as pd
import requests
from requests import HTTPError
from app.exceptions import ApiCallException, ApiResponseException

    

def read_file(file_name: str) -> Dict:
    df = pd.read_excel(file_name)
    df["AC + PN"] = df["AC + PN"].apply(lambda x: str(x)[-10:])
    return {"F"+ str(k + 2):v for k, v in df["AC + PN"].to_dict().items()}

def encrypt_values(rows: Dict) -> Dict:
    return {"H" + k[1:]:encrypt_phone(v) for k, v in rows.items()}

def write_to_file(file_name: str, data: Dict) -> None:
    pass

def encrypt_phone(phone: str) -> str:
    try:
        response = requests.get("http://localhost:8080/hash/phone/" + phone)
        if response.status_code == 200:        
            return response.text
        else:
            raise ApiResponseException("Response code is: " + str(response.status_code))
    except HTTPError as error:
        raise ApiCallException(error) from error
    except Exception as error:
        raise ApiCallException(error) from error

if __name__ == '__main__':
    output = read_file("Phones.xlsx")