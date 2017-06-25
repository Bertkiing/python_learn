import numpy as np  # 导入Numpy库
from numpy import *
import matplotlib.pyplot as plt
dataSet = [[-0.017,14.05],[-1.39,4.66],
                    [-0.75,6.5],[-1.32,7.15],
                    [0.42,11.05],[0.40,7.0],
                    [0.66,12.75]]

#将数据集转换为Numpy矩阵,并转置
dataMat = mat(dataSet).T

plt.scatter(dataMat[0],dataMat[1],c='red',marker='o')  #绘制数据集散点集

#绘制直线图形
X = np.linspace(-2,2,10)

#建立线性方程
Y = 2.8*X + 9

plt.plot(X,Y)  #绘制直线图
plt.show()      # 显示绘制后的结果