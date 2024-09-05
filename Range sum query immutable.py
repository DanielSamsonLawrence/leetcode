class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        cur=0
        for n in nums:
            cur+=n
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        rsum=self.prefix[right]
        lsum=self.prefix[left-1] if left >0 else 0
        return rsum-lsum

