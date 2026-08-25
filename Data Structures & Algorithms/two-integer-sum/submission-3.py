class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            needed=target-num

            if needed in seen:
                return [seen[needed],i]

            seen[num]=i


     #   seen = {}

      #  for i in range(len(nums)):
       #     needed = target - nums[i]

        #    if needed in seen:
         #       return [seen[needed], i]
#
     #       seen[nums[i]] = i
