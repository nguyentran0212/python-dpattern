#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:59:22 2018

@author: nguyentran

This pattern allows reusing instantiated objects. This is useful when the overhead
of object instantiation is high, a number of objects are already instantiated,
and the number of objects in use at one time is low.


Variation: the reusable pool itself can be an abstract class. In this abstract
pool, we can include factory methods. Concrete pools, such as for database or 
http connections, can implement factory methods.
"""

"""
This is pool of reusable objects
"""
class ReusablePool:
    def __init__(self, size):
        # _reusables is the pool of reusable objects
        self._reusables = [Reusable() for _ in range(size)]
        
    # client uses this method to get a reusable object
    def acquire(self):
        return self._reusables.pop()
    
    # client uses this method to return the reusable object
    def release(self, reusable):
        self._reusables.append(reusable)
        print("Size of the pool: %d" % len(self._reusables))
    
"""
This class represents the reusable object
"""    
class Reusable:
    def do_task(self):
        print("Printing from a reusable object")
        
"""
Client
"""
def main():
    pool = ReusablePool(10)
    obj = pool.acquire()
    obj.do_task()
    pool.release(obj)
    
if __name__ == "__main__":
    main()