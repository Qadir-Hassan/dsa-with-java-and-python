def buble_sort(arr):
    
    for i in range(len(arr)):

        swap = False

        for j in range(0,len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j] = arr[j+1]
                arr[j+1] = arr[j]
                swap = True


        if (swap == False) :
            break 
    return arr


nums = [4,5,2]
buble_sort(nums)

for i in range (len(nums)):
    print(nums[i])

               