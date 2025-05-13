# String Permutations
def permute(s):
    def backtrack(first=0):
        if first == n:
            result.append("".join(s))
            return
        for i in range(first, n):
            s[first], s[i] = s[i], s[first]
            backtrack(first + 1)
            s[first], s[i] = s[i], s[first]
    
    n = len(s)
    result = []
    backtrack()
    return result

# Test
print("Permutations of 'ABC':", permute(list("ABC")))