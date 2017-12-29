#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:23:00 2017

@author: nguyentran

Builder pattern
Hide the complicated multi-step creation process of an object from client.
From the view of client, the creation process appears to be a single step.
Combined with abstract factory, client can build different types of objects
using the same creation process (i.e., calling the same method)

Involving parties:
    Client
    Product (i.e., the composite product to be built)
    Director (i.e., monitor of the creation process, invoke builders)
    Builder (i.e., a component of the director. Can be considered the 
             instruction to build a specific type of composite object)
    
If abstract factory is also used, builder can be replaced by an abstract builder
and multiple concrete builders for differents scenarios
"""

from abc import ABC, abstractmethod

#=================================================================
# Product (i.e., the composite object to be built)
# In this example, product has three parts
class Product:
    def __init__(self):
        self.part_a = "N/A"
        self.part_b = "N/A"
        self.part_c = "N/A"
        
    def getInfo(self):
        print("Part A: %s" % self.part_a)
        print("Part B: %s" % self.part_b)
        print("Part C: %s" % self.part_c)


#=================================================================
# Abstract builder
class AbstractBuilder(ABC):
    def __init__(self, builder_name):
        # Upon creation, the builder has an empty product
        # This product will be constructed step-by-step by build methods
        # This product will be returned to client
        self.product = Product()
        self.builder_name = builder_name
        
    @abstractmethod
    def build_part_a(self):
        pass
    
    @abstractmethod
    def build_part_b(self):
        pass
    
    @abstractmethod
    def build_part_c(self):
        pass
    
#=================================================================
# Concrete builders
class ConcreteBuilder1(AbstractBuilder):
    builder_name = "Concrete builder 1"
    def __init__(self):
        AbstractBuilder.__init__(self, self.builder_name)
        
    def build_part_a(self):
        self.product.part_a = "Build by %s" % self.builder_name
    
    def build_part_b(self):
        self.product.part_b = "Build by %s" % self.builder_name
    
    def build_part_c(self):
        self.product.part_c = "Build by %s" % self.builder_name
        
        
class ConcreteBuilder2(AbstractBuilder):
    builder_name = "Concrete builder 2"
    def __init__(self):
        AbstractBuilder.__init__(self, self.builder_name)
        
    def build_part_a(self):
        self.product.part_a = "Build by %s" % self.builder_name
    
    def build_part_b(self):
        self.product.part_b = "Build by %s" % self.builder_name
    
    def build_part_c(self):
        self.product.part_c = "Build by %s" % self.builder_name
        
        
#=================================================================
# Director
class Director:
    """
    Some examples instantiate the builder attribute upon the creation of
    a director object. This approach essentially ties a concrete builder to a director
    It means that the director is expected to server only one type of builder to build one type of product.
    
    This example assign builder to the director upon constructing a product.
    It means that a director can fulful different types of "order", represented by different type of builders,
    instead of being tied to a single type.
    """
    def __init__(self):
        self.builder = None
        
    def construct(self, builder):
        self.builder = builder
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()
        return self.builder.product
    
#=================================================================
# Client
def main():
    director = Director()
    product1 = director.construct(ConcreteBuilder1())
    print("Product 1")
    product1.getInfo()
    
    product2 = director.construct(ConcreteBuilder2())
    print("Product 2")
    product2.getInfo()
    
    """
    Notice how the creation of complex object is only one step from the perspective of a client
    """
    
if __name__ == "__main__":
    main()