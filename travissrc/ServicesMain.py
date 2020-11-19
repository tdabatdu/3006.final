'''
Technical Lead: Tyler Dabat
Contributor: Travis Hammond
COMP 3006 Final
'''

import logging
import ServicesManager as sm
import argparse as ap


#setting up logging
logging.basicConfig(filename='ServiceProcessing.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger()
streamLog = logging.StreamHandler()
logger.addHandler(streamLog)


def main(logger):
    logger.info('Main executed')

    parser = ap.ArgumentParser(description = 'Analyze Service Price Index')
    parser.add_argument('-s', '--service', dest = 'service', action = 'store', metavar = '<service>', choices = ['all', 'pulp', 'metals', 'minerals', 'transportation', 'farmProducts', 'processedFoods', 'textile', 'leather', 'fuels', 'chemicals', 'rubber', 'lumber'])
    parser.add_argument('-p', '--plot', dest = 'plot', action = 'store', metavar = '<plotchoice>', choices = ['flat', 'nomchge', 'perchge' ], help = 'flat: average index year over year, nomchge: nominal change in the current year vs the previous, perchge: percentage change year over year')
    parser.add_argument('-o', '--output', dest = 'out', action = 'store', choices = ['print', 'sys'], help = 'To either print or pipe through sys')
    args = parser.parse_args()


    execute(args.service, args.plot, args.out, logger)
    logger.debug('Execution Context: ' + str(args.service) + str(args.plot) + str(args.out))








#executing flow
def execute(service, plot, output, logger):

    sm.processServices(service, plot, output, logger)

    return None




if __name__ == "__main__":
    logger.info('Main Start')
    main(logger)
