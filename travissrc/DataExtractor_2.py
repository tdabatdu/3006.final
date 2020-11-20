'''
Technical Lead: Tyler Dabat
Contributor: Travis Hammond
COMP 3006 Final
'''

import pandas as pd
import numpy as np
import ServicesIndex as si
import logging





#predefined services
serviceType = {
    'all': 'https://download.bls.gov/pub/time.series/pc/pc.data.0.Current',
    'pulp': 'https://download.bls.gov/pub/time.series/pc/pc.data.11.Paper',
    'metals': 'https://download.bls.gov/pub/time.series/pc/pc.data.2.Mining',
    'minerals': 'https://download.bls.gov/pub/time.series/pc/pc.data.16.NonmetallicMineral',
    'transportation': 'https://download.bls.gov/pub/time.series/pc/pc.data.22.TransportationEquipment',
    'processedFoods': 'https://download.bls.gov/pub/time.series/pc/pc.data.4.Food',
    'textile': 'https://download.bls.gov/pub/time.series/pc/pc.data.6.Textile',
    'leather': 'https://download.bls.gov/pub/time.series/pc/pc.data.9.Leather',
    'fuels': 'https://download.bls.gov/pub/time.series/pc/pc.data.1.OilAndGas',
    'chemicals': 'https://download.bls.gov/pub/time.series/pc/pc.data.14.Chemicals',
    'rubber': 'https://download.bls.gov/pub/time.series/pc/pc.data.15.PlasticsRubberProducts',
    'lumber': 'https://download.bls.gov/pub/time.series/pc/pc.data.10.Wood',
        #'farmProducts': 'https://download.bls.gov/pub/time.series/wp/wp.data.2.FarmProducts', No services analog in database

    }



def extractServicesData(serviceDict, logger):
    try:
        data = pd.read_csv(serviceDict[serviceType], sep='\t')
        data.columns = ['series_id', 'year', 'period', 'value', 'foot']

        logger.info('Address: ' + serviceDict[serviceType])
        logger.debug('services extracted')

    except:
        print('There has been an error in obtaining the services.  Please check connection and try again.')
        logger.error("Unable to extract service data")
        raise ConnectionError

    return data
