# 3006.final
Tyler Dabat and Travis Hammond's submission for the 3006 final project.  

Data Set
Tyler's Data set: Producer Price Index of Commodities
Travis's Data set: Producer Price Index of Services  
 
Tyler's functionality and data set driven through CommoditesMain.py
Travis's functionality and data set driven through ServicesMain.py

Example Execution:
python CommoditiesMain.py -c pulp -p flat -o sys -g

-c(required)  It is the Producer Price Index to be show.  options: 'all', 'pulp', 'metals', 'minerals', 'transportation', 'processedFoods', 'textile', 'leather', 'fuels', 'chemicals', 'rubber', 'lumber'
-p(optional) Type of plot to display. options: 'flat', 'nomchge', 'perchge'
Flat is the data as is plotted over time.
nomchange is the nominal change of the index year over year
perchge is the percentage change of the index year over year
-o(optional) Type of output desired either print with 'print' or stdout with 'sys'
-g(optional) The presence of -g will combine both datasets in the plot. It does not combine the datasets in the output.  


