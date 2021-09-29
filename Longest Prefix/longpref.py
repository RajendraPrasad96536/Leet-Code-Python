class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        smallest = sorted(strs, key=len)[0]
        strs = sorted(strs, key=len)[1:]
        common = ''
        flag = False
        for i in range(len(smallest)):
            for s in strs:
                if s[i]!=smallest[i]:
                    flag = True
                    break
            if flag==False:
                common = common + smallest[i]
            else:
                break
        return common

def main():
    x = Solution()
    print(x.longestCommonPrefix(["flower","flow","flight"]))

if __name__=="__main__":
    main()