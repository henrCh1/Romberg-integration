# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:16:57 2023

"""

# 定义函数f(x)
def f(x):
    f = 0.02792*(2-x)/(1.449*x+1)**0.8/(1-x)**1.2/x
    return f

# 定义梯形法积分
def T(n,a,b):
    h = (b-a)/n  # 计算步长
    TT = 0  # 初始化梯形积分结果
    for i in range(n):
        # 使用梯形积分算法计算积分值
        TT += 1 / 2 * h * (f(a + i * h) + f(a + (i + 1) * h))
    return TT

# 定义Simpson积分
def S(n,a,b):
    # 使用Simpson积分算法计算积分值I
    I = T(2*n, a, b) + (T(2*n, a, b) - T(n, a, b)) / 3
    return I

# 定义柯特斯积分
def C(n,a,b):
    # 使用复合Simpson积分算法计算积分值C
    C = S(2*n, a, b) + (S(2*n, a, b) - S(n, a, b)) / 15
    return C

n = 1 #初始步长
a = 0.1
b = 0.6
while True:
    R_old = C(2*n, a, b) + (C(2*n, a, b) - C(n, a, b)) / 63  # 计算R_old
    n += 1  # 步长n自增1
    R = C(2*n, a, b) + (C(2*n, a, b) - C(n, a, b)) / 63  # 计算R
    error = abs(R_old - R)  # 计算误差error
    if error <= 10 ** (-5):  # 如果误差小于等于10^(-5)，输出R并退出循环
        print('结果为：', R)
        break
