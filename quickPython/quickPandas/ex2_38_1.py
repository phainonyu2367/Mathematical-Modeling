import pandas as pd
import numpy as np
dates = pd.date_range(start='20191101', end='20191124', freq='D')
a1 = pd.DataFrame(np.random.randn(24, 4), index=dates, columns=list('ABCD'))
a2 = pd.DataFrame(np.random.randn(24, 4))
a1.to_excel('data2_38_1.xlsx')
a2.to_csv('data2_38_2.csv')
f = pd.ExcelWriter('data2_38_3.xlsx')
a1.to_excel(excel_writer=f, sheet_name="Sheet1")
a2.to_excel(excel_writer=f, sheet_name="Sheet2")
f._save()
