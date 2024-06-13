def sort_cyclic_shifts(s):
    n = len(s)
    alphabet = 256
    
    # Initialize arrays
    p = [0] * n
    c = [0] * n
    cnt = [0] * max(alphabet, n)
    
    # Count characters in the string
    for i in range(n):
        cnt[ord(s[i])] += 1
    
    # Update cnt to store cumulative counts
    for i in range(1, alphabet):
        cnt[i] += cnt[i - 1]
    
    # Create the permutation array p
    for i in range(n - 1, -1, -1):
        cnt[ord(s[i])] -= 1
        p[cnt[ord(s[i])]] = i
    
    # Initialize equivalence classes and count of classes
    c[p[0]] = 0
    classes = 1
    
    # Assign equivalence classes c
    for i in range(1, n):
        if s[p[i]] != s[p[i - 1]]:
            classes += 1
        c[p[i]] = classes - 1
    
    pn = [0] * n
    cn = [0] * n
    
    # Iterate for each h, where (1 << h) < n
    h = 0
    while (1 << h) < n:
        for i in range(n):
            pn[i] = p[i] - (1 << h)
            if pn[i] < 0:
                pn[i] += n
        
        # Reset cnt and count classes
        cnt = [0] * classes
        for i in range(n):
            cnt[c[pn[i]]] += 1
        
        # Update cnt to store cumulative counts
        for i in range(1, classes):
            cnt[i] += cnt[i - 1]
        
        # Create the permutation array p
        for i in range(n - 1, -1, -1):
            cnt[c[pn[i]]] -= 1
            p[cnt[c[pn[i]]]] = pn[i]
        
        # Initialize equivalence classes and count of classes
        cn[p[0]] = 0
        classes = 1
        
        # Assign equivalence classes cn
        for i in range(1, n):
            cur = (c[p[i]], c[(p[i] + (1 << h)) % n])
            prev = (c[p[i - 1]], c[(p[i - 1] + (1 << h)) % n])
            if cur != prev:
                classes += 1
            cn[p[i]] = classes - 1
        
        # Swap c and cn
        c, cn = cn, c
        
        h += 1
    
    return p
