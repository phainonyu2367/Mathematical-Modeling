import pandas as pd
a = pd.read_csv(filepath_or_buffer="data2_38_2.csv", usecols=range(1, 5))
# b = pd.read_excel("data2_38_3.xlsx", sheet_name="sheet2", usecols=range(1, 5))
print(a)