def sort(lst,ele,idx=0):
    if(ele<lst[idx]):
        lst.insert(idx,ele)
        return lst
    elif(idx==len(lst)-1):
        lst.append(ele)
        return lst
    return sort(lst,ele,idx)

def insert(lst,idx):
    if(idx+1==len(lst)):
        return lst
    elif(lst[idx+1]<lst[idx]):
        ele=lst[idx+1]
        del lst[idx+1]
        sort(lst,ele)
    return insert(lst,idx+1)
    
lst=[4,3,8,6,1,2]
print("sorted list is:",insert(lst,0))
