from app.main import read_file


def test__read_file__after_file_reading__output_cardinal_should_be_103949():
    input = "Phones.xlsx"
    output = read_file(input)
    assert len(output) == 103949

def test__read_file__after_file_reading__output_dict_should_hold_F_column():
    input = "Phones.xlsx"
    output = read_file(input)
    assert output["F7"] == "04811118843"[-10:]

