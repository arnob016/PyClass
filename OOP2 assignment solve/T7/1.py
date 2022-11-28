#Write a Python class to find the three elements that sum to zero from a set (array) of n real numbers.

class ThreeSum:
    def __init__(self, arr1):
        self.arr1 = arr1
        print(self.arr1)

    def sum1(self):
        n = len(self.arr1)
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if self.arr1[i] + self.arr1[j] + self.arr1[k] == 0:
                        print(self.arr1[i], self.arr1[j], self.arr1[k])

arr1 = [-25, -10, -7, -3, 2, 4, 8, 10]
threeSum = ThreeSum(arr1)
threeSum.sum1()