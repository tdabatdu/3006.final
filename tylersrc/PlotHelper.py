'''
Tyler Dabat COMP 3006 Final

'''


import logging
import numpy as np
from collections import defaultdict
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
    
    return 'nominal data'


def createPercentageData(commodities, logger):
    
    return 'percentage data'