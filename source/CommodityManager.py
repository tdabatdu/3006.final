'''
Tyler Dabat COMP 3006 Final

'''

import logging
import DataExtractor as de
import CommodityIndex as ci



#setting up logging



def createCommodities(commodity, logger):
    

    commodityData = de.extractCommoditiesData(commodity, logger)


    commodities = ci.Commodities(logger)

    for row in commodityData.itertuples():
        #print(row)
        #print(row.period, row.year, row.value)
        commodities.addNewCommodity(row.series_id, 'lumber', row.year, row.period, row.value, logger)
    
    for commodity in commodities._getCommodities(logger):
        print(commodity.indexValue)