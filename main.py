import time
import csv

class user:
  def __init__(self, ID, fName, lName, email):
    self.ID = int(ID)
    self.lName = lName
    self.fName = fName
    self.email = email

#import unsorted list
list_unsorted = []
with open("BIT605_unsorted_data.csv") as csv_file:
  reader = csv.reader(csv_file, delimiter=",")
  for row in reader:
    list_unsorted.append(user(row[0], row[1], row[2], row[3])),       reader.__next__

#Binary Search Tree
class Node:
  def __init__(self, user):

    self.left = None
    self.right = None
    self.userID = user.ID
    self.user = user

  def insert(self, user):
# Compare the new value with the parent node
    if self.user:
      if user.ID < self.userID:
        if self.left is None:
          self.left = Node(user)
        else:
          self.left.insert(user)
      elif user.ID >= self.userID:
        if self.right is None:
          self.right = Node(user)
        else:
          self.right.insert(user)
    else:
      self.user = user

  # Print the tree
  def printTree(self):
    if self.left:
      self.left.printTree()
    print(self.userID),
    if self.right:
      self.right.printTree()

  def findUser(self, search):
    if search < self.userID:
      if self.left is None:
        return str(search)+" is not found"
      return self.left.findUser(search)
    elif search > self.userID:
      if self.right is None:
        return str(search)+" is not found"
      return self.right.findUser(search)
    else:
      return str(self.userID) + " is found"

  def maxDepth(self, root):
    if root is None:
        return 0 ;
    else :
      # Compute the depth of each subtree
      lDepth = root.maxDepth(root.left)
      rDepth = root.maxDepth(root.right)
      # Use the larger one
      if (lDepth > rDepth):
        return lDepth+1
      else:
        return rDepth+1

  def listInOrder(self, root, list):
    if root:
        # First recur on left child
        root.listInOrder(root.left, list)
        # then add the data of node
        list.append(root.user),
        # now recur on right child
        root.listInOrder(root.right, list)

  def sortedArrayToBST(self, list):
    if not list:
        return None
    mid_val = len(list)//2
    node = Node(list[mid_val])
    node.left = self.sortedArrayToBST(list[:mid_val])
    node.right = self.sortedArrayToBST(list[mid_val+1:])
    return node 

print ("BIT605 - Binary search tree\n----------\n")

starttime = time.time()
BST = Node(list_unsorted[0])
for i in range(1,len(list_unsorted)):
  BST.insert(list_unsorted[i])
print ("Time to create BST: " + str((time.time()-starttime)*1000) + "\n")

starttime = time.time()
print(BST.findUser(602))
print ("Time: " + str((time.time()-starttime)*1000))
starttime = time.time()
print(BST.findUser(345))
print ("Time: " + str((time.time()-starttime)*1000))
starttime = time.time()
print(BST.findUser(720))
print ("Time: " + str((time.time()-starttime)*1000) + "\n")
print("Left side length = " + str(BST.maxDepth(BST.left)))
print("Right side length = " + str(BST.maxDepth(BST.right)) + "\n")

LtoRTree = []
BST.listInOrder(BST, LtoRTree)
left = LtoRTree[:(len(LtoRTree)//2)-1]
right = LtoRTree[len(LtoRTree)//2:]
baseRootValue =  (int(len(LtoRTree)/2))

starttime = time.time()
newBST = Node(LtoRTree[baseRootValue])
newBSTL = newBST.sortedArrayToBST(left)
newBST.left = newBSTL
newBSTR = newBST.sortedArrayToBST(right)
newBST.right = newBSTR
print ("Time to create new BST: " + str((time.time()-starttime)*1000) + "\n")

BST = newBST

starttime = time.time()
print(BST.findUser(602))
print ("Time: " + str((time.time()-starttime)*1000))
starttime = time.time()
print(BST.findUser(345))
print ("Time: " + str((time.time()-starttime)*1000))
starttime = time.time()
print(BST.findUser(720))
print ("Time: " + str((time.time()-starttime)*1000) + "\n")
print("Left side length = " + str(BST.maxDepth(BST.left)))
print("Right side length = " + str(BST.maxDepth(BST.right)))