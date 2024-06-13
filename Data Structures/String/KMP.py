def compute_prefix_function(s):
    n = len(s)
    pi = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]

        if s[i] == s[j]:
            j += 1

        pi[i] = j

    return pi


def kmp_search(text, pattern):
    prefix_table = compute_prefix_function(pattern)
    matches = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            matches.append(i - j + 1)
            j = prefix_table[j - 1]
    return matches

print(kmp_search('aadbbcbcac','dbbc'))
