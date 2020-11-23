'''
Technical Lead: Tyler Dabat
Contributor: Travis Hammond
COMP 3006 Final
'''
import logging

class ServiceIndex():

    def __init__(self, series, service, year, month, indexValue, logger):
        self.series = series
        self.service = service
        self.year = int(year)
        self.month = int(month[1:])
        self.indexValue = float(indexValue)


        logger.debug('Service Instantiated: ' + str(self))


    def __str__(self):
        return(str(self.service + ', ' +  str(self.year) + ', ' +  str(self.month) + ', ' +  str(self.indexValue)))




#container for services
class Services():

    def __init__(self, logger):
        self.services = []

        logger.debug('Services container made')


    def _getCollection(self, logger):

        logger.debug('services requested')
        return self.services

    def generateServices(self):

        return 'Nothing this is where I need to get services'

    def addNewService(self, series, service, year, month, indexValue, logger):
        newService = ServiceIndex(series, service, year, month, indexValue, logger)
        self.services.append(newService)

        logger.debug('service added')
