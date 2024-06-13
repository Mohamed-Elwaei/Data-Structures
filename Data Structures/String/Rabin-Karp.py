def rabin_karp(s, t):
    p = 31  # A prime number for polynomial hashing
    m = 10**9 + 9  # A large prime number for modulo

    # Calculate the lengths of the pattern and text
    S = len(s)
    T = len(t)

    # Precompute powers of p modulo m
    p_pow = [1] * max(S, T)
    for i in range(1, len(p_pow)):
        p_pow[i] = (p_pow[i - 1] * p) % m

    # Compute prefix hashes of the text
    h = [0] * (T + 1)
    for i in range(T):
        h[i + 1] = (h[i] + (ord(t[i]) - ord('a') + 1) * p_pow[i]) % m

    # Calculate the hash value of the pattern
    h_s = 0
    for i in range(S):
        h_s = (h_s + (ord(s[i]) - ord('a') + 1) * p_pow[i]) % m

    # Initialize a list to store occurrences
    occurrences = []

    # Search for occurrences using rolling hash
    for i in range(T - S + 1):
        # Calculate the hash of the current substring
        cur_h = (h[i + S]  - h[i]) % m

        # Check if the hash matches the pattern's hash
        if cur_h == h_s * p_pow[i] % m:
            # If there's a match, add the current index to occurrences
            occurrences.append(i)

    # Return the list of occurrences
    return occurrences

# Example usage:
text = "abracadabra"
pattern = "abra"
result = rabin_karp(pattern, text)
print("Occurrences:", result)
