import pdb
pdb.set_trace()
def mergesort(lst1,lst2,lst3=[],idx1=0,idx2=0):
    '''
    objective:to merge two sorted list into third list
    input parameters:
        lst1,lst2:two sorted list 
        lst3:third list with elements of the lst1 and lst2 sorted
    approach:using recursion
    '''
    if (len(lst3)==len(lst1)+len(lst2)):
        return (lst3)
    elif (len(lst1)==idx1):
        lst3.extend(lst2[idx2:])
        return (lst3)
    elif (len(lst2)==idx2):
        lst3.extend(lst1[idx1:])
        return (lst3)
    elif (lst1[idx1]<=lst2[idx2]):
        lst3.append(lst1[idx1])
        idx1=idx1+1
        return mergesort(lst1,lst2,lst3,idx1,idx2)
    elif(lst1[idx1]>=lst2[idx2]):
        lst3.append(lst2[idx2])
        idx2=idx2+1
        return mergesort(lst1,lst2,lst3,idx1,idx2)

def main():
    '''
    objective:to merge two sorted list into third list
    input parameters:
        lst1,lst2:two sorted list 
        lst3:third list with elements of the lst1 and lst2 sorted
    approach:using recursion
    '''
    lst1=[1,4,5]
    lst2=[3,8 ,9,11]
    lst3=mergesort(lst1,lst2)
    print(lst3)
    
if __name__=='__main__':
    main()
