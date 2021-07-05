a1 = "1.0.0"
a2 = "1.0.1"


def comp_version(a1,a2):
    a1_list = a1.split('.')
    a2_list = a2.split('.')
    
    n1 = len(a1_list)
    n2 = len(a2_list)
    
    for i in range(max(n1,n2)):
        i1 = int(a1_list[i]) if i < n1 else 0
        
        i2 = int(a2_list[i]) if i<n2 else 0
        
        if i1!=i2:
            return 1 if i1>i2 else -1
        
    return 0

print(comp_version(a1,a2))