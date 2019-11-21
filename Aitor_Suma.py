import pandas as pd
import os
import plotly.graph_objects as plt
import webbrowser as wb
import time

p = 0

while p == 0:
    print('Programa para analizar datos del tranvía de Zaragoza entre dos horas de un mismo día.\n Para acceder presiona mete Y')
    señal_continuar = input()
    if señal_continuar == 'y':
        p = 1
    else:
        print('Hazlo bien colega', end ='\r')
        time.sleep(2)


nombre_archivo_nuevo = input('>>>Como quieres llamar al archivo?\n')
dia_analizar = input('>>>Que dia quieres analizazr?\nFormato mm_dd [Mes_Día]\n>>>')
hora_final_str = input('>>>Hasta que hora quieres analizar la suma?\n>>>Formato hh:mm\n>>>')

path_datos = 'D:\python\python_pruebas\programas'
path_excel = 'D:\python\Docs_Pyt\insert\ ' + nombre_archivo_nuevo + '.xlsx'
getFileXlsx = lambda file: (file[-4:])
getFileDia = lambda file: (file[9:14])


j, k, l, n = 0, 0, 0, 0

indice_inicio = []
indice_final = []
indice_malo = []
columnas = ['FECHA', 'F1_I', 'F2_I']

# def borrar_datos(head, data):
#
#     for i in range(0, len(datos)):
#         print(i)
#         print(datos.iloc[i,0])
#
#         if (datos.iloc[i,2] == 27 & i > 10) or k == 1:
#             datos.drop(datos.index[i])
#             k = 1



for i in os.listdir(path_datos):
    #print(i)
    # print(getFileXlsx(i))
    # print(getFileDia(i))

    if getFileXlsx(i) == '.csv' and getFileDia(i) == dia_analizar:
        #print('It is a MATCH!')
        df = pd.read_csv(i, delimiter=';', usecols=columnas)
        #print(df.head())

        df['F1 + F2'] = df['F2_I'] - df['F1_I']
        #print(df.tail())
        #print('Ahora lo de abajo')
        #print(df.tail())

        if j == 0:
            datos = df
            j = 1
            #print(j,'Valor de j')
        else :
            #print('Concatenacion\n')
            datos = pd.concat((datos,df), ignore_index = True)
            #print(datos.tail())
    #else :
        #print(i + ' No es un archivo CSV')
        #print(getFileDate(i))


#print(datos)
# print('\n >>>>>Este es el archivo concatenado<<<<<\n')
#print(datos.iloc[2,0][-12:-7])
# --------------------------------------------------------------------------
#                       HASTA AQUÍ ESTÁ BIEN
# --------------------------------------------------------------------------

for i in range(0, len(datos)):
    indice_inicio.append(i)

    if k == 1 and n == 1:
        datos = datos.drop(i)
        indice_inicio.pop()
        datos = datos.drop(indice_inicio)

        break

    if datos.iloc[i,0][-12:-7] == '05:40' :
            k = 1
            # print('AHORA K =', k)

    if k == 1 and str(datos.iloc[i,3]) > '0':
        # print('ihhoihas')
        n = 1

# print(datos)
            # print(datos.iloc[indice_inicio], '\n Condición cumplida!!\n\n')
# ------------------------------------------------------------------


indice_malo = list(range(0,len(datos)))
# print(type(len(datos)))
# print(indice_malo)
# print(datos)
# print(datos.tail())

for t in range(0, len(datos)):
    #print(t)
    indice_final.append(t)
    #print(indice_final)
    #print(datos.iloc[t,2])
    #print(datos.iloc[indice_final],'\n\n')

    if l == 1:
        print('Dentro del BREAK segundo')
        indice_final.pop()
        datos = datos.iloc[indice_final]
        print(datos,'\n Ha salido bien?')
        break

    if datos.iloc[t,0][-12:-7] == hora_final_str:
        l = 1

# print(datos)
# print(len(datos))

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

#writer = pd.ExcelWriter(r'D:\python_pruebas\doc_excel\caca.xlsx')
writer = pd.ExcelWriter(path_excel)
datos.to_excel(writer, 'The_Real_Shit', index = False)
writer.save()
print('Done')

# --------------------------------------------------------------------------
# --------------------------------------------------------------------------

fig = plt.Figure()

for key in datos:
    if key != 'FECHA':
        fig.add_trace(plt.Scatter(x=datos['FECHA'],
                                  y=datos[key],
                                  mode='lines',
                                  name=key,
                                  # name = (key+' '*3+str(init))
                                  ))
#horasConsumo = FuncMats.detectConsumption(daydata, 'F2_I')


#
# #if key != 'Media':
# fig.add_trace(plt.Scatter(x = daydata['FECHA'],
#                           y = daydata['F2_I'],
#                           mode = 'lines',
#                           name = 'F2_I',
#                           #name = (key+' '*3+str(init))
#                           ))
#
# fig.add_trace(plt.Scatter(x = daydata['FECHA'],
#                           y = daydata['Deteccion'],
#                           mode = 'lines',
#                           name = 'Deteccion',
#                           #name = (key+' '*3+str(init))
#                           ))

print(" >>>  Graficando datos...")

# ### Visualización de los datos -- En Mozilla Firefox ###
fig.update_layout(
    title='DAQ_ZGZ',
    xaxis = {'title': 'Time'},
    yaxis=dict(
        title='Values',
        #range=[-10, 290],
    ),
    yaxis2=dict(
        title='Values',
        #range=[-450, 800],
        overlaying='y',
        side='right'
    )
)

wb.register('chrome', None, wb.BackgroundBrowser(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
fig.show(renderer='chrome')

for x in range (0,5):
    b = 'Loading' + '.' * x
    print(b, end = '\r')
    time.sleep(0.5)
