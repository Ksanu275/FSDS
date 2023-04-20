#!/usr/bin/env python
# coding: utf-8

# # Inheritance
# 
# If we want to use properties of parent class we can use Inheritance.
# 
# Type of Inheritance
# 
# 1.Single Inheritance- one parent class and one child class
# 
# 2.multiple Inheritance-2 parent class and 1 child class
# 
# 3.Multilevel Inheritance-multiple parent  class
# 
# 4.hierarchial Inheritance- one parent class  have multi child class .
# 
# 5.Hybrid Inheritance- Will have parent class and aslo have child class inside one more child class

# # Single Inheritance- one parent class and one child class

# In[1]:


class parent():
    def func1(self):
        print('Hello I from parent class')
class child(parent):
    def func2(self):
        print('Hello I am from child calss')


# In[2]:


test=child()


# In[3]:


test.func1()


# In[4]:


test.func2()


# In[12]:


class Katthaone:
    company_website='www.katthaone.com'
    name='katthaone'
    def details(self):
        print('Details',self.company_website)
class Realestate(Katthaone):
    def __init__(self):
        self.year_of_establishment=2022
    def est_details(self):
        print('est details', self.name,self.year_of_establishment)


# In[13]:


Kth=Realestate()


# In[14]:


Kth.details()


# In[15]:


Kth.est_details()


# # multiple Inheritance:2 parent class and 1 child class

# In[17]:


class Parent1:
    def func1(self):
        print('Hello from parent1')
class Parent2:
    def func2(self):
        print('Hello from parent2')
class child(Parent1,Parent2):
    def func3(self):
        print('hello from child')


# In[18]:


a=child()


# In[19]:


a.func2()


# In[20]:


a.func1()


# In[21]:


a.func3()


# Create a class a person and company and emp and inhertiamce

# In[29]:


class Person:
    def __init_(self,name,salary,domain):
        self.name=name
        self.salary=salary
        self.domain=domain
    def person_details(self):
        print(f' Employee Name {self.name} salary {self.salary}')
class Company:
    def company(self):
        print('Salary')
        
class Emp(Person,Company):
    def employee(self):
        print(f' Employee Name {self.name} salary {self.salary}')


# In[30]:


a=Emp()


# In[31]:


a.company()


# In[32]:


a.employee()


# # MultiLevel

# In[34]:


class test1:
    def a(self):
        print('test1 from class1')
class test2(test1):
    def b(self):
        print('test2 from class2')
class test3(test2):
    def c(self):
        print('test3 from class3')


# In[36]:


x=test3()


# In[37]:


x.c()


# In[39]:


x.b()


# In[43]:


class Vehicle:
    def info(self):
        print('Inside vehical class')
        
class Car(Vehicle):
    def car_info(self):
        print('Inside car class')

class sports_car(Car):
    def sports(self):
        print('inside the sports car')


# In[44]:


s2=sports_car()


# In[45]:


s2.car_info()


# In[ ]:





# # hierarchial Inheritance

# In[46]:


class Vehicle:
    def info(self):
        print('This is from vehicle class')

class Car(Vehicle):
    def car_info(self,name):
        print('Car Name',name)
class Truck(Vehicle):
    def truck_info(self,name):
        print("truck Name",name)


# In[55]:


x=Car()


# In[51]:


x.car_info('audi')


# In[53]:


t1=Truck()


# In[54]:


t1.truck_info('TATA')


# # Hybrid Inheritance- Will have parent class and aslo have child class inside one more child class

# In[63]:


class Vehicle:
    def info(self):
        print('This is from vehicle class')

class Car(Vehicle):
    def car_info(self,name):
        print('Car Name',name)
class Truck(Vehicle):
    def truck_info(self,name):
        print("truck Name",name)
class sports(Car,Truck):
    def sports_car(self):
        print('inside form sports class')


# In[61]:


a=sports()


# In[59]:


a.car_info('Nano')


# In[62]:


a.info()


# # SUPER

# 1.super() is used to extend the funcionality of previous build class
# 
# 2.super function in python is used to access method of immediate parents class

# In[ ]:


class company:
    def company_name(self):
        return "Wells fargo"
    
class Employee(company):
    def info(self):
        c_name=super().company_name()
        print('I work at',c_name)
        


# In[ ]:




