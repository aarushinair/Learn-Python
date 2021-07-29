#Write a Python program to find the longest common sub-string from two given strings
ef lcs(i, j, count) :  
      
    if (i == 0 or j == 0) :  
        return count    
    if (X[i - 1] == Y[j - 1]) : 
        count = lcs(i - 1, j - 1, count + 1)  
      
    count = max(count, max(lcs( i, j - 1, 0),  
                           lcs( i - 1, j, 0)))  
    return count 
  
# Driver code  
if _name_ == "_main_" : 
  
    X = "abcdxyz"
    Y = "xyzabcd"
  
    n = len(X) 
    m = len(Y) 
    print(lcs(n, m, 0))
