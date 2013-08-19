#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: michaelg
# 

#
# This file contains implementation of various aggregation commands
# That can be used in mining FOR SELECT or FOR DISTINCT ... SELECT ... commands
#

LONG_HELP = """    Possible aggregation commands are:
      sum      - sum expression evaluated for each entry
      sumIf    - gets peer and returns sum of second elements for which first elements are True
      avg      - average value of expression
      count    - counts all occurances when expression evaluates to True
      number   - counts number of distinct values of expression
      superset - Merge values to the set
      first    - returns first seen value of expression
      last     - returns last seen value of expression
      append   - appens values to a list
      concat   - Concatinates lists to a single one
"""

class Base:
    def add(self, value):
        raise NotImplementedError
    def getValue(self):
        raise NotImplementedError

class Sum(Base):
    def __init__(self):
        self.mySum = 0
    def add(self, value):
        self.mySum += value
    def getValue(self):
        return self.mySum

class SumIf(Base):
    def __init__(self):
        self.mySum = 0
    def add(self, value):
        if value[0]:
            self.mySum += value[1]
    def getValue(self):
        return self.mySum

class Avg(Base):
    def __init__(self):
        self.mySum = 0
        self.myCnt = 0
    def add(self, value):
        self.mySum += value
        self.myCnt += 1
    def getValue(self):
        return float(self.mySum)/self.myCnt if self.myCnt > 0 else 0.

class Count(Base):
    def __init__(self):
        self.myCount = 0
    def add(self, value):
        if value:
            self.myCount += 1
    def getValue(self):
        return self.myCount

class Number(Base):
    def __init__(self):
        self.mySet = set()
    def add(self, value):
        self.mySet.add(value)
    def getValue(self):
        return len(self.mySet)


class Min(Base):
    def __init__(self):
        self.myMin = None
    def add(self, value):
        if not self.myMin:
            self.myMin = value
        else:
            self.myMin = min(self.myMin, value)
    def getValue(self):
        return self.myMin

class Max(Base):
    def __init__(self):
        self.myMax = None
    def add(self, value):
        if not self.myMax:
            self.myMax = value
        else:
            self.myMax = max(self.myMax, value)
    def getValue(self):
        return self.myMax

class Superset(Base):
    def __init__(self):
        self.mySet = set()
    def add(self, value):
        if isinstance(value,set):
            self.mySet |= value
        elif isinstance(value, list):
            for val in value:
                self.mySet.add(val)
        else:
            self.mySet.add(value)
    def getValue(self):
        return self.mySet

class First(Base):
    def __init__(self):
        self.myVal = None
    def add(self, value):
        if self.myVal is None:
            self.myVal = value
    def getValue(self):
        return self.myVal

class Last(Base):
    def __init__(self):
        self.myVal = None
    def add(self, value):
        if value is not None:
            self.myVal = value
    def getValue(self):
        return self.myVal

class Append(Base):
    def __init__(self):
        self.myVal = []
    def add(self, value):
        self.myVal.append(value)
    def getValue(self):
        return self.myVal

class Concat(Base):
    def __init__(self):
        self.myVal = []
    def add(self, value):
        self.myVal.extend(value)
    def getValue(self):
        return self.myVal

