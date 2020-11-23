import unittest
import ServicesIndex
import logging

logging.basicConfig(filename='CommodityProcessing.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger()
streamLog = logging.StreamHandler()
logger.addHandler(streamLog)

class TestSI(unittest.TestCase):
    def test_create_si(self):
        SI_A = ServicesIndex.ServicesIndex(1, 'barging', '1984', 'M06', '50.3', logger)
        SI_B = ServicesIndex.ServicesIndex(1, 'HVAC', '1998', 'M08', '256.03', logger)

        self.assertEqual(SI_A.service, 'barging')
        self.assertEqual(SI_A.year, 1984)
        self.assertEqual(SI_A.month, 6)
        self.assertEqual(SI_A.indexValue, 256.03, logger)

        self.assertNotEqual(SI_B.service, 'HVAX')
        self.assertNotEqual(SI_A.year, 1985)
        self.assertNotEqual(SI_A.month, 7)
        self.assertNotEqual(SI_A.indexValue, 256.02, logger)

    def testServices(self):
        services = ServicesIndex.ServiceIndex(logger)

        commodities.addNewService(1, 'pulp', '1995', 'M10', '126.32', logger)
        commodities.addNewService(1, 'metals', '2005', 'M04', '200.65', logger)
        commodities.addNewService(1, 'food', '2010', 'M09', '151.249', logger)

        count = 0
        for commodity in commodities._getCommodities(logger):
            count +=1

        self.assertEqual(3, count)
        self.assertNotEqual(4, count)
