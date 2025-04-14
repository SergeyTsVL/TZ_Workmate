import os
import csv
from tabulate import tabulate
import textwrap

FILE_PATH = './logs'
LOGS_lIST = []
SET_lIST = []
END_lIST = []
TOTAL_INFO, TOTAL_ERROR, TOTAL_WARNING, TOTAL_DEBUG, TOTAL_CRITICAL, Total_requests = 0, 0, 0, 0, 0, 0


class Analiz_logs():
    def load_file(self):
        global SET_lIST, TOTAL_INFO, TOTAL_ERROR, TOTAL_WARNING, TOTAL_DEBUG, TOTAL_CRITICAL
        Total_requests = 0
        files = os.listdir(FILE_PATH)
        for file in files:
            with open(f'{FILE_PATH}/{file}', mode="r", encoding='utf-8') as file:
                for line in file:
                    Total_requests += 1
                    LOGS_lIST.append([' '.join((line.split()[3:])), line.split()[2]])
                    SET_lIST.append(' '.join((line.split()[3:])))
        # END_lIST.append([f'Total requests:{Total_requests}'])
        # END_lIST.append(['HANDLER', 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'])
        SET_lIST = set(SET_lIST)
        SET_lIST = list(SET_lIST)
        SET_lIST = sorted(SET_lIST)
        for i in SET_lIST:
            INFO, ERROR, WARNING, DEBUG, CRITICAL = 0, 0, 0, 0, 0
            for j in LOGS_lIST:
                if i == j[0]:
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
                # print(char_list)
                for ii, char in enumerate(i):
                    # print(char)
                    if char == "/":
                        char_list.append(i.index(char))
                        print(char_list)
                print(type(char_list[0]), type(char_list[1]), type(char_list[2]))
                i = i.split(i.index(min(char_list)))[1].split(i.index(max(char_list)))[0]


            END_lIST.append([textwrap.fill(i, 25), INFO, DEBUG, WARNING, ERROR, CRITICAL])
        END_lIST.append(['TOTAL_SUMM', TOTAL_INFO, TOTAL_ERROR, TOTAL_WARNING, TOTAL_DEBUG, TOTAL_CRITICAL])
        # print(END_lIST)
        # Запись в файл
        with open('handlers.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(END_lIST)

        # Чтение файла для проверки
        with open('handlers.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            # for row in reader:
            #     print(row)




def print_table_tabulate(data):
    # headers = ['HANDLER', 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']
    formatted_data = ['HANDLER', 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']

    # Вывод в разных стилях
    # print("\nСтиль plain:")
    # print(tabulate(END_lIST, tablefmt="plain"))
    #
    # print("\nСтиль grid:")
    # print(tabulate(formatted_data, headers=headers, tablefmt="grid"))
    #
    # print("\nСтиль fancy_grid:")
    # print(tabulate(formatted_data, headers=headers, tablefmt="fancy_grid"))
    # assign data
    # a = [
    #     ["Nikhil", "Delhi"],
    #     ["Ravi", "Kanpur"],
    #     ["Manish", "Ahmedabad"],
    #     ["Prince", "Bangalore"]
    # ]

    # create header
    header = ["Name", "City"]

    # print header
    # print(f"{header[0]:<10} {header[1]:<15}")
    # print("-" * 25)
    line_width = 20
    # print rows
    # for row in END_lIST:
        # print(f"{textwrap.fill(row[0], 30):<20} {row[1]:<15}  {row[2]:<15}  {row[3]:<15}  {row[4]:<15}  {row[5]:<15}")

        # print('{:<30}|{:<10}|{:<10}|{:<10}|{:<10}|{:<10}'.format( row[0], row[1], row[2], row[3], row[4], row[5]))

        # print(f'{row[0]}'.ljust(line_width) + "LEFT"*6, f'row[1]'.ljust(line_width) + "LEFT"*6, f'row[2]'.ljust(line_width) + "LEFT"*6, f'row[3]'.ljust(line_width) + "LEFT"*6)

# textwrap.fill(row[0], 20)
# "{0:<{1}}{0}".format(row[1], 40)
# Пример использования
# data = [
#     [1, "Иван Петрович", 25],
#     [2, "Мария Ивановна", 30]
# ]
# # textwrap.fill(row[0], 25),



f = Analiz_logs()
f.load_file()
print_table_tabulate(END_lIST)


# print ('{:<20}{:<20}'.format('UserName:ывпастм','Foo'))
# print ('{:<30}{:<40}'.format('User:','FooBar'))
# print ('{:<30}{:<40}'.format('','FooBar42'))
#
# line_width = 20
# print ("Username:".ljust(line_width) + "LEFT"*6)
# print ("".ljust(line_width) + "RIGHT"*3)