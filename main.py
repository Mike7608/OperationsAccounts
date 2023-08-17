import json
import os
import datetime
from INIT import init
from operation import Operation


def load_data(filepath):
    """
    Функция получает из файла json данные и возвращает список операций класса Operation
    :param filepath: путь к файлу json
    :return: список операций класс Operation
    """
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding="utf-8") as file:
            data_file = json.load(file)

            list_operation = []
            # преобразуем список данных json в список данных класса Operation
            for one_op in data_file:
                if len(one_op) > 0:
                    op = Operation()
                    op['id'] = one_op['id']
                    op['state'] = one_op['state']
                    op['date'] = datetime.datetime.fromisoformat(one_op['date'])
                    op['operationAmount'] = one_op['operationAmount']
                    op['description'] = one_op['description']
                    op['from'] = one_op.get('from', "")
                    op['to'] = one_op.get('to', "")
                    list_operation.append(op)

            # получаем новый сортированный по дате список на основе предыдущего
            new_list_operation = sorted(list_operation, key=lambda oper: oper['date'], reverse=True)
            # и возвращаем его
            return new_list_operation
    else:
        print(f"Файл данных '{filepath}' не найден или указан неверный путь!")


def print_operation(oper: Operation):
    """
    Процедура вывода одной операуии Operation
    :param oper: класс Operation
    """
    print(oper['date'].date().strftime(init.DATE_FORMAT), oper['description'])
    print(oper.get_security_account_operation_from(), init.DIRECTION_SYMBOL, oper.get_security_account_operation_to())
    print(oper['operationAmount']['amount'], oper['operationAmount']['currency']['name'])
    print()


def main():
    """
    Главный модуль запуска программы
    """
    # в data получаем список (массив) данных класса Operation
    data = load_data(init.FILE_PATH_OPERATION)

    # счетчик пройденных записей по порядку
    index = 0
    # счетчик требуемых записей
    true_op = 0
    while true_op < init.COUNT_SELECT_OPERATION:  # default = 5
        operation = data[index]
        # находим запись по критерию state. default = EXECUTED
        if str(operation['state']).upper() == init.TYPE_STATE_OPERATION.upper():
            # и выводим её на экран
            print_operation(operation)
            true_op += 1
        index += 1


# старт программы
if __name__ == '__main__':
    main()
