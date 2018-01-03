#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:07:51 2017

@author: nguyentran

Factory method pattern
Essentially, factory method pattern means providing a method to handle object 
instantiation instead of calling constructors

This pattern allows a parent abstract class to defer the instantiation process to its subclasses
The parent class knows when an object must be created, but it does not know which class to use
to create the object. 
Parent class creates an abstract function that handles the creation of the object. Children classes
provide implementation of this creation.

Whenever the parent abstract class requires the instantiation of the product, it can
simply call the factory method.
This approach avoid the use of Class() (i.e., constructor), as the abstract class
does not know which class to instantiate, and the abstract class of the product cannot
be used for instantiation

Generally, parent abstract class belongs to a library or an architectural framework. Children classes
are defined by clients to build applications upon the architectural framework.
"""

from abc import ABC, abstractmethod

#=================================================================
# Product to be used in this example
class AbstractProduct(ABC):
    def __init__(self, product_name):
        self.product_name = product_name
        
    def do_task(self):
        print("Do task in %s" % self.product_name)

class ConcreteProduct1(AbstractProduct):
    product_name = "Product 1"
    def __init__(self):
        AbstractProduct.__init__(self, self.product_name)

class ConcreteProduct2(AbstractProduct):
    product_name = "Product 2"
    def __init__(self):
        AbstractProduct.__init__(self, self.product_name)
        

#=================================================================
# Parent abstract class
class AbstractApplication(ABC):
    def __init__(self):
        """
        Create a product by using the factory method.
        It should be noted that the product needs not to be created here in the 
        constructor. This is just for demonstration
        """
        self.product = self._factory_method()
    
    """
    This abstract method returns a product object. Whenever we need a new object
    of this class hierarchy, instead of calling constructor, which we have no
    idea which one to use at the design time, we call this function. Concrete
    application classes will implement this abstract class with concrete 
    creation method
    """
    @abstractmethod
    def _factory_method(self):
        pass
    
    """
    Noted how the abstract parent class can specify all application logic using the abstract product.
    It only cannot specify the instantiation of this product. 
    """
    def do_task(self):
        self.product.do_task()
    
#=================================================================
# concrete classes
class ConcreteApplication1(AbstractApplication):
    def _factory_method(self):
        return ConcreteProduct1()
    
class ConcreteApplication2(AbstractApplication):
    def _factory_method(self):
        return ConcreteProduct2()
    
#=================================================================
# client
def main():
    app = ConcreteApplication1()
    app.do_task()
    
    app = ConcreteApplication2()
    app.do_task()
    
if __name__ == "__main__":
    main()