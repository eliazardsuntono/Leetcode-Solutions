def solution(s):
    if not s:
        return 0

    char_set = set()
    left = 0
    max_len = 0
    
    for right in (len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)