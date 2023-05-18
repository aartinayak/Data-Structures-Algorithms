"""
Question: 

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # Initialize the starting point to the first element
        # and the ending point to the last element
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, (row*col)-1

        while left <= right:

            mid = (left + right)//2  # Compute the mid position to start the search from

            # Convert the flat index into the row and column number
            # "//" --> gives the row, "%"" --> gives the column
            curr_num = matrix[mid//col][mid%col]

            # Check if the current number is our target number
            if curr_num == target:
                return True

            # Check if the current number is greater than our target number,
            # and if so, we check on the left side of our lists.
            elif curr_num > target:
                right = mid - 1
            
            # If the current number is lesser than our target number,
            # we check on the right side of our lists.
            else:
                left = mid + 1
        
        return False
    
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))