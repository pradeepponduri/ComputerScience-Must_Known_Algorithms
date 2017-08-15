
# coding: utf-8

# In[ ]:

def mergesort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        rh=alist[:mid]
        lh=alist[mid:]
        mergesort(rh)
        mergesort(lh)
        
        i,j,k=0,0,0
        
        while i<len(lh) and j<len(rh):
            if lh[i]<rh[j]:
                alist[k]=lh[i]
                i=i+1
            else:
                alist[k]=rh[j]
                j=j+1
            k=k+1
        while i<len(lh):
            alist[k]=lh[i]
            i=i+1
            k=k+1
        while j<len(rh):
            alist[k]=rh[j]
            j=j+1
            k=k+1
    
    
alist=[55,25,22,17,8,6,3,25,24,7,25,0]
(mergesort(alist))
print(alist)     

