import pandas as pd
import os


path_excel = r'D:\python_pruebas\doc_excel'

# ------------ CREATE AN EXCEL DOCUMENT ------------

# Create a Pandas Excel writer using XlsWriter as the engine
writer = pd.ExcelWriter('pandas_simple_2.xlsx', engine='xlswriter')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

# ------------ ADD DATA ------------

# Create a Pandas dataframe from the dataframe
df = pd.DataFrame({'Force' : [10, 20, 30, 20, 15, 30, 45],
                    'Age' : [50, 35, 23, 65, 12, 45, 35]})

# Convert the dataframe to an XlsWriter Excel graph_objects
df.to_excel(writer, sheet_name = 'Sheet 1', index = False)

# ------------ READ DATA ------------

reader = pd.read_excel(r'demo.xlxs')
print(reader)

# ------------ APPEND DATA AT THE END OF AN EXCEL SHEET ------------
