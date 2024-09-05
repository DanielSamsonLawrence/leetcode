class Solution:
    def findMaxLength(self, nums):
        ans,cnt,pref=0,0,{0:-1}
        for i,num in enumerate(nums):
            cnt+=1 if num else -1
            if cnt in pref:
                ans=max(i-pref[cnt],ans)
            else:
                pref[cnt]=i
        return ans