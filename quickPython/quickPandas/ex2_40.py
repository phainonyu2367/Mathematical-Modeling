import pandas as pd
import numpy as np
a = pd.DataFrame(np.random.randint(1, 6, (10, 4)), columns=list('ABCD'))
a1 = a[:4]
a2 = a[4:]
aa = pd.concat([a1, a2])
s1 = a.groupby('A').mean() # 依据
s2 = a.groupby('A').apply(sum)
print(a1)
print(a2)
print(aa)
print(s1)
print(s2)