#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 18:15:01 2017

@author: nguyentran

Abstract factory pattern
Provide a same interface to create families of related or dependent objects

Client interact with interfaces declared by abstract factories and abstract products

"""

from abc import ABC, abstractmethod
"""
Python does not provide native support for abstract method. In other word, it allows 
a base abstract class to be instantiated, and it does not force children of 
a base abstract class to implement abstract methods.

Module abc (i.e., abstract base class) simulate these enforcements
ABC is a class
abstract method is a decorator
"""

#=================================================================
# Abstract factories
class AbstractFactory(ABC):
    def __init__(self, factoryName):
        self.factoryName = factoryName
    
    @abstractmethod
    def create_product_a(self):
        pass
    
    @abstractmethod
    def create_product_b(self):
        pass

#=================================================================
# Concrete factories
class ConcreteFactory1(AbstractFactory):
    # Concrete factory 1 is for usage context 1
    # It creates product A1 and B1
    factoryName = "factory 1"
    def __init__(self):
        AbstractFactory.__init__(self, self.factoryName)
    
    def create_product_a(self):
        return ConcreteProductA1()
    
    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    # Concrete factory 1 is for usage context 1
    # It creates product A1 and B1
    factoryName = "factory 2"
    def __init__(self):
        AbstractFactory.__init__(self, self.factoryName)
    
    def create_product_a(self):
        return ConcreteProductA2()
    
    def create_product_b(self):
        return ConcreteProductB2()

#=================================================================
# Abstract products
class AbstractProductA(ABC):
    @abstractmethod
    def method_a(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def method_b(self):
        pass

#=================================================================
# Concrete products
class ConcreteProductA1(AbstractProductA):
    """
    This is a concrete product A created by the concrete factory 1
    """
    def method_a(self):
        print("Called method_a of concrete product A1")

class ConcreteProductA2(AbstractProductA):
    """
    This is a concrete product A created by the concrete factory 2
    """    
    def method_a(self):
        print("Called method_a of concrete product A2")

class ConcreteProductB1(AbstractProductB):
    """
    This is a concrete product B created by the concrete factory 1
    """
    def method_b(self):
        print("Called method_b of concrete product B1")
        
class ConcreteProductB2(AbstractProductB):
    """
    This is a concrete product B created by the concrete factory 2
    """
    def method_b(self):
        print("Called method_b of concrete product B2")
        
#=================================================================
# Client
def main():
    """
    Clients only interact with abstract factory and abstract products
    This interaction doesn't change despite actual factories and products
    are different in different usage scenarios
    """
    def create_and_call_products(factory):
        print("Creating from factory: %s" % factory.factoryName)
        productA = factory.create_product_a()
        productB = factory.create_product_b()
        productA.method_a()
        productB.method_b()
    
    # Usage context 1
    factory = ConcreteFactory1()
    create_and_call_products(factory)
    
    # Usage context 2
    factory = ConcreteFactory2()
    create_and_call_products(factory)
    
    # Note that in two usage context, the interaction with products are the same
    
if __name__ == "__main__":
    main()
