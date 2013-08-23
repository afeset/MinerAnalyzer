'''
Created on Aug 7, 2013

@author: asaf
'''
class Pair:
    def __init__(self, key, value):
        self.key=key
        self.value=value
    
    def Bla(self, i):
        print(6+i)    
class Test2:
    def run(self):
        list=[]
        list.append(Pair(1,2))
        list.append(Pair(3,4))
        
        return list

