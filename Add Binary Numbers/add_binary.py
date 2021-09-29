class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            biggest = a
            smallest = b
        else:
            biggest = b
            smallest = a
        smallest = (len(biggest) - len(smallest))*'0'+smallest
        smallest = smallest[::-1]
        biggest = biggest[::-1]
        total = []
        carry = 0
        for i in range(len(biggest)):
            if int(biggest[i]) + int(smallest[i]) + carry == 2:
                carry = 1;
                total.append(0)
            else:
                total.append(int(biggest[i]) + int(smallest[i]) + carry)
            if i+1 == len(biggest):
                
        if carry == 1:
            total.append(1)
        return total


def main():
    x = Solution()
    print(x.addBinary(a = "11", b = "1"))

if __name__ == "__main__":
    main()