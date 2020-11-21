'''
Tyler Dabat COMP 3006 Final

'''
import unittest
import PlotHelper as ph
import CommodityIndex
import logging

logging.basicConfig(filename='CommodityProcessing.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger()
streamLog = logging.StreamHandler()
logger.addHandler(streamLog)


class Test(unittest.TestCase):
    def setUp(self):
        self.commodities = CommodityIndex.Commodities(logger)
        self.commodities.addNewCommodity(1, 'pulp', 1920, 'M12', 100, logger)
        self.commodities.addNewCommodity(1, 'pulp', 1921, 'M11', 101, logger)
        self.commodities.addNewCommodity(1, 'pulp', 1922, 'M10', 120, logger)
        self.commodities.addNewCommodity(1, 'pulp', 1923, 'M09', 130, logger)
        self.commodities.addNewCommodity(1, 'pulp', 1924, 'M08', 140, logger)
        self.commodities.addNewCommodity(1, 'pulp', 1925, 'M07', 141, logger)
        
    def tearDown(self):
        self.commodities = None
        
    

    def testCreateFlatDataa(self):
        x,y = ph.createFlatData(self.commodities, logger)
        
        self.assertEqual((1920,1921,1922,1923,1924,1925), x)
        self.assertEqual((100,101,120,130,140,141), y)
        
    
    
    def testCreateNominalData(self):
        x,y = ph.createNomialData(self.commodities, logger)
        
        self.assertEqual((1920,1921,1922,1923,1924,1925), x)
        self.assertEqual((0.0,1.0,19.0,10.0,10.0,1.0),y)
        
    
    def testCreatePercentageData(self):
        x,y = ph.createPercentageData(self.commodities, logger)
        
        self.assertEqual((1920,1921,1922,1923,1924,1925), x)

        
        assertionPlaceholder = (1.000, 1.0100, 1.1881188, 1.083333333, 1.0769230, 1.00714285)
        i = 0 
        for number in assertionPlaceholder:
            self.assertAlmostEqual(number, y[i], 2)
            i += 1


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()