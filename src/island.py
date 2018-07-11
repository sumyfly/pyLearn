#!/user/bin/python3
# -*-coding:utf-8-*-
# @Author: qsl
# @Date: 2018-03-25 12:19:28
# @Last Modified by:   qsl
# @Last Modified time: 2018-03-25 12:19:28
# @Description: Description

import numpy as np

rn = np.random.random(5 * 5)
island = np.reshape(np.round(rn, 0), (5, 5))
print('Given Island is :\n', island)


def find_independ(matrix):
    independLen = 0
    rowLen, colLen = matrix.shape

    for i in range(rowLen):
        for j in range(colLen):
            if matrix[i, j] != 0:
                independLen += 1
                if i - 1 >= 0 and matrix[i - 1, j] == 1 or \
                        j - 1 >= 0 and matrix[i, j-1] == 1 or \
                        i + 1 <= rowLen - 1 and matrix[i + 1, j] == 1 or \
                        j + 1 <= colLen - 1 and matrix[i, j + 1] == 1:
                    independLen -= 1
    return independLen


print("The independ island number is {}.".format(find_independ(island)))

test = (1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1,
        1)
# x = np.asarray(test).reshape(5, 5))
# print('Test result is ', find_independ(x))
