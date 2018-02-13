# Tuple: tuple = ('a', 'b', 'c')
# List:  list = ['a', 'b', 'c']
# Dictionary: {'a':1, 'b':2, 'c':3}

class solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        temp = []
        for idx in range(len(nums)):
            temp = temp + [(nums[idx],idx)]
        sort = sorted(temp)[::-1] 
        # If temp is a list containing lists/tuples, it will be sorted based on the first elements
        #sorted(x)[::-1] returns decedant sorted array
        #sorted(x)[::1]  returns ascendant sorted array                          
        
        sorted_nums = [0]*len(nums)    #create a List of length len(nums) and initialize it to 0
        for idx in range(len(nums)):
            if idx == 0: sorted_nums[sort[idx][1]]="First"
            elif idx == 1: sorted_nums[sort[idx][1]] = "second"
            elif idx == 2: sorted_nums[sort[idx][1]] = "third"
            else: sorted_nums[sort[idx][1]] = len(nums)-idx
        print(sorted_nums)
        return sorted_nums
    
  # a = solution()
  # a.findRelativeRanks([5, 8, 3, 2, 18, 34, 6, 9])
