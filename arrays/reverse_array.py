"""
Problem: Reverse an array
Approach: Python slicing
Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverse_array(arr):
    return arr[::-1]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(reverse_array(arr))
