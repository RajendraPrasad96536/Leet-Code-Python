class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,
                 'D':500, 'M':1000, 'IV':4, 'IX':9,
                 'XL':40, 'XC':90, 'CD':400 , 'CM':900}
        num = []
        i=0
        while i<len(s):
            if s[i] and s[i:i+2] in roman:
                num.append(roman[s[i:i+2]])
                i = i + 2
            else:
                num.append(roman[s[i]])
                i=i+1
        return sum(num)

def main():
    x = Solution()
    print(x.romanToInt('MCMXCIV'))

if __name__=="__main__":
    main()