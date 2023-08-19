import main
from INIT import init


def test_load_data():
    data = main.load_data("operations.json")
    assert isinstance(data, list)


def test_not_load_data():
    err_file = main.load_data("operations.json-0")
    assert err_file is None


def test_print_operation(capsys):
    data = main.load_data("operations.json")
    main.print_operation(data[0])
    captured = capsys.readouterr()
    assert captured.out == "08.12.2019 Открытие вклада\nЗачисление -> Счет **5907\n41096.24 USD\n\n"


def test_main():
    assert main.main() is None


