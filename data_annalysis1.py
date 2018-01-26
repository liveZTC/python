# -*- coding:utf-8 -*-
#读取文件
import pandas as pd
from scipy import stats as ss
import matplotlib.pyplot  as plt
import seaborn as sns


data_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
df = pd.read_csv(data_url)    

#输出文件前五行
#print df.head()
#print df.head(n=10)

#输出文件后五行
#print df.tail()
#print df.tail(n=10)

#csv文件的列名
#print df.columns

#csv文件的行
#print df.index   

#T置换文件行和列
#print  df.T   

#使用iloc或ix提取某些行或列,ix较为稳定
# print df.ix[:,1].head()
# print df.ix[:5,1]
# print df.ix[10:20,:3]
# print df.ix[10:20, ['Abra', 'Apayao', 'Benguet']]
#print df.ix[:,1].tail()

#drop用来舍弃某些行或列，axis表示舍弃行还是列（0为行，1为列）
#print df.columns[[1,2]]
# print df.drop(df.columns[[1,2]],axis=1).head()
# print df.ix[:,2].head()

#对数据的统计特性进行描述
#print df.describe()

#print ss.ttest_1samp(a = df.ix[:, 'Abra'], popmean = 15000)
# OUTPUT
#(-1.1281738488299586, 0.26270472069109496)
#元组第一个元素为t（数组或浮点数，统计量），第二个为prob(p，数组或浮点数，双侧概率值)。

#plt.show(df.plot(kind='box'))

#plt.show(sns.boxplot(df,width=.5,color="palettes"))

#plt.show(sns.violinplot(df,width=.5))

#plt.show(sns.distplot(df.ix[:,2], rug = True, bins = 15))

# with sns.axes_style("white"):
#     plt.show(sns.jointplot(df.ix[:,1], df.ix[:,2], kind = "kde"))

#plt.show(sns.lmplot("Benguet", "Ifugao", df))
