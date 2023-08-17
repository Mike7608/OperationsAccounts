from INIT import init


class Operation:
    """
    Основной класс для работы программы
    """

    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def get_security_account_operation_from(self):
        """
        Процедура шифрования и форматирования картсчета в формате XXXX XX** **** XXXX
        :return: Счет XXXX XX** **** XXXX
        """
        str_tmp = str(self.data['from']).split(" ")
        len_tmp = len(str_tmp)
        # берем строку со счетом
        str_sel = str_tmp[len_tmp - 1]
        # в счете должно быть 16 символов и более
        # если менее то выводим строку init.STRING_FROM_IS_NONE
        if len(str_sel) > 15:
            str_tmp.pop(len_tmp - 1)
            len_acc = len(str_sel)
            start_str = str_sel[0:init.COUNT_DISPLEY_SYMBOLS_START_STRING_FROM]
            end_str = str_sel[len_acc - init.COUNT_DISPLAY_SYMBOLS_END_STRING_FROM:]
            sec_str = init.SYMBOL_FOR_SECURITY * (len_acc - len(start_str) - len(end_str))
            str_result = start_str + sec_str + end_str
            # делим строку на блоки по n-знаков
            n = init.COUNT_DIGITS_IN_BLOK
            chunks = [str_result[i:i + n] for i in range(0, len(str_result), n)]
            return str(" ".join(str_tmp) + " " + " ".join(chunks)).strip()
        else:
            return init.STRING_FROM_IS_NONE

    def get_security_account_operation_to(self):
        """
        Процедура шифрования и форматирования счета получателя в формате **XXXX
        :return: Счет **XXXX
        """
        str_tmp = str(self.data['to']).split(" ")
        len_tmp = len(str_tmp) - 1
        str_tmp[len_tmp] = (str(init.SYMBOL_FOR_SECURITY * 2) +
                            str_tmp[len(str_tmp) - 1][-init.COUNT_DISPLAY_SYMBOLS_END_STRING_TO:])
        return " ".join(str_tmp)
