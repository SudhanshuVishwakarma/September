zeros = 0.0    
    neg = 0.0
    pos = 0.0
    length = len(arr)
    for i in range(0,length):
 
        if arr[i] == 0: 
            zeros= zeros + 1
 
        elif arr[i] < 0 : 
            neg = neg + 1
        else:
            pos = pos + 1 
    zeros = round(zeros/length,6)
 
    pos = round(pos/length,6)
 
    neg = round(neg/length,6)
 
    print(pos)
 
    print(neg)
 
    print(zeros)