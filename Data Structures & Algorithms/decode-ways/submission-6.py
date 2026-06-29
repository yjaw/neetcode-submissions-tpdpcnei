class Solution:
    def numDecodings(self, s: str) -> int:
        #...   0123
        #...   2101
        #... 111211
        dp0 = 1 # ""
        dp1 = 1 # 1st char

        for i in range(len(s)):
            
            if s[i] == '0':
                if i == 0 or int(s[i - 1]) == 0 or int(s[i - 1]) > 2:
                    return 0
                dp0, dp1 = dp1, dp0
                print("c1")
            else:
                if i > 0 and int(s[i - 1] + s[i]) <= 26 and s[i - 1] != '0':
                    dp0, dp1 = dp1, dp0 + dp1
                    print("c2")
                else:
                    dp0, dp1 = dp1, dp1
                    print("c3")
            print(i, dp0, dp1)
        return dp1
        # O(N), O(1)