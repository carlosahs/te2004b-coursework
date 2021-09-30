arr = [14,18,19,20,16,17,2,1,5,4,7,9,7]

def Insertion_Sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
Insertion_Sort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
 
