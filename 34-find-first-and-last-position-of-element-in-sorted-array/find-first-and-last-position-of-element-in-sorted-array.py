class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       
        l = []
        c=nums.count(target)
        if c>=2:
            l.append(nums.index(target))
            
            l.append(nums.index(target)+c-1)
            return l
        elif c==1:
            l.append(nums.index(target))
            l.append(nums.index(target))
            return l
        else:
            return [-1,-1]
        
        