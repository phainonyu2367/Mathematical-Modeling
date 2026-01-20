"""
Docstring for ex2_37
生成服从标准正态分布的24x4随机数矩阵，并保存为DataFrame数据结构
"""

import numpy as np
import pandas as pd
dates = pd.date_range(start='20191101', end='20191124', freq='D')
a1 = pd.DataFrame(np.random.randn(24, 4), index=dates, columns=list('ABCD'))
a2 = pd.DataFrame(np.random.rand(24, 4))
print(a1)
print(a2)