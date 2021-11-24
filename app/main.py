from typing import Any, Dict
import pandas as pd

    

def read_file(file_name: str) -> Dict:
    df = pd.read_excel(file_name)
    df["AC + PN"] = df["AC + PN"].apply(lambda x: str(x)[-10:])
    dict_columns = {"F"+ str(k + 2):v for k, v in df["AC + PN"].to_dict().items()}
    return dict_columns

def encrypt_values(rows: Dict) -> Dict:
    pass

def write_to_file(file_name: str, data: Dict) -> None:
    pass

def encrypt_phone(phone: str) -> str:
    pass


if __name__ == '__main__':
    output = read_file("Phones.xlsx")