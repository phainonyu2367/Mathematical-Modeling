import pandas as pd
import numpy as np
dates = pd.date_range(start='20191101', end='20191124', freq='D')
a1 = pd.DataFrame(np.random.randn(24, 4), index=dates, columns=list('ABCD'))
a2 = pd.DataFrame(np.random.randn(24, 4))
a1.to_excel('data2_38_1_0.xlsx', index=False)
a2.to_csv('data2_38_2_0.csv', index=False)
f = pd.ExcelWriter('data2_38_3_0.xlsx')
a1.to_excel(excel_writer=f, sheet_name="Sheet1", index=False)
a2.to_excel(excel_writer=f, sheet_name="Sheet2", index=False)
f._save()