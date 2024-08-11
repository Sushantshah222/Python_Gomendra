# from datetime import datetime, date, timedelta

# if []:
#     print("I am empty, but do i run?")
# if ["hi"]:
#     print("I am elem having, but do i run?")

# print(type(date.today()))
# print(type(str(date.today())))

# try:
#     datetime.strptime("20232-3-2", "%Y-%m-%d").date()
# except ValueError:
#     print('error conversion of value')

# if (type(9)=='int'): # the type gives the instance, not the str
#     print("hello")

# print(type(9) == int)

# try:
#     a = input('enter:') # no error raise if empty 
#     print(a)
# except:
#     print('er')

# print(int("-1") <0)


# with open('2024-08-11.txt') as file:
#     print(file.readline())
    
#     content = file.readline()
#     print(content.strip().split(': '))


# with open('2024-08-11.txt') as file:
#     each_line=None
#     content = file.read()
#     print(content)
#     print(content.split('\n'))

#     for idx, each_line in enumerate(content.split('\n')):
#         # print(each_line.strip().split(': '))
#         if len(each_line)>1:
#             if (idx == 1):
#                 a, b = each_line.replace("Â°C", '').split(": ")
#                 print (a, b)
#             if (idx == 2):
#                 print(each_line.replace("%", ''))

        # print(idx)

# today = date.today()
# week_ago = today - timedelta(days=7)
# week_ago = today - timedelta(days=0)
# print(week_ago)

# import os
# current_file_path = os.path.dirname(__file__)
# print("Full pathname of the current file:", current_file_path)
# os.mkdir(f"{current_file_path}/temp")
