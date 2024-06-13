def build_suffix_array(text):
    # Create a list of (suffix, index) tuples
    suffixes = [(text[i:], i) for i in range(len(text))]
    
    # Sort the suffixes lexicographically
    suffixes.sort()
    
    # Extract the sorted indices to form the suffix array
    suffix_array = [index for _, index in suffixes]
    
    return suffix_array

def build_lcp_array(text, suffix_array):
    n = len(text)
    lcp = [0] * n
    inv_suffix_array = [0] * n

    # Initialize the inverse suffix array
    for i in range(n):
        inv_suffix_array[suffix_array[i]] = i

    k = 0  # Initialize the length of the common prefix

    for i in range(n):
        if inv_suffix_array[i] == n - 1:
            k = 0
            continue

        j = suffix_array[inv_suffix_array[i] + 1]

        while i + k < n and j + k < n and text[i + k] == text[j + k]:
            k += 1

        lcp[inv_suffix_array[i]] = k  # LCP value for the current suffix

        if k > 0:
            k -= 1  # Decrement k for the next iteration

    return lcp

# Example usage:
text = "ABABBAB"
suffix_array = build_suffix_array(text)
lcp_array = build_lcp_array(text, suffix_array)

# Print the LCP array
print("LCP Array:", lcp_array)
