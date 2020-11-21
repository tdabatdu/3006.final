'''
Technical Lead: Tyler Dabat
Contributor: Travis Hammond
COMP 3006 Final
'''
import logging


#logging.basicConfig(filename='CommodityIndex.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
#logger = logging.getLogger()
#streamLog = logging.StreamHandler()
#logger.addHandler(streamLog)

#commodity
class CommodityIndex():
    
    def __init__(self, series, commodity, year, month, indexValue, logger):
        self.series = series
        self.commodity = commodity
        self.year = int(year)
        self.month = int(month[1:])
        self.indexValue = float(indexValue)
        
        
        logger.debug('Commodity Instantiated: ' + str(self))
        
        #Not used
    def __srt__(self):
        return(str(self.commodity + ', ' +  str(self.year) + ', ' +  str(self.month) + ', ' +  str(self.indexValue)))
    



#container for commodities
class Commodities():
    
    def __init__(self, logger):
        self.commodities = []
        
        logger.debug('Commodites container made')
        
        
    def _getCollection(self, logger):
        logger.debug('commodities requested')
        return self.commodities
    
    def addNewCommodity(self, series, commodity, year, month, indexValue, logger):
        newCommodity = CommodityIndex(series, commodity, year, month, indexValue, logger)
        self.commodities.append(newCommodity)
        
        logger.debug('commodity added')
        

