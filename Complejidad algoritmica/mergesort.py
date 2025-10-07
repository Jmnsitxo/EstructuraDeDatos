def mergeSort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr) //2
lefthalf= arr[:mid]
rightHalf = arr[mid:]

sortedLeft = mergesort(lefthalf)
sortedRight=mergesort(righthalf)

return merge(sortedleft, sortedright)

def merge (left ,right):
    result=[]
    i= j = 0

while i< len(left) and j <len(right):
    if left[i]<right[j]:
        result.append(left[i])
        

    


    
    
    
