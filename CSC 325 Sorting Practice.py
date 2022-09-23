def merge_two_sorted_list(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i< len_a:
        sorted_list.append(a[i])
        i += 1
        
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
        
    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge_two_sorted_list(left, right)
    
    

if __name__ == '__main__':
    a = [5, 8, 12, 56, 20, 100]
    b = [7, 9, 45, 51]
    arr = [1,5,9,4,5,9]
    
    #print(merge_two_sorted_list(a,b))
    print(merge_sort(arr))