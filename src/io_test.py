#!/user/bin/python3
# -*-coding:utf-8-*-
# @Author: qsl
# @Date: 2018-04-22 22:36:35
# @Last Modified by:   qsl
# @Last Modified time: 2018-04-22 22:36:35
# @Description: Description

import os


def main():
    curPath = os.path.dirname(os.path.abspath(__file__))
    inputFileName = os.path.join(curPath, ('dict_test.py'))
    outputFileName = os.path.join(curPath, ('output.txt'))
    print('fileName: %s' % inputFileName)
    with open(inputFileName, 'r') as inputFile:
        with open(outputFileName, 'w+') as outputFile:
            for l in inputFile:
                outputFile.write(l)


def write():
    curPath = os.path.dirname(os.path.abspath(__file__))
    fileName = os.path.join(curPath, ('output.txt'))
    print('fileName: %s' % fileName)
    lines = ['line1', 'line2']
    with open(fileName, 'w+') as f:
        f.writelines('%s\n' % l for l in lines)


if __name__ == '__main__':
    main()
    # write()
