'''
Tyler Dabat COMP 3006 Final

'''

import logging
import DataExtractor as de
import CommodityIndex as ci
import PlotHelper as ph
import Plotter as ptr






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
        data = ph.createFlatData(commodities, logger)
        ptr.plotFlatData(data. logger)
        
    elif plotType == 'nomchge':
        data = ph.createFlatData(commodities, logger)
        
    
    
























def showCommodities(commodity, plot, output, logger):
    commodities = createCommodities(commodity, logger)
    
    
    
    
    
    
    
    