import os



# LOGS_lIST = []
# SET_lIST = []
# END_lIST = []
# TOTAL_INFO, TOTAL_ERROR, TOTAL_WARNING, TOTAL_DEBUG, TOTAL_CRITICAL, Total_requests = 0, 0, 0, 0, 0, 0


class Analiz_logs:
    def __init__(self):
        self.file_path = './logs'
        self.file_name = 'handlers.txt'
        self.Total_requests = 0
        self.LOGS_lIST = []
        self.SET_lIST = []
        self.END_lIST = []

    def load_file(self):
        '''
        Этот код читает все файлы в папке указанной в FILE_PATH. Если файл не читаемый выдает по нему исключение.
        Прочитанные строки в файле преобразуются в списки, разделителем служит пробел.
        :return:
        '''

        files = os.listdir(self.file_path)

        # Total_requests = 0
        for file in files:
            try:
                with open(f'{self.file_path}/{file}', mode="r", encoding='utf-8') as file:
                    for line in file:
                        # print(line)
                        self.Total_requests += 1
                        self.LOGS_lIST.append([' '.join((line.split()[3:])), line.split()[2]])
                        self.SET_lIST.append(' '.join((line.split()[3:])))
            except:
                print(f'{file} - Не доступен/корректен для обработки')
        return self.LOGS_lIST, self.SET_lIST
        # print(LOGS_lIST[0])
        # print(SET_lIST[0])
    # ['django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]', 'INFO']
    # django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]

    def read_file(self):
        """
        Элементы списков подсчитываются для заполнения таблицы INFO, ERROR, ... и для расчета TOTAL_SUMM
        TOTAL_INFO, TOTAL_ERROR... Далее строка с подробным описанием путем преобразования строк сокращается до, например,
        /api/v1/shipping/.
        :return:
        """

        self.END_lIST.append(['HANDLER', 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'])
        TOTAL_INFO, TOTAL_ERROR, TOTAL_WARNING, TOTAL_DEBUG, TOTAL_CRITICAL= 0, 0, 0, 0, 0
        SET_lIST = set(self.SET_lIST)
        SET_lIST = list(SET_lIST)
        SET_lIST = sorted(SET_lIST)
        for i in SET_lIST:
            INFO, ERROR, WARNING, DEBUG, CRITICAL = 0, 0, 0, 0, 0
            try:
                for j in self.LOGS_lIST:
                    if i == j[0] and '/' in j[0]:
                        if j[1] == 'INFO':
                            INFO += 1
                            TOTAL_INFO += 1
                        if j[1] == 'ERROR':
                            ERROR += 1
                            TOTAL_ERROR += 1
                        if j[1] == 'WARNING':
                            WARNING += 1
                            TOTAL_WARNING += 1
                        if j[1] == 'DEBUG':
                            DEBUG += 1
                            TOTAL_DEBUG += 1
                        if j[1] == 'CRITICAL':
                            CRITICAL += 1
                            TOTAL_CRITICAL += 1
                if '/' in i:
                    char_list = []
                    char_int = 0
                    for char in i:
                        char_int += 1
                        if "/" == char:
                            char_list.append(char_int)
                    min_char = min(char_list)
                    max_char = max(char_list)
                    parts = i[min_char - 1:max_char]
                    self.END_lIST.append([parts, INFO, DEBUG, WARNING, ERROR, CRITICAL])  # textwrap.fill(parts, 25)
            except:
                print(ValueError("Пустая подстрока"))
        self.END_lIST.append(['TOTAL_SUMM', TOTAL_INFO, TOTAL_DEBUG, TOTAL_WARNING, TOTAL_ERROR, TOTAL_CRITICAL])
        print(self.END_lIST[1])
        # ['/admin/dashboard/', 1, 0, 0, 0, 0]
        return self.END_lIST

    def print_table_tabulate(self, data):
        """
        Этот метод создает файл с названием указанным в FILE_NAME. Записываем в него данные используя print(), при этом
         определяем указанный формат.
        :param data:
        :return:
        """
        with open(self.file_name, 'w', newline='', encoding='utf-8') as file:
            print(f'Total requests:{self.Total_requests}', file=file)
            for row in data:
                print('{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])), file=file)
                # print('{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(*data), file=file)



    # def print_table_tabulate(self, data):
    #     """
    #     Создает файл с табулированными данными
    #     """
    #     with open(self.file_name, 'w', newline='', encoding='utf-8') as file:
    #         print(f'Total requests:{self.Total_requests}', file=file)
    #         # Преобразуем данные в кортеж, если они не являются последовательностью
    #         row_data = tuple(data) if not isinstance(data, (list, tuple)) else data
    #         d = '{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(
    #             row_data[0], row_data[1], row_data[2],
    #             row_data[3], row_data[4], row_data[5]
    #         )
    #         print(d, file=file)

f = Analiz_logs()
f.load_file()
# f.read_file()
f.print_table_tabulate(f.read_file())

import pytest
import tempfile

# def save_data_to_file(data, filename):
#     with open(filename, 'w') as f:
#         f.write(data)

