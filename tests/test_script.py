from app.main import read_file, encrypt_values, encrypt_phone, write_to_file
import pytest
import requests
from requests.models import Response
from requests import HTTPError
from app.exceptions import ApiCallException, ApiResponseException
import pandas as pd

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
    response = Response()
    response.status_code = 200
    instance = mocker.patch("requests.get", return_value=response)
    encrypt_phone("1234567890")
    instance.assert_called_with("http://localhost:8080/hash/phone/1234567890")

def test__encrypt_phone__http_error_is_catched__raises_api_call_exception(mocker):
    instance = mocker.patch("requests.get", side_effect=HTTPError)
    with pytest.raises(ApiCallException):
        encrypt_phone("1234567890")

def test__encrypt_phone__generic_exception_is_catched__raises_api_call_exception(mocker):
    mocker.patch("requests.get", side_effect=Exception)
    with pytest.raises(ApiCallException):
        encrypt_phone("1234567890")

def test__encrypt_phone__status_code_is_differente_than_200__raises_api_response_exception(mocker):
    response = Response()
    response.status_code = 500
    mocker.patch("requests.get", return_value=response)
    with pytest.raises(ApiResponseException):
        encrypt_phone("1234567890")

def test__encrypt_phone__when_file_written__there_should_be_a_new_column_called_result():
    input_data = {f"H{i}":str(i) for i in range(103949)}
    input_file = "Phones_test.xlsx"
    output_file = "Phones_test_output.xlsx"
    write_to_file(input_file, input_data, output_file)
    df = pd.read_excel(output_file)
    assert "result" in df.columns

def test__encrypt_phone__when_file_written__there_should_be_a_new_cellH2_with_hashing_result():
    input_data = {f"H{i}":str(i) for i in range(103949)}
    input_file = "Phones_test.xlsx"
    output_file = "Phones_test_output.xlsx"
    write_to_file(input_file, input_data, output_file)
    df = pd.read_excel(output_file)
    assert "103948" in [str(value) for value in df["result"]]