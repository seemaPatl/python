def min1(ls, ub, lb):
    '''
        Objective: to find th mininum of a list if the lower bound and upper 
              bound of the list is given
        Input Parameters:
            ls: list to be given
            ub: upper bound of the list
            lb: lower bound of the list
        Return Value: the minimun of the list in the bounds given is returned
    '''

    #Approach: recursion is being used
    if ub==lb:
        return ub
    elif ls[lb] <ls[ub]:
        return min1(ls,ub-1,lb)
    else:
        return min1(ls,ub,lb+1)

ls = [25,16,13,29,11,66,14]
ub = 6
lb = 0
print ("list is :", ls)
print("Minimum in the list",min1(ls,ub,lb))
