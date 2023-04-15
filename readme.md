#README.md- To write any information

#END to END Automation

#Create a environment

''' conda create -p venv python==3.8 ''' ' create requirements.txt

'''# requirement.txt file require to access all packages and we will import the this packages from this file#'''

''' To install requirement.txt we will use -pip install -r requirement.txt

'''

#Create setup.py file ''' why we require- if we want to convert this folder into packages

'''

-e . means when we try to install packages from requirements.txt and it found -e . then setup.py file get triggered

#if we removed -e . then it will not triggered the setup.py file ''' #If we independently want insatll setup.py file

''' python setup.py install

'''

When ever we start project we will create src folder """ My entire project lifecycle should be run inside the src folder """

init.py why we required run -bcz this is also package and we want use the fucionality in other folder ''' Basically used to importing the packages in other folder '''

EDA and featuring engerining we required so we will create another folder - notebook

In src ''' we will create py file

init.py , excpetion.py, logger.py

utils.py - we use this file for any generic functionallity that we will create and want to use this funcionality during our priject '''

#Add component folder in src ''' init.py data_ingestion.py data_transformation.py model_trainer.py '''

#Add pipeline in src ''' init.py

exception.py

logger.py

'''
