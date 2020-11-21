'''
Tyler Dabat COMP 3006 Final

'''


import logging
import numpy as np
import copy
from collections import defaultdict, OrderedDict
from statistics import mean

#prepping flat data for plotting
def createFlatData(commodities, logger):
    tempDict = defaultdict(lambda: [])
    
    for commodity in commodities._getCommodities(logger):
        tempDict[commodity.year].append(commodity.indexValue)
        
    
    for key in tempDict:
        tempDict[key] = mean(tempDict[key])
      
      #sorting dict  
    indexList = sorted(tempDict.items())
    x,y = zip(*indexList)  
     
    
    return x,y

    


def createNomialData(commodities, logger):
    tempDict = defaultdict(lambda: [])
    
    for commodity in commodities._getCommodities(logger):
        tempDict[commodity.year].append(commodity.indexValue)
    
    #pre-sorting so loop works chronologically
    sortedDict = OrderedDict(sorted(tempDict.items()))
        
    #setting value for first year
    earliestYear = min(tempDict.keys())
    lastYear = copy.deepcopy(mean(tempDict[earliestYear]))
    #print('earliet Year', lastYear, earliestYear)

    #calculating difference
    for key in sortedDict:
        thisYear = mean(sortedDict[key])
        sortedDict[key] = thisYear - lastYear


        logger.debug(thisYear, lastYear, key)
        
        lastYear = thisYear

    indexList = sorted(sortedDict.items())
    x,y = zip(*indexList)
    
    
    return x,y


def createPercentageData(commodities, logger):
    tempDict = defaultdict(lambda: [])
    
    for commodity in commodities._getCommodities(logger):
        tempDict[commodity.year].append(commodity.indexValue)
        
    #pre-sorting so loop works chronologically
    sortedDict = OrderedDict(sorted(tempDict.items()))
    
    #setting value for first year
    earliestYear = min(tempDict.keys())
    lastYear = copy.deepcopy(mean(tempDict[earliestYear]))
    
    #calculating percentage change
    for key in sortedDict:
        thisYear = mean(sortedDict[key])
        
        if thisYear < lastYear:
            sortedDict[key] = -lastYear / thisYear
        
        else:
            sortedDict[key] = thisYear / lastYear

        logger.debug(thisYear, lastYear, key)
        
        lastYear = thisYear

    indexList = sorted(sortedDict.items())
    x,y = zip(*indexList)
    
    
    return x,y


