from numpy import *
import operator
import os # 见 handwritingClassTest()

def createDataSet():
    group = array([(1.0, 1.1),(1.0, 1.0),(0, 0),(0, 0.1)])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX,dataSet,labels, k):
    dataSetSize = dataSet.shape[0] # 4
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqdiffMat = diffMat ** 2
    sqDistances = sqdiffMat.sum(axis = 1) # 按行相加
    distances = sqDistances ** 0.5
    sortedDistIndecies = distances.argsort() # sort
    classCount = {} # dictionary
    for i in range(k):
        voteIlabel = labels[sortedDistIndecies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedclassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortedclassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classlabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classlabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classlabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / (maxVals - minVals)
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.10
    datingDateMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDateMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0

    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs : m, :], datingLabels[numTestVecs : m], 3)
        print("the output of KNN is: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))

def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input('percentage of time spent palying video games?'))
    ffMiles = float(input('frequent flier miles consumed per year?'))
    iceCream = float(input('liters of ice cream consumed per year?'))
    datingDateMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDateMat)
    inArr = array([percentTats, ffMiles, iceCream])
    classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)
    print('You will probably like this person:', resultList[classifierResult-1])

def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, i*32 + j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = os.listdir('./digits/trainingDigits') # 获取文件夹下所有文件名
    testFileList = os.listdir('./digits/testDigits') # 获取文件夹下所有文件名
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))

    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('./digits/trainingDigits/%s'% fileNameStr)

    errorCount = 0.0
    mTest = len(testFileList)

    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('./digits/testDigits/%s'%fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print('the output of KNN is %d, the real answer is: %d'% (classifierResult,classNumStr))
        if classifierResult != classNumStr:
            errorCount += 1
    print('the total number of errors is %d\n' % errorCount)
    print('the total error rate is %f\n'% (errorCount / float(mTest)))










# 测试函数classify0
group, labels = createDataSet()
print(group)
print(labels)
print(classify0([2,0], group, labels, 3))

# 测试函数file2matrix
datingDateMat, datingLabels = file2matrix('datingTestSet2.txt')
print(datingDateMat)
print(datingLabels)

# 测试autoNorm
normMat, ranges, minVals = autoNorm(datingDateMat)
print(normMat)
print(ranges)
print(minVals)

# 测试 KNN 的错误率
datingClassTest()

# 测试某个人是否是你喜欢的
#classifyPerson()

# 测试img2vector
testVector = img2vector('./digits/testDigits/0_13.txt')
print(testVector[0, 0:31])

handwritingClassTest()