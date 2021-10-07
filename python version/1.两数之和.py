class solution:
    def Sum(nums,target):
        hashmap = dict()
        for i,num in enumerate(nums):
            if(target - num in hashmap):
                return [hashmap[target - num],i]
            hashmap[num] = i
        return []
result = solution
print(result.Sum([3,3],6))
