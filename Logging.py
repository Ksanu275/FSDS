#!/usr/bin/env python
# coding: utf-8

# # Logging
# 
# to undserstand where is the issue in the code 
# 
# It helps us to track and monitioring the error in python code
# 
# Log Critical part of system documentation about runttime of status of application.

# 10th Dec Live Class Python logging and debugging
# 
# https://learn.ineuron.ai/lesson/10th-Dec-Live-Class-Python-logging-and-debugging/6394dbb0e714c01445532f66/course/Full-Stack-Data-Science-BootCamp-2.0/62eaa6ba766d6539c53164bd

# In[ ]:





# In[3]:


def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiple(x,y):
    return x*y
def divide(x,y):
    return x/y

num1=20
num2=10

add_result=add(num1,num2)
print(add_result)

sub_result=substract(num1,num2)
print(sub_result)

multi_result=multiple(num1,num2)
print(multi_result)


# Different level of logging
# 
# 1.Debug- point(10)-capture the details of logging - All level are included
# 
# 2.info- point(20)- all level included except debug
# 
# 3.warning-point(30)
# 
# 4.Error-point(40)
# 
# 5.Critical-point(50)
# 

# In[4]:


import logging


# In[10]:


logging.basicConfig(filename='test1.log',level=logging.DEBUG,format='%(acstime)s-%(levelname)s-%(message)s') #Here we can se the level of logging
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiple(x,y):
    return x*y
def divide(x,y):
    return x/y

num1=20
num2=10

add_result=add(num1,num2)
logging.debug(add_result)

sub_result=substract(num1,num2)
logging.info(sub_result)

multi_result=multiple(num1,num2)
print(multi_result)


# In[28]:


import logging
logging.basicConfig(level=logging.DEBUG,format='%(acstime)s - %(levelname)s - %(message)s')
def namecheck(name):
    if len(name)<2:
        logging.debug('checking name length')
        return 'name is inavaild'
    elif name.isspace():
        logging.debug('checking name has space')
        return 'vaild name'
    elif name.isalpha():
        logging.debug('checking name is alphabet')
        return 'name is valid'
    elif name.replace(' ','').isalpha():
        logging.debug('checking for full name and all the condition satisfied')
        return 'name is valid'
    else:
        logging.debug('Failed to check')
        return 'inavaild name'


# In[29]:


namecheck('kumar sanu')


# Create a logger in the code and create one function which ccan take any number of arguements and it will return the sum of it and capture the logging 

# In[38]:


import logging
logging.basicConfig(level=logging.INFO, format='%(acstime)s: %(levelname)s : %(message)s')
def addition(*args):
    logging.info('this is my addition function')
    num1=0
    for i in args:
        logging.info(str(i))
        num1=num1+i
    return num1


# In[39]:


addition(1,2,3)


# In[37]:


import def_inside_def_function


# If we want to use some other.py file we will be using (import .py (file name)

# # How to create logger from scratch

# get logger help us to create different logging in different file 
# 
# lo

# In[49]:


logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f=logging.Formatter('%(acstime)s: %(levelname)s : %(message)s')
fh=logging.FileHandler("employee.log")
fh.setFormatter(f)
logger.addHandler(fh)


def addition(*args):
    logging.info('this is my addition function')
    num1=0
    for i in args:
        logging.info(str(i))
        num1=num1+i
    return num1


# In[50]:


addition(1,2,3)


# In[51]:


import logging

#create custom logger
logger=logging.getLogger(__name__)

#create handler
c_handler=logging.StreamHandler()
f_handler=logging.FileHandler('xyx.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

#create formatter and add it to handler

c_format=logging.Formatter('%(acstime)s: %(levelname)s : %(message)s')
f_format=logging.Formatter('%(acstime)s: %(levelname)s : %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

#Add Handler to the logger

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('this is a warning')
logger.error('This is error')


# In[53]:


logger=logging.getLogger(__name__)
handler=logging.StreamHandler()

formatter=logging.Formatter('%(acstime)s: %(levelname)s : %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.setLevel(logging.INFO)

def div(dividend,divisor):
    try:
        
        logger.info(f'Dividing {dividend} by {divisor}')
        return dividend/divisor
    except ZeroDivisionError:
        logger.info("Zero division error")


# In[56]:


print(div(2,2))

