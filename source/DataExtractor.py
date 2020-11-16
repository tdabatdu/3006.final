'''
Tyler Dabat COMP 3006 Final

'''

import pandas as pd
import numpy as np
import CommodityIndex as ci
import logging





#predefined commodities
commodityDict = {
    'all': 'https://download.bls.gov/pub/time.series/wp/wp.data.1.AllCommodities',
    'pulp': 'https://download.bls.gov/pub/time.series/wp/wp.data.10.Pulp',
    'metals': 'https://download.bls.gov/pub/time.series/wp/wp.data.11a.Metals10-103',
    'minerals': 'https://download.bls.gov/pub/time.series/wp/wp.data.14.Minerals',
    'transportation': 'https://download.bls.gov/pub/time.series/wp/wp.data.15.Transportation',
    'farmProducts': 'https://download.bls.gov/pub/time.series/wp/wp.data.2.FarmProducts',
    'prrocessedFoods': 'https://download.bls.gov/pub/time.series/wp/wp.data.3.ProcessedFoods',
    'textile': 'https://download.bls.gov/pub/time.series/wp/wp.data.4.Textile',
    'leather': 'https://download.bls.gov/pub/time.series/wp/wp.data.5.Leather',
    'fuels': 'https://download.bls.gov/pub/time.series/wp/wp.data.6.Fuels',
    'chemicals': 'https://download.bls.gov/pub/time.series/wp/wp.data.7.Chemicals',
    'rubber': 'https://download.bls.gov/pub/time.series/wp/wp.data.8.Rubber',
    'lumber': 'https://download.bls.gov/pub/time.series/wp/wp.data.9.Lumber',
    
    }



def extractCommoditiesData(commodityType, logger):
    try:
        data = pd.read_csv(commodityDict[commodityType], sep='\t')
        data.columns = ['series_id', 'year', 'period', 'value', 'foot']
        
        logger.info('Address: ' + commodityDict[commodityType])
        logger.debug('commodities extracted')
    
    except:
        print('There has been an error in obtaining the commodities.  Please check connection and try again.')
        logger.error("Unable to extract commodity data")
        raise ConnectionError
    
    return data

    
    

