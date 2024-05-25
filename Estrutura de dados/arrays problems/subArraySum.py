def subarraySum(nums: list[int], k: int) -> int:
        running = 0
        total = 0
        
        sum_frequency = {0: 1}
        
        for i in range(0, len(nums)):
            running += nums[i]
            target_sum = running - k
            
            if target_sum in sum_frequency:
                total += sum_frequency[target_sum]
            
            sum_frequency[running] = sum_frequency.get(running, 0) + 1
        
        return total

nums = [3,1,2,4]
k = 6

print(subarraySum(nums,k))

'''
PRECISA REVISAR 
https://interviewing.io/questions/subarray-sum-equals-k

'''