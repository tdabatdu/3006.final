'''
Tyler Dabat COMP 3006 Final

'''

import logging
import CommodityManager as cm
import argparse as ap


#setting up logging
logging.basicConfig(filename='CommodityProcessing.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger()
streamLog = logging.StreamHandler()
logger.addHandler(streamLog)


def main(logger):
    logger.info('Main executed')
    
    parser = ap.ArgumentParser(description = 'Analyze Commodity Price Index')
    parser.add_argument('-c', '--commodity', dest = 'commodity', action = 'store', metavar = '<commodity>', choices = ['all', 'pulp', 'metals', 'minerals', 'transportation', 'farmProducts', 'processedFoods', 'textile', 'leather', 'fuels', 'chemicals', 'rubber', 'lumber'])
    parser.add_argument('-p', '--plot', dest = 'plot', action = 'store', metavar = '<plotchoice>', choices = ['flat', 'nomchge', 'perchge' ], help = 'flat: average index year over year, nomchge: nominal change in the current year vs the previous, perchge: percentage change year over year')
    parser.add_argument('-o', '--output', dest = 'out', action = 'store', choices = ['print', 'sys'], help = 'To either print or pipe through sys')
    args = parser.parse_args()
    
    
    execute(args.commodity, args.plot, args.out, logger)
    







#executing flow
def execute(commodity, plot, output, logger):
    
    cm.processCommodities(commodity, plot, output, logger)
    
    
    
    
    
    return 'Place holder'
    
    
    
    
if __name__ == "__main__":
    main(logger)