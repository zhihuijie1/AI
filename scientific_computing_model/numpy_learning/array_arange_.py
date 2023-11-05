import numpy as np


def test1():
    # ---------------------- array ----------------------
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    arr = np.array(list)
    print(arr)  # [1 2 3 4 5]
    print("arr的维度--", arr.shape)  # arr的维度-- (5,) 五行0列，一维数组

    arr2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print(arr2)
    '''
    [[0 1 2]
    [3 4 5]
    [6 7 8]]'''
    print(arr2.shape)  # (3, 3) 三行三列

    arr2 = np.array(list, ndmin=3)  # ndmin:用来指定数组的最小维度
    print(arr2)  # [[[1 2 3 4 5 6 7 8 9]]]

    arr2 = np.array(list, dtype=float)  # dtype:指定数组中元素的类型
    print(arr2)  # [1. 2. 3. 4. 5. 6. 7. 8. 9.]
    print(list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # ---------------------- arange ----------------------

    x = np.arange(0, 10, 2, dtype=int)  # numpy.arange(start, stop, step, dtype) step默认是1
    y = np.arange(10, 30, 5, dtype=complex)  # 注意范围是左闭右开  complex是复数
    z = np.array([np.arange(1, 4), np.arange(4, 7), np.arange(7, 10)])
    print(x)  # [0 2 4 6 8]
    print(y)  # [10.+0.j 15.+0.j 20.+0.j 25.+0.j]
    print(z)
    '''
    [[1 2 3]
    [4 5 6]
    [7 8 9]]'''


if __name__ == '__main__':
    test1()
