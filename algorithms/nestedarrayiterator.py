'''
n an array of arrays,
e.g. given [[], [1, 2, 3], [4, 5], [], [], [6, 7], [8], [9, 10], [], []], 
print: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Implement an iterator that supports hasNext(), next() and remove() methods.
'''

class NestedArrayIterator:

    def __init__(self, nestedArray):
        self.nestedArray = nestedArray
        self.currentIndex = 0
        self.subIndex = 0

    def hasNext(self):
        if self.currentIndex < len(self.nestedArray):
            if type(self.nestedArray[self.currentIndex]) is list \
                and len(self.nestedArray[self.currentIndex]) == 0:
                self.currentIndex = self.currentIndex + 1
                return self.hasNext()
            return True
        return False

    def next(self):
        element = self.nestedArray[self.currentIndex]
        if type(element) is list:
            if self.subIndex < len(element):
                subElement = element[self.subIndex]
                self.subIndex = self.subIndex + 1
                if self.subIndex == len(element):
                    self.subIndex = 0
                    self.currentIndex = self.currentIndex + 1
                return subElement
        self.currentIndex = self.currentIndex + 1
        return element

    def remove(self, index):
        if index < len(self.nestedArray):
            del self.nestedArray[index]

nestedArray = NestedArrayIterator([[], [1, 2, 3], [4, 5], [], [], [6, 7], [8], [9, 10], [], []])
while nestedArray.hasNext():
    print nestedArray.next()