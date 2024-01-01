class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    result.append("FizzBuzz")
                else:
                    result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

"""
Time Complexity O(n)
Space Complexity O(n)

This is a simple if else statement.
"""
