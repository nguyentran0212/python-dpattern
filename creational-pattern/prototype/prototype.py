#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 09:31:05 2018

@author: nguyentran

Essentially, this pattern creates new objects by cloning existing, instantiated
objects instead of invoking the constructor of the class directly

This pattern is useful in the case where creating a new object from scratch is 
costly, yet new objects are slightly different from existing ones (so pooling
is not viable)
"""

# Python provide copy library to clone objects
import copy
from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    """
    NOTE: the use of abstract class here is not a part of prototype pattern.
    It is used to show how prototype pattern is integrated into abstract
    factory pattern only
    """
    def __init__(self, prod_name):
        self.prod_name = prod_name
    
    @abstractmethod
    def clone(self):
        """
        Prototype pattern relies only on this method
        """
        pass
    
    def do_task(self):
        print("Printing from %s" % self.prod_name)
    
class ConcreteProduct1(AbstractProduct):
    prod_name = "Product 1"
    def __init__(self):
        AbstractProduct.__init__(self, self.prod_name)
        
    def clone(self):
        return copy.deepcopy(self)

class ConcreteProduct2(AbstractProduct):
    prod_name = "Product 2"
    def __init__(self):
        AbstractProduct.__init__(self, self.prod_name)
        
    def clone(self):
        return copy.deepcopy(self)
    
class AbstractFactory(ABC):
    """
    This is a part of abstract factory pattern, not prototype pattern
    """
    
    @abstractmethod
    def create_product(self, *arg, **kwarg):
        pass
    
class Factory(AbstractFactory):
    """
    Concrete factory. The difference here is that this factory clone existing
    prototypes instead of calling constructors to create new objects
    """
    _prototypes = {"product1" : ConcreteProduct1(), "product2" : ConcreteProduct2()}
    
    def create_product(self, prod_name):
        if(prod_name not in self._prototypes.keys()):
            print("%s not found" % prod_name)
            return None
        else:
            """
            Note that instead of calling constructor of the needed object,
            this factory clones an existing prototypal object
            """
            clone = self._prototypes[prod_name].clone()
            return clone
        
def main():
    factory = Factory()
    for i in range(1,5):
        product = factory.create_product("product%s" % i)
        if product:
            product.do_task()
            
if __name__ == "__main__":
    main()
    