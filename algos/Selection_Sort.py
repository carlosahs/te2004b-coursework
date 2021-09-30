arr = [1,2,3,10,9,4,5,7,8,7]

def Selection_Sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j                        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
  
Selection_Sort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])