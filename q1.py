def decode_msg():
    top_secret = ['through', 'day', 'calm', 'vibrant', 'jumping', 'waters',
                  'energizes', 'reflecting', 'sunlight', 'A', 'keenly',
                  'ponds', 'frogs', 'near', 'quietly', 'opulent']
    
    # Insertion Sort
    for i in range(1, len(top_secret)):
        key = top_secret[i]
        j = i - 1
        
        # Compare words case-insensitively
        while j >= 0 and top_secret[j].lower() > key.lower():
            top_secret[j + 1] = top_secret[j]
            j -= 1
        
        top_secret[j + 1] = key
    
    # Join into a single string
    return " ".join(top_secret)

print(decode_msg())
