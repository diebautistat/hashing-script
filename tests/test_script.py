from app.main import read_file, encrypt_values, encrypt_phone
import pytest
import requests



def test__read_file__after_file_reading__output_cardinal_should_be_103949():
    input = "Phones.xlsx"
    output = read_file(input)
    assert len(output) == 103949

def test__read_file__after_file_reading__output_dict_should_hold_F_column():
    input = "Phones.xlsx"
    output = read_file(input)
    assert output["F7"] == "04811118843"[-10:]


def test__encrypt_values___a_phone_needs_to_be_encrypted__encrypt_function_should_be_called(mocker):
    output = {"F2": "1234567890"}
    instance = mocker.patch("app.main.encrypt_phone")
    encrypted_rows = encrypt_values(output)
    instance.assert_called_with("1234567890")

def test__encrypt_values___phone_to_encrypt_is_passed_as_parameter__response_contains_encrypted_phone(mocker):
    output = {"F2": "1234567890"}
    mocker.patch("app.main.encrypt_phone", return_value = "LOPOJSNCU")
    encrypted_rows = encrypt_values(output)
    assert encrypted_rows["H2"]  == "LOPOJSNCU"

def test__encrypt_phone__phone_is_encrypted__encrypt_endpoint_should_be_called(mocker):
    instance = mocker.patch("requests.get")
    encrypt_phone("1234567890")
    instance.assert_called_with("http://localhost:8080/hash/phone/1234567890")