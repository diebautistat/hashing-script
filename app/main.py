from typing import Any, Dict
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode, b64encode
import openpyxl
import requests


def read_file(file_name: str) -> Dict:
    pass

def encrypt_values(rows: Dict) -> Dict:
    pass

def write_to_file(file_name: str, data: Dict) -> None:
    pass

def encrypt_phone(phone: str) -> str:
    url = f"http://localhost:8080/hash/phone/{phone}"
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    phones_file = openpyxl.load_workbook('Phones.xlsx')
    sheet = phones_file["Base definitiva"]
    rows_count = sheet.max_row
    for i in range (2, rows_count + 1):
        phone = f"F{i}"
        phone_initial_value = f"H{i}"
        phone_final_value = f"I{i}"
        initial_value = str(sheet[phone].value).lstrip('0')[-10:]
        encrypted_phone =  encrypt_phone(initial_value)
        sheet[phone_initial_value].value = initial_value
        sheet[phone_final_value].value = encrypted_phone
        print(i)
    phones_file.save("Output.xlsx")
