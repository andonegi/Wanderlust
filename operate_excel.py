import pandas as pd
import os

getFileDate = lambda file: (file[-4:])
j = 0
k = 0
l = 0
indice_inicio = []
indice_final = []
indice_malo = []

# def borrar_datos(head, data):
#
#     for i in range(0, len(datos)):
#         print(i)
#         print(datos.iloc[i,0])
#
#         if (datos.iloc[i,2] == 27 & i > 10) or k == 1:
#             datos.drop(datos.index[i])
#             k = 1



for i in os.listdir(r'C:\Users\Afuentes\Desktop\python\wanderlust\Wanderlust-master'):
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

for i in range(0, len(datos)):
    print(i)
    print(datos.iloc[i,2]) # fila, columna
    print(type(datos.iloc[i,2]))
    print('>>> k = ', k)
    print(datos.iloc[i:])

    indice_inicio.append(i)
    print(indice_inicio)

    if k == 1:
        #datos = datos.drop(i)
        datos = datos.drop(indice_inicio)
        print(datos)
        print('Dentro del BREAK', i)
        break

    if (str(datos.iloc[i,2]) == '60' and i > 3) :
        k = 1
        print(datos, '\n Datos del IF')

indice_malo = list(range(0,len(datos)))
print(type(len(datos)))
print(indice_malo)

for t in range(0, len(datos)):
    print(t)
    print(datos.iloc[t,2])
    print(datos)

    indice_final.append(t)
    print(indice_final)

    if l == 1:
        print('Dentro del BREAK segundo')
        datos = datos.drop(indice_raro)
        break

    if (str(datos.iloc[t,2]) == 27):
        l = 1



print(datos)
print(len(datos))

# writer = pd.ExcelWriter(r'C:\Users\Afuentes\Desktop\python\wanderlust\Docs\new_book.xlsx')
# datos.to_excel(writer, 'new_sheet', index = False)
# writer.save()
# print('Done')

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
