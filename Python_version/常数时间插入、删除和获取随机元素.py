from random import choice

class Random:
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self,num):
        if num in self.dict:
            return False
        self.dict[num] = len(self.list)
        self.list.append(num)
        return True

    def remove(self,num):
        if num in self.dict:
            last,index = self.list[-1],self.dict[num]
            self.dict[last],self.list[index] = index,last
            self.list.pop()
            del self.dict[num]
            return True
        return False

    def random(self):
        return choice(self.list)
