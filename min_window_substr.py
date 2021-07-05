from typing import Counter


str1 = "ADOBECODEBANC"
pattern = "ABC"

def find_string(str1,pattern):
    start , matched , substr_start = 0,0,0
    min_length = len(str1) + 1
    
    counter = Counter(pattern)
    
    
    for end in range(len(str1)):
        right = str1[end]
        if right in counter:
            counter[right]-=1
            if counter[right]>=0:
                matched+=1
        while matched == len(pattern):
            if min_length >end - start +1:
                min_length = end-start+1
                substr_start = start
            left = str1[start]
            start+=1
            if left in counter:
                if counter[left]==0:
                    matched-=1
                counter[left] +=1
    if min_length > len(str1):
        return ""
    return str1[substr_start:substr_start+min_length]
    
    
print(find_string(str1,pattern))


