import pandas as pd
import os

getFileDate = lambda file: (file[-4:])
j = 0
ficheros = []

for i in os.listdir(r'D:\python_pruebas\programas'):
    print(i)
    print(getFileDate(i))

    if getFileDate(i) == 'xlsx':
        print('It is a .XLSX')
        df = pd.read_excel(i)
        print(df.head())

        df['F1 + F2'] = df['Age'] + df['Force']
        print(df.head())
        print('Ahora lo de abajo')
        print(df.tail())

        if j == 0:
            datos = df
            j = 1
        else :
            datos = pd.concat((datos,df), ignore_index = True)






    else :
        print('Algo ta mal')
        print(getFileDate(i))

writer = pd.ExcelWriter(r'D:\python_pruebas\doc_excel\new_book.xlsx')
datos.to_excel(writer, 'new_sheet', index = False)
writer.save()
print('Done')

#
# df = pd.read_excel('pandas_simple.xlsx')
#
# print(df.head())
#
# df['Value 4'] = df['Age'] + df['Force']
#
# print(df.head())
#
# def doble(num):
#     return num * 2
#
# df['Doble'] = df ['Value 4'].apply(doble)
# print(df)
#
# # def resta(fila_1, fila_2):
# #     return fila_2 - fila_1
#
# df['resta'] = df['Age'] - df['Value 4']
# print(df)
# # -------------- The real excel is not changed --------------
#
# writer = pd.ExcelWriter(r'D:\python_pruebas\doc_excel\new_book.xlsx')
# df.to_excel(writer, 'new_sheet', index = False)
# writer.save()
# print('Done')
# # -------------- We have created a new book with the old data --------------
