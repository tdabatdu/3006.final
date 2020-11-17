'''
Tyler Dabat COMP 3006 Final

'''

import logging
import DataExtractor as de
import CommodityIndex as ci
import PlotHelper as ph
import Plotter as ptr
import Printer as pnr
import numpy as np






#creating commodities
def createCommodities(commodity, logger):
    
    #extracting commodities from source
    commodityData = de.extractCommoditiesData(commodity, logger)
    commodities = ci.Commodities(logger)

    #instantiating commodities
    for row in commodityData.itertuples():
        #print(row)
        #print(row.period, row.year, row.value)
        commodities.addNewCommodity(row.series_id, commodity, row.year, row.period, row.value, logger)
        
    return commodities


#evaluate and display plot
def displayPlot(commodities, plotType, logger):
    
    
    if plotType == 'flat':
        logger.debug('flat chosen')
        
        x,y = ph.createFlatData(commodities, logger)
        ptr.plotFlatData(x,y, logger)
        
        
        
    elif plotType == 'nomchge':
        data = ph.createFlatData(commodities, logger)
        ptr.plotNominalData(data, logger)
        
        logger.debug('Nominal Change chosen')
        
    elif plotType == 'perchge':
        data = ph.createPercentageData(commodities, logger)
        ptr.plotPercentageData(data, logger)
        
        logger.debug('Percentage Change chosen')
        
    
    elif plotType == None:
        logger.info("No plot chosen")
        logger.debug("Plot input Null")
    
    else:
        logger.error('plot display type invalid')
        
    
    return x,y
        
    
    

def printPlot(output, outputType, logger):
    
    if outputType == 'print':
        logger.debug('Printing output')
        
        pnr.printOutput(output, outputType, logger)
        
    elif outputType == 'sys':
        logger.debug('sys stdout chosen')
        
    elif outputType == None:
        logger.debug('No outputType chosen')
        logger.info('No output chosen')
        
    else:
        logger.error('Problem with outputType processing')






















def processCommodities(commodity, plot, outputType, logger):
    commodities = createCommodities(commodity, logger)
    x,y = displayPlot(commodities, plot, logger)
    
    #Numpy used here!!-------------------------------------------------------------
    output = [np.column_stack((x,y))]

    pnr.printOutput(output, outputType, logger)
        
    
    
    
    
    
    
    
    