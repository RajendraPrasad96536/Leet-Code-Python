class Solution:
    def addBinary(self, a: str, b: str) -> str:
        cary = 0
        num = ''
        if len(a)>len(b):
            first_num = a
            second_num = (len(a)-len(b))*'0' + b
        else:
            first_num = b
            second_num = (len(b) - len(a)) * '0' + a

        i = len(first_num)-1
        while i>-1:
            if int(first_num[i]) + int(second_num[i]) + cary == 2:
                num = num+'0'
                cary = 1
            else:
                num = num + str(int(first_num[i]) + int(second_num[i]) + cary)
                cary = 0
        if cary ==1:
            return '1'+num
        else:
            return num


# Defining main function
def main():
    x = Solution()
    print(x.addBinary('1010','1011'))

# Using the special variable
if __name__ == "__main__":
    main()






