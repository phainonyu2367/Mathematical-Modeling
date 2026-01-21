## 基本数据结构
pandas中有两种基本数据结构
`Series` 和 `DataFrame`
- Series：一个一维的带标签数组，可容纳任何类型的数据
- DataFrame：一个二维数据结构，像二维数组或带有行和列的表格一样容纳数据

>由于pandas中的操作主要围绕DataFrame，我们简要介绍Series的一些基本操作后便围绕DataFrame展开。

## Series
#### 对象创建
```
s = pd.Series(data=, index=, dtype=, name=, copy=, fastpath=)
```

>[!info] pandas中的特殊方法
>- `pd.date_range(start=str, end=str, freq='D', periods=int)`, 通过频率或者分段来创建一个特殊的日期pandas对象
>- `pd.Timestamp('str')` 创建一个特殊的时间戳对象


## DataFrame
本质上是一个二维的数表， 有column和index，分别对应列和行，可以分开定义。

#### 对象创建
`df = pd.DataFrame(data=, index=, columns=, dtype=, copy=)`
内容与上面相同，只不过在创建的时候可以额外提供columns的信息（列表）

额外的，还可以用传入对象字典来创建DataFrame， 其中键式列表前，值式列值。
```
df = pd.DataFrame(
	{
	"A": 1.0,
	"B": pd.Timestamp("20130102)，
	"C": pd.Series(1, index=list(range(4)), dtype="float32"),
	"D": np.array([3] * 4, dtype="int32"),
	"E": pd.Categorical(["test", "train", "test", "train"]),
	"F": "foo",
	}
)
```

生成的DataFrame的列具有不同的dtypes

#### 查看数据
- `DataFrame.head(int)`和`DataFrame.tail(int)`分别查看框架的顶部和底行
- `DataFrame.index`
- `DataFrame.columns`
- `DataFrame.to_numpy`返回底层数据的 NumPy 表示，不包含索引或列标签。
- `DataFrame.dtype`返回底层数据的数据类型

#### 选择器
- 按列选择： 对于`DataFrame`，传入单个标签会选择一列并生成一个`Series`，等同于 `df.A`
- 按行选择： 传入切片 `:` 会选择匹配的行。`df[0:3]`
- 按标签选择
	- `df.loc[]`接收两个参数，第一个选择行，第二个选择列
	- `df.at[]`效果同loc，只不过是专门用来处理单个元素选择的
- 按位置选择
	- `df.iloc()`和loc的效果一样，只不过是用数字index来获取位置
	- `df.iat`
- 布尔索引
	- case: `df[df["A"] > 0]`, 这句的意思是选出df.A大于0的行
	- case: 使用isin()方法进行过滤。
```
df2["E"] = ["one", "one", "two", "three", "four", "three"]
df2[df2["E"].isin(["two", "four"])]
```
实际上就是is in的意思，这里是挑出E列元素在\["two", "four"\]之中的例子

#### 数据处理
- df.describe(): 现实数据的快速统计摘要
- df.T: 转置数据
- df.sort_index(axis=, ascending=): 按轴排序
- df.sort_values(by="B"): 按值排序
- df.mean(axis=): 0为列，1为行，这是pandas和numpy中通用的index，统计平均值
- df.shift(int): 将整体数据下移int行
- df.sub(): 类似numpy中的数据操作，同时也有同样的广播/减少规则

#### 数据修改
- 允许设置新列
	- `df["F"] = s1`
	- 直接添加或修改第F列，同时自动按照索引对齐数据
- 按位置设置值
	- df.loc
	- df.iloc, 两者都可以直接修改

#### 缺失数据及其处理
在Numpy中`np.nan`表示缺失数据。默认情况下它不包含在计算里面。

重新索引允许你更改/添加/删除指定轴上的索引。这会返回数据的副本。
```
df-c = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
```

处理缺失数据
- df.dropna(how='any'): 删除任何包含缺失数据的行
- df.fillna(value=5): 填充缺失数据
- df.isna(DataFrame): 获取值为nan的布尔掩码（即用布尔值标注每一个位置上是否为nan）

#### 对象操作
拼接：
- pd.concat(list: pieces)，自动对齐将内容拼接起来

分组：
- df.groupby(index=)：按照index组的value来分组，分组得到的结果并不是直接处理的，而是相当于一个中间态，只有经过比如sum()之类的才会得到进一步的结果

堆叠：
- 我们知道，pandas中存在multiindex，对于一个dataframe，我们可以使用
- df.stack(future_stack=True): 这压缩了Dataframe列中的一个层
- 可以用unstack()来进行stack()的逆操作

透视：
- pd.pivot_table(df, value=, index=, columns=, aggfunc=)
- 透视表，简单地来讲就是将原来的结构改造为新给出的结构，并通过aggfunc来讲不同维度的数据聚合在一起

#### 时间序列

```
rng = pd.date_range("1/1/2012", periods=100, freq="s")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts_utc = ts.tz_localize("UTC") # 将时间序列本地化到某个时区
ts_utc.tz_convert("US/Eastern") # 将时区感知的时间序列转换为另一个时区
```

#### 分类数据
pandas可以在DataFrame中包含分类数据
```
df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
    df["grade"] = 
)
df["raw_grade"].astype("category")
# category 是pandas中的特殊数据类型
new_categories = ["very good", "good", "very bad"]
df["grade"] = df["grade"].cat.rename_categories(new_categories)
```

#### 文件操作
CSV:
- df.to_csv(file)
- pd.read_csv(file)
- df.to_excel(file)
- df.read_excel(file)
- 同时读入多个表格
```
f = pd.excelwriter(file)
a.to_excel(f, sheet="sheet1")
b.to_excel(f, sheet="sheet2")
```
