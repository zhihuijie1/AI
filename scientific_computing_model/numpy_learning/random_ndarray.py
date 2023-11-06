import numpy as np


# ------------------- random -------------------
def test():
    x = np.random.random(size=4)  # 随机生成一个一维数组有4个元素
    y = np.random.random(size=(3, 4))  # 随机生成一个三行四列的二维数组
    z = np.random.random(size=(2, 2, 2))  # 生成两个两行两列的二维数组
    print(x)  # [0.43748444 0.31316165 0.75512347 0.83041988]
    print(y)
    '''
    [[0.26221976 0.68534481 0.15005012 0.59585608]
    [0.46784864 0.82590267 0.49278113 0.1003134 ]
    [0.66758629 0.35972381 0.90134684 0.61506468]]
    '''
    print(z)
    '''
    [[[0.03016134 0.93801003]
    [0.4377422  0.77839783]]

    [[0.49862417 0.59331288]
    [0.87436223 0.73816752]]]
    '''

    x = np.random.randint(5, 10, size=(3, 4))  # 随机生成[5,10)之间的数字
    print(x)
    '''
    [[6 9 6 7]
    [7 8 6 9]
    [5 8 9 8]]
    '''

    x = np.random.randn(2, 4)  # 符合标准正态分布
    y = np.random.randn(2, 2, 3)
    print(x)
    '''
    [[-2.52628182  0.31678616 -0.02809508 -0.41589727]
    [-1.14239645  0.6182614   0.99580234 -1.79528159]]
    '''
    print(y)
    '''
    [[[-0.00564934  0.43474816 -1.0387402 ]
    [-1.08257134  2.51639821 -0.13413167]]

    [[-0.98813699  0.71185406 -0.47172114]
    [ 0.8586497  -0.65775648 -1.31897014]]]
    '''

    x = np.random.normal(3, 4, size=(2, 3))  # 正太分布/高斯分布，loc:期望 scale:方差,size:维度
    print(x)
    '''
    [[ 4.33044196  7.53083032  2.20060048]
    [-3.20252688  2.42266187  2.11590227]]
    '''

    # ------------------- ndarray -------------------


    # zeros 创建指定大小的数组，数组元素以 0 来填充
    # numpy.zeros(shape, dtype = float, order = 'C')
    x = np.zeros((2, 3), dtype=float)
    print(x)
    '''
    [[0. 0. 0.]
    [0. 0. 0.]]
    '''


    # numpy.ones(shape, dtype = None, order = 'C')
    print(np.ones((5,), dtype=int))  # [1 1 1 1 1]


    # numpy.empty(shape, dtype = float, order = 'C')
    # 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组，里面的元素的值是之前内存的值：
    print(np.empty((2, 3), dtype=float))
    '''
    [[0. 0. 0.]
    [0. 0. 0.]]
    '''

    # np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    # linspace 函数用于创建一个一维数组，数组是一个等差数列构成的
    # num:要生成的等步长的样本数量
    # endpoint 该值为 ture 时，数列中中包含 stop 值，反之不包含，默认是 True。
    # retstep 如果为 True 时，生成的数组中会显示间距，反之不显示。
    print(np.linspace(5, 10, 5, endpoint=True, retstep=True, dtype=int))  # (array([ 5,  6,  7,  8, 10]), 1.25)


    # np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
    # numpy.logspace 函数用于创建一个于等比数列。
    # num 要生成的等步长的样本数量
    # endpoint 该值为 ture 时，数列中中包含 stop 值，反之不包含，默认是 True。
    # base 对数 log 的底数
    print(np.logspace(1, 10, 10, endpoint=True, base=3, dtype=int))
    # [    3     9    27    81   243   729  2187  6561 19683 59049]


if __name__ == '__main__':
    test()
