def twoSum(numbers: list[int], target: int) -> list[int]:

        left, right = 1, len(numbers)


        while left <= right:

            curr_sum = numbers[left] + numbers[mid]

            if curr_sum == target:
                return [left+1, mid+1]
            elif curr_sum >= target:
                right -= 1
            else:
                left += 1

        return [1, -1]


print(twoSum([2, 3, 4], 6))
