#做一个myrange类
# class MyrangeIterator:
#     def __init__(self,target):
#         self.index = 0
#         self.target = target
#     def __next__(self):
#         if self.index >self.target-1:
#             raise StopIteration
#         item = self.index
#         self.index +=1
#         return item
class Myrange:
    def __init__(self,counts):
        self.all_counts = counts

    def __iter__(self):
        for item in range(self.all_counts):
            yield item

# for item in Myrange(5):
#     print(item)
manager = Myrange(5)
item = manager.__iter__()
while True:
    try:
        iterator = item.__next__()
        print(iterator)
    except StopIteration as e:
        break
