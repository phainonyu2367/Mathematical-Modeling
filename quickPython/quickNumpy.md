\# QuickNumpy



to quickly understand the power and be able to use NumPy, it would be a good idea for us to know what exactly can NumPy do.



\## Array Manipulation



NumPy provide a series of method for us to manipulate n-dimentions arrays, which are called ndarrays in NumPy.



\### Create Ndarrays

to create ndarrays with our own data, we use the generator `np.array()` to generate the ndarray we want.

```

import numpy as np



ndarray = np.array(\[\[1, 2, 3], \[4, 5, 6]])

```



there are also special array generators.

```

one = np.ones((1, 2)) # 1x2array filled with one

zero = np.zeros((3, 3)) #  3x3array filled with 0

empty = np.empty((4, 3)) # 4x3array filled with random numbers(actually empty)

one\_like = np.one\_like(a) # a-like array filled with one

eye = np.eye(3) # 3x3elementary matrix

....



```



```

aran = np.arange(<start>, <end>, <step>) # 1dim array from start to end

linspa = np.linspace(<start>, <end>, <amount>) # 1dim array from start to end with <amount> elements

logspa = np.logspace(<start>, <end>, <amount>) # the same, but in log version

```



\#### important parameters/attributes

* .astype(<type>)
* para: dtype=<datatype>





\### array manipulation

\#### array stack

```

a = np.array(...)

b = np.array(...)



np.vstack(\[a, b]) # stack the arrays from up to down

np.hstack(\[c, d])  # stack the arrays from left to right

```



\#### array split

```

np.vsplit(\[a, 2]) # split in to two arrays (in average)

np.hsplit(\[a, 2]) # the same

```



\#### array reshape

`a.reshape(4, 4)`



\### array calculation

calculation in np are all operated element by element

\#### sum

```

a = np.array(...)

b = np.array(...)

sum\_of\_all\_elements = a.sum()

sum\_by\_column = sum(a) = np.sum(a, axis=0)

sum\_by\_column\_with\_dim = np.sum(a, axis=0, keepdims=True)

```



\#### other

```

a = np.array(\[\[1, 2, 3], \[4, 5, 6]])

b = np.array(\[\[1, 2, 3], \[4, 5, 6]])

d = np.array(\[\[1, 2, 3]])

c = a + b

c = a - b

c = a \* b

c = a \* d # d will be expanded first to be able to mul with a

c = a + d

c = a \*\* 2

```



\## Linear Algebra stuff



Matrix multiply

```

c = a @ b

```



in np we have a special module just for linear algebra

np.linalg

* norm # “求范数”
* inv(a) # inverse matrix
* pinv(a) # general inv
* solve(A, b) # solve the equation
* det # determinant
* lstsq # 最小二乘法求超定方程组
* eig  # eigen vectors and eigen values
* eigvals # eigen values
* svd # singular value decomposition
* qr # qr decomposition





practice

1. 求下列矩阵的各个行向量，各个列向量的2范数和矩阵2范数

\[ 0   3   4]

\[1    6   4]



```

import numpy as np

a = np.array(\[\[0, 3, 4], \[1, 6, 4]])

normc = np.linalg.norm(a, axis=0, 2)

normr = np.linalg.norm(a, axix=1, 2)

norm = np.linalg.norm(a, 2)

```



2\. 求解线性方程组的唯一解

3x + y = 9

x + 2y = 8

```

import numpy as np

a = np.array(\[\[3, 1], \[1, 2]])

b = np.array(\[9, 8])

sol1 = np.linalg.solve(a, b)

inva = np.linalg.inv(a)

sol2 = inva @ b

```



3\. 求下列矩阵的特征值和特征向量

\[0  0  0  1]

\[0  0  1  0]

\[0  1  0  0]

\[1  0  0  0]

```

import numpy as np

a = np.eye(4)

b = np.rot90(a)

c, d = np.linalg.eig(b)

print(f"特征值：{c}")

print(f"特征向量：{d}")

```

