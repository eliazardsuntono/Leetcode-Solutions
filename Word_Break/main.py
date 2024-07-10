def solution1 (s, wordDict):
        word_set = set(wordDict)
        lst = [False] * (len(s) + 1)
        lst[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if lst[j] and s[j:i] in word_set:
                    lst[i] = True
                    break
        
        return dp[-1]

if __name__ == "__main__":
	print(solution1("leetcode", ["leet", "code"]))

