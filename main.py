import os


FILE_PATH = './logs'
FILE_NAME = 'handlers.txt'
LOGS_lIST = []
SET_lIST = []
END_lIST = []
TOTAL_INFO, TOTAL_ERROR, TOTAL_WARNING, TOTAL_DEBUG, TOTAL_CRITICAL, Total_requests = 0, 0, 0, 0, 0, 0


class Analiz_logs():
    def load_file(self):
        '''
        Этот код читает все файлы в папке указанной в FILE_PATH. Если файл не читаемый выдает по нему исключение.
        Прочитанные строки в файле преобразуются в списки, разделителем служит пробел. Далее уже элементы списков
        подсчитываются для заполнения таблицы INFO, ERROR, ... и для расчета TOTAL_SUMM TOTAL_INFO, TOTAL_ERROR...
        Далее строка с подробным описанием путем преобразования строк сокращается до, например, /api/v1/shipping/.
        :return:
        '''
        global SET_lIST, TOTAL_INFO, TOTAL_ERROR, TOTAL_WARNING, TOTAL_DEBUG, TOTAL_CRITICAL, Total_requests
        files = os.listdir(FILE_PATH)
        for file in files:
            try:
                with open(f'{FILE_PATH}/{file}', mode="r", encoding='utf-8') as file:
                    for line in file:
                        Total_requests += 1
                        LOGS_lIST.append([' '.join((line.split()[3:])), line.split()[2]])
                        SET_lIST.append(' '.join((line.split()[3:])))
            except:
                print(f'{file} - Не доступен/корректен для обработки')
        END_lIST.append(['HANDLER', 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'])
        SET_lIST = set(SET_lIST)
        SET_lIST = list(SET_lIST)
        SET_lIST = sorted(SET_lIST)
        for i in SET_lIST:
            INFO, ERROR, WARNING, DEBUG, CRITICAL = 0, 0, 0, 0, 0
            try:
                for j in LOGS_lIST:
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
                    END_lIST.append([parts, INFO, DEBUG, WARNING, ERROR, CRITICAL])  # textwrap.fill(parts, 25)
            except:
                print(ValueError("Пустая подстрока"))
        END_lIST.append(['TOTAL_SUMM', TOTAL_INFO, TOTAL_DEBUG, TOTAL_WARNING, TOTAL_ERROR, TOTAL_CRITICAL])

def print_table_tabulate(data):
    """
    Этот метод создает файл с названием указанным в FILE_NAME. Записываем в него данные используя print(), при этом
     определяем указанный формат.
    :param data:
    :return:
    """
    with open(FILE_NAME, 'w', newline='', encoding='utf-8') as file:
        print(f'Total requests:{Total_requests}', file=file)
        for row in data:
            print('{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format( row[0], row[1], row[2], row[3], row[4], row[5]), file=file)

f = Analiz_logs()
f.load_file()
print_table_tabulate(END_lIST)
