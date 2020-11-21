'''
Technical Lead: Tyler Dabat
Contributor: Travis Hammond
COMP 3006 Final
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
    parser.add_argument('-c', '--commodity', dest = 'commodity', action = 'store', metavar = '<commodity>', choices = ['all', 'pulp', 'metals', 'minerals', 'transportation', 'processedFoods', 'textile', 'leather', 'fuels', 'chemicals', 'rubber', 'lumber'])
    parser.add_argument('-p', '--plot', dest = 'plot', action = 'store', metavar = '<plotchoice>', choices = ['flat', 'nomchge', 'perchge' ], help = 'flat: average index year over year, nomchge: nominal change in the current year vs the previous, perchge: percentage change year over year')
    parser.add_argument('-o', '--output', dest = 'out', action = 'store', choices = ['print', 'sys'], help = 'To either print or pipe through sys')
    parser.add_argument('-g', '--grouping', dest = 'grouping', action = 'store_true', help = 'The presence of this will add services to the plot')
    args = parser.parse_args()
    
    if args.commodity == None:
        print('Commodity is require, please try again.')
        
        raise SystemError
    
    
    execute(args.commodity, args.plot, args.out, args.grouping, logger)
    logger.debug('Execution Context: ' + str(args.commodity) + str(args.plot) + str(args.out))
    







#executing flow
def execute(commodity, plot, output, grouping, logger):
    
    cm.processCommodities(commodity, plot, output, grouping, logger)
    
    return None
    
    
    
    
if __name__ == "__main__":
    logger.info('Main Start')
    main(logger)