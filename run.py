s = "1123"
n = len(s)
results = [""]

i = 0
while i < n:
    new_results = []
    
    # Single digit decoding
    if '1' <= s[i] <= '9':
        for result in results:
            new_results.append(result + chr(ord('a') + int(s[i]) - 1))
    
    # Two digit decoding
    if i + 1 < n and '10' <= s[i:i + 2] <= '26':
        for result in results:
            new_results.append(result + chr(ord('a') + int(s[i:i + 2]) - 1))
    
    results = new_results
    i += 1

print(results)
