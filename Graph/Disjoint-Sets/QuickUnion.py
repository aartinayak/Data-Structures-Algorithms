# QuickUnion implementation of a disjoint set.

# Quick Union Class
class QuickUnion():
    
    def __init__(self, size:int) -> None:
        """
        Initializes the root array to map the nodes to the root parent.
        
        Keyword arguments:
        size: The total number of elements
        """
        self.root = [i for i in range(size)]
        
    def find(self, x:int) -> int:
        """
        Returns the parent of the element.
        
        Keyword arguments:
        x: The node who's root is to be found.
        """
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x:int, y:int) -> None:
        """
        Makes disjoint sets of nodes and maps the parents of the given nodes.
        
        Keyword arguments:
        x, y: nodes to form the graph components.
        """
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            self.root[parentY] = parentX
            
    def connected(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)

# Test Case
uf = QuickUnion(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
        
            
            
        