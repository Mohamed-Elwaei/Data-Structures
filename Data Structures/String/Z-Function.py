def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        if i + z[i] > r:
            l = i
            r = i + z[i]
    
    return z

def count_distinct_substrings(s):
    k = 0  # Initialize the number of distinct substrings
    t = ""  # Initialize the string t
    
    for c in s:
        t = t + c  # Append the current character to t
        
        # Compute the Z-function for the reversed string t
        z_values = z_function(t[::-1])
        
        # Find the maximum value in the Z-function array
        z_max = max(z_values)
        
        # Calculate the number of new distinct substrings
        new_substrings = len(t) - z_max
        
        # Update the total count of distinct substrings
        k += new_substrings
    
    return k

# Example usage:
s = "abc"
result = count_distinct_substrings(s)
print("Number of distinct substrings:", result)
