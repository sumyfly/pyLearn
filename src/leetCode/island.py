#!/user/bin/python3
# -*-coding:utf-8-*-
# @Author: qsl
# @Date: 2018-03-25 12:19:28
# @Last Modified by:   qsl
# @Last Modified time: 2018-03-25 12:19:28
# @Description: Description

import numpy as np


def dfs(matrix, visted, i, j):
    rowLen, colLen = matrix.shape
    if i < 0 or i >= rowLen:
        return
    if j < 0 or j >= colLen:
        return
    if matrix[i, j] != 1 or visted[i, j]:
        return
    visted[i, j] = 1  # set matrix[i,j] visted true
    dfs(matrix, visted, i - 1, j)
    dfs(matrix, visted, i + 1, j)
    dfs(matrix, visted, i, j - 1)
    dfs(matrix, visted, i, j + 1)


def find_independ(matrix):
    independLen = 0
    rowLen, colLen = matrix.shape
    # store the matrix visited status
    visted = np.zeros((rowLen, colLen), dtype=int)

    for i in range(rowLen):
        for j in range(colLen):
            if matrix[i, j] != 0 and visted[i, j] == 0:
                # 深度优先
                dfs(matrix, visted, i, j)
                independLen += 1
    return independLen
