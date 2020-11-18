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
    
    logger.debug('Creating Commodities')
    #instantiating commodities
    for row in commodityData.itertuples():
        commodities.addNewCommodity(row.series_id, commodity, row.year, row.period, row.value, logger)
        
    logger.debug('Commodities created')
    return commodities


#evaluate and display plot
def displayPlot(commodities, plotType, logger):
    
    #flat plot type execution
    if plotType == 'flat':
        logger.debug('flat chosen')
        
        x,y = ph.createFlatData(commodities, logger)
        ptr.plotFlatData(x,y, logger)
        logger.debug('flat plotter invoked')
        
        
    #nominal plot type execution
    elif plotType == 'nomchge':
        logger.debug('nomchge chosen')
        
        x,y = ph.createNomialData(commodities, logger)
        ptr.plotNominalData(x,y, logger)
        logger.debug('Nominal plotter invoked')
        
    #nominal plot type execution
    elif plotType == 'perchge':
        logger.debug('perchge')
        
        x,y = ph.createPercentageData(commodities, logger)
        ptr.plotPercentageData(x,y, logger)
        
        logger.debug('Percentage plotter invoked')
        
    #no plot type
    elif plotType == None:
        logger.info("No plot chosen")
        logger.debug("Plot input Null")
    
    #error in plot type
    else:
        logger.error('plot display type invalid, investigation needed')
        
    
    return x,y
        
    
    ''' Probably need to delete this
#printing the plot
def printPlot(output, outputType, logger):
    
    if outputType == 'print':
        logger.debug('Printing output')
        
        pnr.printOutput(output, outputType, logger)
        
        logger.debug('printing ouput invoked')
        
    elif outputType == 'sys':
        logger.debug('sys stdout chosen')
        
        pnr.printOutput(output, outputType, logger)
        
    elif outputType == None:
        logger.debug('No outputType chosen')
        logger.info('No output chosen')
        
    else:
        logger.error('Problem with outputType processing')


'''
#Processing all flows from main  (Also, numpy is used here!!!!!!!!!!!!!!!!!!!!!!!!!!!------------------ yay!
def processCommodities(commodity, plot, outputType, logger):
    #Creating commodities
    commodities = createCommodities(commodity, logger)
    logger.info(commodity + ' Obtained')
    
    #displaying Plots
    x,y = displayPlot(commodities, plot, logger)
    logger.debug(plot + ' attempted')
    
    #Numpy used here!!-------------------------------------------------------------
    output = [np.column_stack((x,y))]
    #output handled here
    pnr.printOutput(output, outputType, logger)
        
    
    