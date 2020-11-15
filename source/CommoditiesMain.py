'''
Tyler Dabat COMP 3006 Final

'''

import logging
import CommodityManager as cm

logging.basicConfig(filename='CommodityIndex.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger()
streamLog = logging.StreamHandler()
logger.addHandler(streamLog)


def createCommodities(logger):
    
    