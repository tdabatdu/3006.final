'''
Technical Lead: Tyler Dabat
Contributor: Travis Hammond
COMP 3006 Final
'''
import logging
from sys import stdout



def printOutput(output, outputType, logger):
    
    if outputType == 'print':
        for item in output:
            print(item)
            
    elif outputType == 'sys':
        for item in output:
            stdout.write(str(item))
            
    elif outputType == None:
        logger.debug('No outputType chosen')
        logger.info('No output chosen')
        
    else:
        logger.error('Problem with outputType processing')
        