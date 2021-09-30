def part(array, low, high):
    i = (low-1)         
    pivot = array[high]    
  
    for j in range(low, high):
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)
  
def quick_Sort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        x = part(array, low, high)
        quick_Sort(array, low, x-1)
        quick_Sort(array, x+1, high)
  
array = [13,1,1,4,8,9,4,7,15,20,100,99,7,8,2,3]
n = len(array)
quick_Sort(array, 0, n-1)
for i in range(n):
    print("%d" % array[i]),