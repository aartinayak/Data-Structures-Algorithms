# QuickFind implementation of a disjoint set.

# Quick Find Class 
class QuickFind():
    
    def __init__(self, size:int) -> None:
        """
        Initializes the root array to map the nodes to the root parent.
        
        Keyword arguments:
        size: The total number of elements
        """       
        self.root = [i for i in range(size)]
            
    def find(self, x:int) -> int:
        """
        Returns the root of the element.
        
        Keyword arguments:
        x: The node who's root is to be found.
        """
        return self.root[x]
    
    def union(self, x:int, y:int) -> None:
        """
        Makes disjoint sets of nodes and maps the roots of the given nodes based on the connectivtiy.
        
        Keyword arguments:
        x, y: nodes to form the graph components.
        """
        rootX = self.find(x)
        rootY = self.find(y)
        
        #  Checks if the nodes are isolated or are a part of a set.
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX  # Set the parent node of the new set.
                    
    def connected(self, x:int, y:int) -> bool:
        """
        Checks for direct/undirect connectivity between nodes.
        
        Keyword arguments:
        x, y: nodes to be check for connected.
        """
        return self.find(x) == self.find(y)
    
    
# Test Case
uf = QuickFind(10)
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
        
            
        
        
        