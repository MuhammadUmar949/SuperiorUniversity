#  Longest Substring Without Repeating Characters python
def longest_substring_brute(s):
    max_len = 0
    result = ""
    for i in range(len(s)):
        seen = set()
        current = ""
        for j in range(i, len(s)):
            if s[j] not in seen:
                seen.add(s[j])
                current += s[j]
                if len(current) > max_len:
                    max_len = len(current)
                    result = current
            else:
                break
    return result

def longest_substring_sliding(s):
    char_index = {}
    left = max_len = 0
    result = ""
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        if right - left + 1 > max_len:
            max_len = right - left + 1
            result = s[left:right+1]
    return result

s = "abcabcbb"
print("Brute force:", longest_substring_brute(s))
print("Sliding window:", longest_substring_sliding(s))