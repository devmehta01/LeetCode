class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        num = 1

        for _ in range(n):
            ans.append(num)

            if num * 10 <= n:
                num = num*10
            else:
                while num % 10 == 9 or num>=n:
                    num //= 10
                num += 1
        
        return ans