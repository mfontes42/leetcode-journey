class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        len_n = len(nums)
        
        for i in range(len_n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            b = i + 1 
            c = len_n - 1  
            
            while b < c:
                soma = nums[i] + nums[b] + nums[c]
                
                if soma == 0:
                    result.append([nums[i], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
                        
                elif soma < 0:
                    b += 1 
                else:
                    c -= 1 
                    
        return result