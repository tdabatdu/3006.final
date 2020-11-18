'''
Tyler Dabat COMP 3006 Final

'''


import logging
import numpy as np
import copy
from collections import defaultdict, OrderedDict
from statistics import mean


def createFlatData(commodities, logger):
    tempDict = defaultdict(lambda: [])
    
    for commodity in commodities._getCommodities(logger):
        tempDict[commodity.year].append(commodity.indexValue)
        
    
    for key in tempDict:
        tempDict[key] = mean(tempDict[key])
        
    indexList = sorted(tempDict.items())
    x,y = zip(*indexList)  
     
    
    return x,y

    


def createNomialData(commodities, logger):
    tempDict = defaultdict(lambda: [])
    
    for commodity in commodities._getCommodities(logger):
        tempDict[commodity.year].append(commodity.indexValue)
    
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


def createPercentageData(commodities, logger):
    tempDict = defaultdict(lambda: [])
    
    for commodity in commodities._getCommodities(logger):
        tempDict[commodity.year].append(commodity.indexValue)
        
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


