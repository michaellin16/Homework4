# Code for binary tree
import cProfile
import random
import time


class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


n = 1000
# Use the insert method to add nodes
start = time.perf_counter()
arr = random.sample(range(0, 200000), n)
root = Node(arr[0])
for i in range(1, len(arr)):
    root.insert(arr[i])

endPoint = 200
testArr = random.sample(range(0, 200000), endPoint)

for i in range(0, endPoint):
    root.insert(testArr[i])
end = time.perf_counter()
print("Binary Tree Time:", end - start)

# Hash table
# Size 10000
start2 = time.perf_counter()
dictArrKey = random.sample(range(0, 200000), n)
dictArrVal = random.sample(range(0, 200000), n)
hashTable = {}
for i in range(0, len(dictArrVal)):
    hashTable[dictArrKey[i]] = dictArrVal[i]

testArr2 = random.sample(range(0, 200000), endPoint)
testArr3 = random.sample(range(0, 200000), endPoint)

for i in range(0, len(testArr2)):
    hashTable[testArr2[i]] = testArr3[i]
end2 = time.perf_counter()
print("Hash Table Time:", end2 - start2)
