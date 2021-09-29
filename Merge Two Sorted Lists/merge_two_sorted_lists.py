# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if len(l1)==0 and len(l2)==0:
            return []
        if len(l1)==0:
            return l2
        if len(l2)==0:
            return l1
        if len(l1)>len(l2):
            max = l1
            min = l2
        else:
            max = l2
            min = l1
        result = []
        k = 0
        l = 0
        for i in range(len(max)+1):
            if len(min)>i:
                if max[k]>min[l]:
                    result.append(min[l])
                    l = l + 1
                elif max[k]==min[l]:
                    result.append(max[k])
                    result.append(min[l])
                    l = l + 1
                    k = k + 1
                else:
                    result.append(max[k])
                    k = k + 1
            else:
                result.append(max[k])
                k = k + 1
        return result

def main():
    x = Solution()
    print(x.mergeTwoLists([1,2,4], [1,3,4]))

if __name__=="__main__":
    main()