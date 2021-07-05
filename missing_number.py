from typing import Counter


A = [0,1,3]

def missing_number(A):
    c = Counter(A)   
    print(c)
    for i in range(len(A)+1):
        if i not in c:
            return i
        
        
print(missing_number(A))