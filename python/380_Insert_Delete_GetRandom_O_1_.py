# Time Complexity - O(1)
# Space Complexity - O(1)

import random 
class RandomizedSet:

    def __init__(self):
        self.rdict = dict()
        self.rlist = list()

    def insert(self, val: int) -> bool:
        if  val in self.rdict:
            return False
        else:
            self.rdict[val] = len(self.rlist)
            self.rlist.append(val)
            print(self.rdict, self.rlist)

            return True

    def remove(self, val: int) -> bool:
        if val in self.rdict:
            self.rlist[self.rdict[val]] = self.rlist[-1]
            self.rlist.pop(-1)
            self.rdict.pop(val)
            print(self.rdict, self.rlist)

            return True
        
        return False


    def getRandom(self) -> int:
        return random.choice(self.rlist)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
