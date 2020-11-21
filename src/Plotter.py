'''
Technical Lead: Tyler Dabat
Contributor: Travis Hammond
COMP 3006 Final
'''
import logging
import matplotlib.pyplot as plt

def plotFlatData(x,y,x2, y2, logger):
    
    plt.plot(x,y, label = 'Commodities')
    
    if x2 and y2 != None:
        plt.plot(x2,y2, label = "Services")
        
    plt.xlabel('Year')
    plt.ylabel('Index Value')
    plt.title('Producer Price Index Value Over Time')
    plt.legend()
    plt.show()
    return None

def plotNominalData(x,y, x2, y2, logger):
    
    plt.plot(x,y, label = 'Commodities')
    
    if x2 and y2 != None:
        plt.plot(x2,y2, label = "Services")
    
    plt.xlabel('Year')
    plt.ylabel('Difference in Index Value')
    plt.title('Difference in Producer Price Index Value Over Time')
    plt.legend()
    plt.show()
    
    
    return None

def plotPercentageData(x,y,x2, y2, logger):
    
    plt.plot(x,y, label = 'Commodities')
    
    if x2 and y2 != None:
        plt.plot(x2,y2, label = "Services")
    
    plt.xlabel('Year')
    plt.ylabel('Percentage Change in Index Value')
    plt.title('Percentage Change in Producer Price Index Value Over Time')
    plt.legend()
    plt.show()
    
    return None