'''
Technical Lead: Travis Hammond
Contributor: Tyler Dabat
COMP 3006 Final
'''

import logging
import DataExtractor as de
import CommodityIndex as ci
import ServicesIndex as si
import PlotHelper as ph
import Plotter as ptr
import Printer as pnr
import numpy as np




#creating services	
def createServices(service, logger):

    #extracting services from source
    serviceData = de.extractServicesData(service, logger)
    services = si.Services(logger)

    logger.debug('Creating Services')
    #instantiating services
    for row in serviceData.itertuples():
        services.addNewService(row.series_id, service, row.year, row.period, row.value, logger)

    logger.debug('Services created')
    return services

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
def displayPlot(commodities, services, plotType, logger):
    
    #flat plot type execution
    if plotType == 'flat':
        logger.debug('flat chosen')
        
        x,y = ph.createFlatData(commodities, logger)
        
        # add conditions to handle Null values
        x2 = None
        y2 = None
        if services != None:
            x2,y2 = ph.createFlatData(services, logger)
        
        #plotting
        ptr.plotFlatData(x,y,x2,y2, logger)
        logger.debug('flat plotter invoked')
        
        
    #nominal plot type execution
    elif plotType == 'nomchge':
        logger.debug('nomchge chosen')
        
        x,y = ph.createNomialData(commodities, logger)
        
        #handling nulls
        x2 = None
        y2 = None
        if services != None:
            x2,y2 = ph.createNomialData(services, logger)
          
        #plotting  
        ptr.plotNominalData(x,y,x2,y2, logger)
        logger.debug('Nominal plotter invoked')
        
    #percentage plot type execution
    elif plotType == 'perchge':
        logger.debug('perchge')
        
        x,y = ph.createPercentageData(commodities, logger)
        
        #handlingNulls
        x2 = None
        y2 = None
        if services != None:
            x2,y2 = ph.createPercentageData(services, logger)
        
        #plotting
        ptr.plotPercentageData(x,y,x2,y2, logger)
        logger.debug('Percentage plotter invoked')
        
    #no plot type
    elif plotType == None:
        x,y = ph.createPercentageData(commodities, logger)
        logger.info("No plot chosen")
        logger.debug("Plot input Null")
        
        
    
    #error in plot type
    else:
        logger.error('plot display type invalid, investigation needed')
        
    
    return x,y

#Processing all flows from main  (Also, numpy is used here
def processCommodities(commodity, plot, outputType, grouping,  logger):
    #Creating commodities
    commodities = createCommodities(commodity, logger)
    logger.info(commodity + ' Obtained')
    
    
    services = None
    
    #creating services
    if grouping == True:
        services = createServices(commodity, logger)
        logger.info('Service: ' + commodity + 'Obtained')
    
    
    #displaying Plots
    x,y = displayPlot(commodities, services, plot, logger)
    logger.debug(str(plot) + ' attempted')
    
    #<<Numpy
    output = [np.column_stack((x,y))]
    #output handled here
    pnr.printOutput(output, outputType, logger)
