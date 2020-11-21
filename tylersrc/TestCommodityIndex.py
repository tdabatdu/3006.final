'''
Tyler Dabat COMP 3006 Final

'''
import unittest
import CommodityIndex
import logging

logging.basicConfig(filename='CommodityProcessing.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger()
streamLog = logging.StreamHandler()
logger.addHandler(streamLog)


class Test(unittest.TestCase):




    def testCommodityIndex(self):
        commodity1 = CommodityIndex.CommodityIndex(1,'TestCom', '1999', 'M12', '10.1', logger)
        commodity2 = CommodityIndex.CommodityIndex(1,'TestCom2', '2020', 'M08', '1000.1234', logger)
        
        self.assertEqual(commodity1.commodity, 'TestCom')
        self.assertEqual(commodity1.year, 1999)
        self.assertEqual(commodity1.month, 12)
        self.assertEqual(commodity1.indexValue, 10.1)
        
        self.assertEqual(commodity2.commodity, 'TestCom2')
        self.assertEqual(commodity2.year, 2020)
        self.assertEqual(commodity2.month, 8)
        self.assertEqual(commodity2.indexValue, 1000.1234)
        
        
    def testCommodities(self):
        commodities = CommodityIndex.Commodities(logger)
        
        commodities.addNewCommodity(1, 'Test', '1920', 'M04', '14.231563', logger)
        commodities.addNewCommodity(1, 'Test2', '1920', 'M04', '14.231563', logger)
        commodities.addNewCommodity(1, 'Test3', '1920', 'M04', '14.231563', logger)
        
        count = 0
        for commodity in commodities._getCommodities(logger):
            count +=1
            
        self.assertEqual(3, count)
        
        
    def testCommodities2(self):
        commodities = CommodityIndex.Commodities(logger)
        
        commodities.addNewCommodity(1, 'Test', '1920', 'M04', '14.231563', logger)
        commodities.addNewCommodity(1, 'Test2', '1921', 'M04', '14.231563', logger)
        commodities.addNewCommodity(1, 'Test3', '1922', 'M04', '14.231563', logger)
        
        for commodity in commodities._getCommodities(logger):
            if commodity.commodity == 'Test':
                self.assertEqual(1920, commodity.year)
                
            elif commodity.commodity == 'Test2':
                self.assertEqual(1921, commodity.year)
                
            elif commodity.commodity == 'Test3':
                self.assertEqual(1922, commodity.year)
            else:
                self.assertTrue(False)
        
            
        
        
        
        
                


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()