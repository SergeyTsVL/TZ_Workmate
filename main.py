import json
import os
from collections import Counter


FILE_PATH = './logs'
TOTAL_lIST = []
INFO_list, ERROR_list, WARNING_list, DEBUG_list, CRITICAL_list = [], [], [], [], []
Total_requests = 0


class Analiz_logs():

    def load_file(self):
        files = os.listdir(FILE_PATH)
        for file in files:
            # print(file, '********************************************************************************************************************************')
            with open(f'{FILE_PATH}/{file}', mode="r", encoding='utf-8') as file:
                for line in file:
                    global Total_requests
                    Total_requests += 1
                    TOTAL_lIST.append(' '.join((line.split()[3:])))
        for file in files:
            with open(f'{FILE_PATH}/{file}', mode="r", encoding='utf-8') as file:
                for line in file:
                    # print(' '.join((line.split()[3:])))
                    if ' '.join((line.split()[3:])) in set(TOTAL_lIST):
                        # print(' '.join((line.split()[3:])))
                        d = line.split()[2]
                        print(d)

        # with open(f'{FILE_PATH}/{file}', mode="r", encoding='utf-8') as file:
        #     for line in file:
        #         if line in set(TOTAL_lIST):
        #             print(555555555)










        #
        #             if str(line.split()[2]) == 'INFO':
        #                 INFO_list.append(' '.join((line.split()[3:])))
        #             if str(line.split()[2]) == 'ERROR':
        #                 ERROR_list.append(' '.join((line.split()[3:])))
        #             if str(line.split()[2]) == 'WARNING':
        #                 WARNING_list.append(' '.join((line.split()[3:])))
        #             if str(line.split()[2]) == 'DEBUG':
        #                 DEBUG_list.append(' '.join((line.split()[3:])))
        #             if str(line.split()[2]) == 'CRITICAL':
        #                 CRITICAL_list.append(' '.join((line.split()[3:])))
        # print(Total_requests)
        # # counter_INFO_dict = dict(Counter(INFO_list))
        # print(type(TOTAL_lIST))
        # print(type(' '.join((line.split()[3:]))))
        # print(' '.join((line.split()[3:])))
        # print(len(TOTAL_lIST))

        # print(INFO_list)
        # print(ERROR_list)
        # print(WARNING_list)
        # print(DEBUG_list)
        # print(CRITICAL_list)




#
#                     b = ' '.join(a[3:])
#
#                     c = a[2] + ' ' + b
#                     # c = list(a[2]).extend(list(b))
#                     print(c)
#
# #











f = Analiz_logs()
f.load_file()