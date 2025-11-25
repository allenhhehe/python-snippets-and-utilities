def compress_list(nums):
    """Compresses a list of numbers using run-length encoding.
  Example:
    [1,1,2,2,2,3,3,4,4,4,4] becomes [(1,2),(2,3),(3,2),(4,4)]
    """
  
    value=nums[0]
    count=1
    if not nums:      
        return []
    result=[]
    for i in range(1,len(nums)):
        if nums[i]==value:
            count+=1
            
        else:
            result.append((value,count))
            count=1
            value=nums[i]
            
    result.append((value,count))
    return result        

m=[1,1,2,2,2,3,3,4,4,4,4]
print(compress_list(m))

def conut_frenquent(n):
    """Counts the frequency of a number which appears most frenquently in the list.
    Example:
    [1,1,2,2,2,3,3,4,4,4,4] returns 4
    """
    if not n:
        return 0
    freq={}
    for i in n:
        freq[i]=freq.get(i,0)+1     # get here is used to get the value of the key i in the dictionary freq,the i means the number in the list,the 0 means if the ket i is not in the dictionary freq ,then return 0
        max_freq=max(freq,key=freq.get)   # the max method here is used to get the key with the maximum value in the dictionary freq ,the key=freq.get means we use the value of the key to compare
    return freq[max_freq]

     
n=[1,1,2,2,2,3,3,4,4,4,4]     
print(conut_frenquent(n))   



def remove_duplicate(d):
    """remove the duplicate in list 
    """
    duplicate=[]
    for i in range (len(d)-1):
        if i==0 or d[i]!=d[i-1]:
            duplicate.append((d[i]))
           
   
    return duplicate    
d=[1,1,2,2,2,3,3,4,4,4,4] 
print(remove_duplicate(d))


def remove_duplicate2(b):
    """remove the duplicate in list """
    no_duplicate=[]
    for i in b:
        if i not in no_duplicate:       # check if i is already in the list,if not ,append it to the list,but here we use the set to remove duplicate will be more efficient
            no_duplicate.append(i)       
    return no_duplicate
b=[1,1,2,2,2,3,3,4,4,4,4]
print(remove_duplicate2(b))


def reverse_list(c):
    """Reverses the given list."""
    clist=[]
    for i in range (len(c)-1,-1,-1):       #len(c)-1 is the last index of the list,-1 is the stop index but not include it,1 is the step
         clist.append(c[i])
    return clist
c=[1,2,3,4,5]
print(reverse_list(c))                  

"""def merge_sorted(a,b):
    Merges two sorted lists into one sorted list.
    merge=[]
   
    for i in range (len(a)):
        for j in range (len(b)):
         if i not in merge and a[i]<b[j]:
            merge.append(a[i])
            i+=1
        else:
                merge.append(b[j])
                j+=1    
    return merge
a=[1,3,5,7]
b=[2,4,6,8]
print(merge_sorted(a,b))            
"""
def merge_sorted(a,b):
    """Merges two sorted lists into one sorted list."""
    merge=[]
    i,j=0,0        #pointers for a and b doubly lists
    while i<len(a) and j<len(b):   #    loop until reach the end of either list
        if a[i]<b[j]:               # compare the elements at the pointers
            merge.append(a[i])     #   append the smaller element to the merged list
            i+=1
        else:
            merge.append(b[j])
            j+=1
    merge.extend(a[i:])
    merge.extend(b[j:])
    return merge
a=[1,3,5,7]
b=[2,4,6,8] 
print(merge_sorted(a,b))        
