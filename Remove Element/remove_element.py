class Solution:
    def removeElement(self, nums, val) :
        count = 0
        index = 0
        for i in range(len(nums)-1):
            print(i, nums[i])
            if nums[index] == val:
                del nums[index]
                count = count + 1
            index = index + 1
        return count, nums

def main():
    x = Solution()
    print(x.removeElement([0,1,2,2,3,0,4,2], 2))

if __name__ == "__main__":
    main()
