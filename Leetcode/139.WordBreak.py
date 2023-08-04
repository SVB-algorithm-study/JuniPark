class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # cnt = 1
        # while cnt < len(s)+1:
        #     print(s[:cnt], s[cnt:])
        #     if s[:cnt] in wordDict :
        #         s = s[cnt:]
        #         print(s)
        #         cnt = 0
        #     if s[cnt:] in wordDict :
        #         s = s[:cnt]
        #         print(s)
        #         cnt = 0
        #     cnt += 1
        #     if s == "" : return True


        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break

        return dp[n]