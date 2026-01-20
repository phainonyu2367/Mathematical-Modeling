import pandas as pd
import numpy as np

a = pd.DataFrame(np.random.randint(1, 6, (5, 3)),
                 index=list('abcde'),
                 columns=['one', 'two', 'three']
                 )
a.loc['a', 'one'] = np.nan
b = a.iloc[1:3, 0:2].values
a['four'] = 'bar'
a2 = a.reindex(list('abcdef'))
a3 = a2.dropna()
print(a2)
print(a3)