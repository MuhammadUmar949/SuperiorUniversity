# Anagram Checker
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    count = {}
    for char in str1:
        count[char] = count.get(char, 0) + 1
    for char in str2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True

# Test cases
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False