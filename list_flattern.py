def flatern(lst):
    newLst=[]
    for x in lst:
        if type(x)==type([]):
            newLt=flatern(x)
            newLst.extend(newLt)
            
        else:
            newLst.append(x)
    return newLst
            
            
lst1=[1,[2,[3,4,5],7],8]
print(flatern(lst1))
