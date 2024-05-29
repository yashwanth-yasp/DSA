class MinStack(object):

    def __init__(self):
        self.line = []

        

    def push(self, val):
        self.line.append(val)
        

    def pop(self):
        self.line.pop()

    def top(self):
        return self.line[0]

    def getMin(self):
        self.line.sort()
        return self.line[0]
        


obj = MinStack()
for val in range(5):
    obj.push(val)
obj.pop()
print(obj.list())
param_3 = obj.top()
param_4 = obj.getMin()
