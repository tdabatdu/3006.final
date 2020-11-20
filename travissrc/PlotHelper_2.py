'''
Technical Lead: Tyler Dabat
Contributor: Travis Hammond
COMP 3006 Final
'''


import logging
import numpy as np
import copy
from collections import defaultdict, OrderedDict
from statistics import mean


def createFlatData(services, logger):
    tempDict = defaultdict(lambda: [])

    for services in services._getServices(logger):
        tempDict[services.year].append(services.indexValue)


    for key in tempDict:
        tempDict[key] = mean(tempDict[key])

    indexList = sorted(tempDict.items())
    x,y = zip(*indexList)


    return x,y

def createNomialData(services, logger):
    tempDict = defaultdict(lambda: [])

    for service in services._getServices(logger):
        tempDict[services.year].append(services.indexValue)

    sortedDict = OrderedDict(sorted(tempDict.items()))

    earliestYear = min(tempDict.keys())
    lastYear = copy.deepcopy(mean(tempDict[earliestYear]))
    print('earliet Year', lastYear, earliestYear)


    for key in sortedDict:
        thisYear = mean(sortedDict[key])
        sortedDict[key] = thisYear - lastYear
        print(thisYear, lastYear, key)

        lastYear = thisYear

    indexList = sorted(sortedDict.items())
    x,y = zip(*indexList)


    return x,y


def createPercentageData(services, logger):
    tempDict = defaultdict(lambda: [])

    for service in services._getServices(logger):
        tempDict[services.year].append(services.indexValue)

    sortedDict = OrderedDict(sorted(tempDict.items()))

    earliestYear = min(tempDict.keys())
    lastYear = copy.deepcopy(mean(tempDict[earliestYear]))


    for key in sortedDict:
        thisYear = mean(sortedDict[key])
        sortedDict[key] = thisYear / lastYear
        print(thisYear, lastYear, key)

        lastYear = thisYear

    indexList = sorted(sortedDict.items())
    x,y = zip(*indexList)


    return x,y
