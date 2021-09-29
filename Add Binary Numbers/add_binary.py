class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]

def main():
    x = Solution()
    print(x.addBinary(a = "11", b = "1"))

if __name__ == "__main__":
    main()