# OLS = Ordinary Least Square

from numpy import *

def loadDataSet(filename):
    numFeat = len(open(filename).readline().split('\t')) - 1
    dataMat = []
    labelMat = []
    fr = open(filename)

    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat

def standRegres(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, can not do inverse.\n")
        return

    ws = xTx.I * (xMat.T * yMat)
    return ws


xArr, yArr = loadDataSet('ex0.txt')
print(xArr)
print(yArr)

w = standRegres(xArr, yArr)
print(w)