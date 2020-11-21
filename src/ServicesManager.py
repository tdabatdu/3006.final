'''
Technical Lead: Tyler Dabat
Contributor: Travis Hammond
COMP 3006 Final
'''

import logging
import DataExtractor_2 as de
import ServicesIndex as si
import PlotHelper_2 as ph
import plotter_2 as ptr
import printer_2 as pnr
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


#evaluate and display plot
def displayPlot(services, plotType, logger):

    #flat plot type execution
    if plotType == 'flat':
        logger.debug('flat chosen')

        x,y = ph.createFlatData(services, logger)
        ptr.plotFlatData(x,y, logger)
        logger.debug('flat plotter invoked')


    #nominal plot type execution
    elif plotType == 'nomchge':
        logger.debug('nomchge chosen')

        x,y = ph.createNomialData(services, logger)
        ptr.plotNominalData(x,y, logger)
        logger.debug('Nominal plotter invoked')

    #nominal plot type execution
    elif plotType == 'perchge':
        logger.debug('perchge')

        x,y = ph.createPercentageData(services, logger)
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

#Processing all flows from main
def processServices(service, plot, outputType, logger):
    #Creating services
    services = createServices(service, logger)
    logger.info(service + ' Obtained')

    #displaying Plots
    x,y = displayPlot(services, plot, logger)
    logger.debug(plot + ' attempted')

    output = [np.column_stack((x,y))]
    #output handled here
    pnr.printOutput(output, outputType, logger)
