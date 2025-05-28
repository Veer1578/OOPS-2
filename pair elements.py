class pair_elememnts():
    def two_sum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target - num], i
            lookup[num] = i

value = int(input('Enter sum for which you want to find numbers: '))
print("Index1 = %d, Index2 = %d" % 
      
      pair_elememnts().two_sum((10, 20, 30, 40, 50, 60, 70), value))