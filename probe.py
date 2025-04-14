# import os
# import csv
# import webbrowser
#
# from airium import Airium
# import time
# import keyboard
#
#
# FILE_PATH = '../Price_List_Analyzer_Glob/Files_for_analysis'
# FILE_HTML = '../Price_List_Analyzer_Glob/Files_for_analysis/output.html'
# FILE_HTML_1 = 'output.html'
# LIST_RESULT = []
# SEARCH = input(f"Найти: ")
# SAFE_WORD = []
# class PriceMachine:
#
#     def load_prices(self):
#         '''
#             Сканирует указанный каталог. Ищет файлы со словом price в названии.
#             В файле ищет столбцы с названием товара, ценой и весом.
#             Допустимые названия для столбца с товаром:
#                 товар
#                 название
#                 наименование
#                 продукт
#             Допустимые названия для столбца с ценой:
#                 розница
#                 цена
#             Допустимые названия для столбца с весом (в кг.)
#                 вес
#                 масса
#                 фасовка
#         '''
#         Product_name = ['товар', 'название', 'наименование', 'продукт']
#         Name_with_price = ['розница', 'цена']
#         Name_with_weight = ['вес', 'масса', 'фасовка']
#         files = os.listdir(FILE_PATH)
#
#         for file in files:
#
#             # if key == "exit":
#             #     break
#             if "price" in file:
#                 with open(f'{FILE_PATH}/{file}', mode="r", encoding='utf-8') as sort_file:
#                     for row in csv.reader(sort_file):
#                         for i in Product_name:
#                             try:
#                                 index_Product_name = row.index(i)
#                             except:
#                                 None
#                         a = row[index_Product_name]
#
#                         for i in Name_with_price:
#                             try:
#                                 index_Name_with_price = row.index(i)
#                             except:
#                                 None
#                         try:
#                             b = int(row[index_Name_with_price])
#                         except:
#                             b = row[index_Name_with_price]
#
#                         for i in Name_with_weight:
#                             try:
#                                 index_Name_with_weight = row.index(i)
#                             except:
#                                 None
#                         try:
#                             c = int(row[index_Name_with_weight])
#                         except:
#                             c = row[index_Name_with_weight]
#
#                         if a not in Product_name and b not in Name_with_price and c not in Name_with_weight:
#                             result = a, b, c, file
#                             LIST_RESULT.append(result)
#         LIST_RESULT.sort(key=lambda x: x[1])
#         return LIST_RESULT
#
#     def find_text(self):
#         '''
#         Нолучает текст и возвращает список позиций,
#         содержащий этот текст в названии продукта.
#         <td 1></td><td Филе пангасиуса б/ш ></td><td 92></td><td 1></td><td price_5.csv></td>
#         <td 2></td><td Филе пангасиуса б/ш ></td><td 103></td><td 1></td><td price_4.csv></td>
#         <td 3></td><td Ряпушка вял н/р></td><td 119></td><td 1></td><td price_3.csv></td>
#         <td 4></td><td Килька п/п ></td><td 130></td><td 1></td><td price_0.csv></td>
#         '''
#         file = open(f"{FILE_HTML}", "a", encoding='utf-8')
#         b = Airium(source_minify=True)
#         y = 0
#
#
#         for i in LIST_RESULT:
#
#             # time.sleep(0.05)
#             if keyboard.is_pressed('e'):
#                 SAFE_WORD.append('e')
#             if keyboard.is_pressed('x'):
#                 SAFE_WORD.append('x')
#             if keyboard.is_pressed('i'):
#                 SAFE_WORD.append('i')
#             if keyboard.is_pressed('t'):
#                 SAFE_WORD.append('t')
#             if {'e', 'x', 'i', 't'} <= set(SAFE_WORD):
#                 break
#
#             if SEARCH in i[0]:
#                 y += 1
#                 b.break_source_line()
#                 with b.tr():
#                     with b.td(_t=y):
#                         pass
#                     with b.td(_t=i[0]):
#                         pass
#                     with b.td(_t=i[1]):
#                         pass
#                     with b.td(_t=i[2]):
#                         pass
#                     with b.td(_t=i[3]):
#                         pass
#         file.write(str(b))
#         return b
#
#     def export_to_html(self):
#         '''
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>Позиции продуктов</title>
#         </head>
#         <body>
#             <table>
#                 <tr>
#                     <th>Номер</th>
#                     <th>Название</th>
#                     <th>Цена</th>
#                     <th>Фасовка</th>
#                     <th>Файл</th>
#                     <th>Цена за кг.</th>
#                 </tr>
#         '''
#         file = open(f"{FILE_HTML}", "w", encoding ='utf-8')
#         a = Airium()
#         a('<!DOCTYPE html>')
#         with ((((a.html())))):
#             a.head()
#             a.title(_t="Позиции продуктов")
#         with a.body():
#             with a.table():
#                 with a.tr():
#                     a.th(_t="№")
#                     a.th(_t="Наименование")
#                     a.th(_t="Цена")
#                     a.th(_t="Масса")
#                     a.th(_t="Файл")
#                 with a.tr(_t=self.find_text()):
#                     pass
#             file.write(str(a))
#         # webbrowser.open_new_tab(file_html)
#         webbrowser.open_new_tab(f'file://{os.getcwd()}/Files_for_analysis/{FILE_HTML_1}')
#
# if __name__ == "__main__":
#     PriceMachine.load_prices(FILE_PATH)
#     PriceMachine().export_to_html()

from tabulate import tabulate


def print_table_tabulate(data):
    headers = ["ID", "Имя", "Возраст"]
    formatted_data = [headers] + data

    # Вывод в разных стилях
    print("\nСтиль plain:")
    print(tabulate(formatted_data, headers=headers, tablefmt="plain"))

    print("\nСтиль grid:")
    print(tabulate(formatted_data, headers=headers, tablefmt="grid"))

    print("\nСтиль fancy_grid:")
    print(tabulate(formatted_data, headers=headers, tablefmt="fancy_grid"))


# Пример использования
data = [
    [1, "Иван Петрович", 25],
    [2, "Мария Ивановна", 30]
]

print_table_tabulate(data)