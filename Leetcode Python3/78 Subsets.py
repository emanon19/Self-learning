class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # [] to [1]
        # [] [1] to [2] [1 2]
        # [] [1] [2] [1 2] to [3] [1 3] [2 3] [1 2 3]
        res = [[]]
        for i in nums:
            new = []
            for cur in res:
                temp = cur.copy()
                temp.append(i)
                new.append(temp)
            for cur in new:
                res.append(cur)

        return res