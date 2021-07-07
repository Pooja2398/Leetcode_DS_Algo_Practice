def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                return i
            else:
                hashmap[i]=1
