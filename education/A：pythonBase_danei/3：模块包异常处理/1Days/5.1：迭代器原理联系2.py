#做一个myrange类
class MyrangeIterator:
    def __init__(self,target):
        self.index = 0
        self.target = target
    def __next__(self):
        if self.index >self.target-1:
            raise StopIteration
        item = self.index
        self.index +=1
        return item
class Myrange:
    def __init__(self,counts):
        self.all_counts = counts

    def __iter__(self):
        return MyrangeIterator(self.all_counts)

for item in Myrange(5):
    print(item)

# for item in range(5):
#     print(item)

