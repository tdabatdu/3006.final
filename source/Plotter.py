'''
Tyler Dabat COMP 3006 Final

'''
import logging
import matplotlib.pyplot as plt

def plotFlatData(x,y, logger):
    
    plt.plot(x,y)
    plt.xlabel('Year')
    plt.ylabel('Index Value')
    plt.title('Index Value Over Time')
    plt.show()
    return None

def plotNominalData(data, logger):
    
    return None

def plotPercentageData(data, logger):
    
    return None