class RandomizedSet:

    def __init__(self):
        self.numsmap = {}
        self.numslist = []

    def insert(self, val: int) -> bool:

        if val in self.numsmap:
            return False

        self.numsmap[val] = len(self.numslist)
        self.numslist.append(val)

        return True

    def remove(self, val: int) -> bool:

        if val not in self.numsmap:
            return False

        valindex = self.numsmap[val]
        last = self.numslist[-1]

        # Move last element into val's position
        self.numslist[valindex] = last
        self.numsmap[last] = valindex

        # Remove last element
        self.numslist.pop()
        del self.numsmap[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.numslist)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
import random

