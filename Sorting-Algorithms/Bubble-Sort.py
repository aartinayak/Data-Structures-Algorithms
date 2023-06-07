"""_summary_
Implements the bubble sort algorithm from scratch.
Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order.

Space Complexity: O(1)

Time Complexity:
Best	O(n) -> Array is already sorted, no need for sorting
Worst	O(n2) -> Array is sorted in a descending order 
Average	O(n2)
"""


class bubble_sort():
    
    def unoptimized_bubble_sort(self, elements: list) -> list:
        
        #  Iterate through each element of the list
        for i in range(len(elements)):
            
            #  Iterate through all elements of the list that are not sorted
            for j in range(len(elements) - i - 1):
                
                #  Swap the elements in place if they are not in the sorted order
                if elements[j] > elements[j+1]:
                    elements[j], elements[j + 1] = elements[j + 1], elements[j]
                    
                    
        return elements

    def optimized_bubble_sort(self, elements: list) -> list:
        
        #  Intoduce an extra variable swap to check if the array is already sorted,
        #  To avoid extra computation
        
        for i in range(len(elements)):
            
            swap = False
            
            for j in range(len(elements) - i - 1):
                if elements[j] > elements[j + 1]:
                    elements[j], elements[j + 1] = elements[j + 1], elements[j]
                    
                    swap = True
            
            #  Implies that the elements are already sorted
            if not swap:
                return elements
            
        return elements
    
    
    
def main():
    
    obj = bubble_sort()
    print(obj.unoptimized_bubble_sort())
    print(obj.optimized_bubble_sort([-2, 45, 0, 11, -9]))
    
    
main()
