#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:51:05 2018

@author: nguyentran

This pattern ensures that there is only one instance of the the class
in the entire system. It can be used to implement factories, for example.

The instance is not already available, then it is created upon request (i.e. lazy initialisation)
"""

class Singleton(type):
    """
    Create a new type of class that allows clients to access its own unique instance
    If I want to implement any class as a singleton, just make this class the 
    metaclass of the new one.
    """
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None
        
    def __call__(cls, *args, **kwargs):
        """
        the __call__ method is called when we invoke <Class>()
        it is called after __init__
        """
        # Lazy instantiation: create the instance when the class is called
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
    
class MyClass(metaclass=Singleton):
    """
    Example class
    """
    pass

class MyClass2:
    pass

def main():
    m1 = MyClass()
    m2 = MyClass()
    # m1 and m2 are the same instance
    print(m1 is m2)
    
    
    #m3 and m4 are different instances
    m3 = MyClass2()
    m4 = MyClass2()
    print(m3 is m4)
    
if __name__ is "__main__":
    main()