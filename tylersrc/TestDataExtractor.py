'''
Tyler Dabat COMP 3006 Final

'''
import unittest
import logging
import DataExtractor
import pandas as pd

logging.basicConfig(filename='CommodityProcessing.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger()
streamLog = logging.StreamHandler()
logger.addHandler(streamLog)


class Test(unittest.TestCase):


    def testExtractCommoditiesData(self):
        data = DataExtractor.extractCommoditiesData('lumber', logger)
        
        data2 = pd.read_csv('https://download.bls.gov/pub/time.series/wp/wp.data.9.Lumber', sep='\t')
        data2.columns = ['series_id', 'year', 'period', 'value', 'foot']
        
        self.assertTrue(data.equals(data2))
        
    
    def testExtractCommoditiesData2(self):
        data3 = DataExtractor.extractCommoditiesData('pulp', logger)
        
        data4 = pd.read_csv('https://download.bls.gov/pub/time.series/wp/wp.data.10.Pulp', sep='\t')
        data4.columns = ['series_id', 'year', 'period', 'value', 'foot']
        
        self.assertTrue(data3.equals(data4))
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()