class Solution:
    def removeDuplicates(self, nums):
        index = 0
        final_len = len(nums)
        for i in range(len(nums)):
            if index<len(nums)-1:
                if nums[index] == nums[index+1]:
                    del nums[index]
                    initial_len = final_len - 1
                else:
                    index = index + 1
        return final_len

def main():
    x = Solution()
    print(x.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

if __name__ == "__main__":
    main()
