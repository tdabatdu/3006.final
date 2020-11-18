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

def plotNominalData(x,y, logger):
    
    plt.plot(x,y)
    plt.xlabel('Year')
    plt.ylabel('Difference in Index Value From Previous Year')
    plt.title('Difference in Index Value Over Time')
    plt.show()
    
    
    return None

def plotPercentageData(x,y, logger):
    
    plt.plot(x,y)
    plt.xlabel('Year')
    plt.ylabel('Percentage Change in Index Value From Previous Year')
    plt.title('Percentage Change in Index Value Over Time')
    plt.show()
    
    return None