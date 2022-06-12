def maxArrayProduct(arr, n):
    result = arr[0]
 
    for i in range(n):
     
        mul = arr[i]
       
        for j in range(i + 1, n):
         
            result = max(result, mul)
            mul *= arr[j]

        result = max(result, mul)
     
    return result
 

# Driver code
arr = [ 5, -1, -4, 0, 2, -6, -1 ]
n = len(arr)
print("Maximum product in Sub Array is" , maxArrayProduct(arr, n))
